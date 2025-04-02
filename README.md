# Evaluator-Agent-Evaluating-model-performance
This project automates the evaluation of machine learning model performance using Azure OpenAI GPT-4o and Autogen AgentChat. The system reads CSV files containing model metrics, analyzes the data, and determines the best-performing model based on predefined criteria.

## Features
✅ Reads and processes model performance metrics from a CSV file.
✅ Uses Azure OpenAI GPT-4o for intelligent analysis.
✅ Implements Autogen AgentChat to create AI-powered agents for evaluation.
✅ Supports Python code execution for additional analysis.
✅ Provides automated justification for model selection with trade-off suggestions.

## Prerequisites
Ensure you have the following installed:
```
Python 3.10+
```

## Environment Variables
Set up the following environment variables to authenticate with Azure OpenAI:
```
export AZURE_OPENAI_ENDPOINT="your_azure_openai_endpoint"
export AZURE_OPENAI_API_KEY="your_api_key"
```

## Installation
Clone the repository and install the required dependencies:
```
git clone <repository_url>
cd <repository_name>
pip install -r requirements.txt
```

## Usage
Place your CSV file (e.g., fake_data.csv) in the project directory.

Run the script:
```
python evaluator_agent.py
```

## How It Works
+ Reads CSV data and extracts model performance metrics.
+ Creates AI agents using Autogen to evaluate the models.
+ Runs an evaluation task where an AI agent analyzes the metrics, selects the best model, and provides justification.
+ Displays the final result, including trade-offs if multiple models are close in performance.

## Example Output
```
Best Model: Model_X  
Justification: Model_X outperforms others in accuracy and F1-score, making it the best choice.  
Trade-offs: Model_Y has lower latency but slightly lower accuracy.  
```

## Contributing
Feel free to contribute by opening issues or submitting pull requests! 🚀

## License
This project is licensed under the MIT License.