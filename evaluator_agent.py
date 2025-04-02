import os
import pandas as pd
import asyncio
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent, CodeExecutorAgent
from autogen_agentchat.ui import Console
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from autogen_ext.tools.code_execution import PythonCodeExecutionTool
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import MagenticOneGroupChat


CSV_FILE = "fake_data.csv"
MAX_TOKENS = 100000

az_model_client = AzureOpenAIChatCompletionClient(
    azure_deployment="gpt-4o",
    model="gpt-4o",
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
)

def analyze_csv(csv_file):
    """Reads CSV and extracts key model metrics."""
    try:
        df = pd.read_csv(csv_file)

        if df.empty:
            return "The CSV file is empty."

        model_metrics = df.to_dict(orient="records")
        return model_metrics
    except Exception as e:
        return f"Error reading CSV: {str(e)}"

async def main():
    model_client = az_model_client
    tool = PythonCodeExecutionTool(LocalCommandLineCodeExecutor(timeout=1000, work_dir=WORK_DIR))
    code_executor = LocalCommandLineCodeExecutor(timeout=1000, work_dir=WORK_DIR)

    evaluator_agent = AssistantAgent(
        "evaluator_agent", model_client, tools=[tool], reflect_on_tool_use=True
    )
    code_executor_agent = CodeExecutorAgent("code_executor_agent", code_executor)
    
    termination = TextMentionTermination("exit")
    team = MagenticOneGroupChat([evaluator_agent, code_executor_agent], model_client=model_client, max_stalls=20, max_turns=50)
 
    csv_summary = analyze_csv(CSV_FILE)

    # Evaluation Task
    evaluation_task = f"""
    Given the following model performance metrics, determine which model is the best and explain why.
    Here are the file summary:
    {csv_summary}

    **Task:**  
    1. Analyze the metrics.  
    2. Identify the best model based on metrics.  
    3. Justify why this model is the best.  
    4. If two models are close in performance, suggest trade-offs.  

    **Expected Output:**
    ```
    Best Model: <Model Name>
    Justification: <Why this model is the best?>
    Trade-offs: <If applicable>
    ```
    """
    try:
        result = await evaluator_agent.run(task=evaluation_task)
        print("Final result is  : ", result) 
    except Exception as e:
        print("Error occurred:", str(e))

asyncio.run(main())
