# Agentic Data Analysis System
## Project Overview

This project implements a tool-based Agentic Data Analysis System using:

LangChain

Groq LLM API

Pandas

Custom analytical tools

The system allows users to ask natural language questions about engineering performance metrics, and the agent intelligently selects the appropriate analytical tool to answer the query.

## Objective

Build an agentic system capable of:

Detecting anomalies in a selected metric

Performing aggregation operations (mean, sum, median, etc.)

Calculating correlation between variables

Answering user queries through a CLI interface

## System Architecture
User Query
     ↓
LangChain Agent (ReAct-based reasoning)
     ↓
Tool Selection (Aggregation / Correlation / Anomaly)
     ↓
Pandas Data Processing
     ↓
Structured Result
     ↓
Natural Language Explanation

## Project Structure
Agentic-data-analysis/
│
├── data/
│   └── samples_dev_metrics_daily.csv
│
├── tools.py          # Data analysis tools
├── agent.py          # Agent setup (Groq + LangChain)
├── main.py           # CLI interface
├── requirements.txt
└── README.md

## Technologies Used

Python

Pandas

NumPy

LangChain (0.1.x stable version)

Groq API

Mixtral-8x7B model

## Tools Implemented
1️. Aggregation Tool

Performs statistical operations:

Mean

Sum

Median

Max

Min

Example Query:

What is the mean of cycle time?


Output Format:

{
  "metric": "cycle_time_in_days",
  "aggregation": "mean",
  "value": 12.8
}

2️. Correlation Tool

Calculates Pearson correlation between two variables.

Example Query:

Is throughput correlated with cycle time?


Output Format:

{
  "correlation": -0.62,
  "interpretation": "Moderate negative correlation"
}

3️. Anomaly Detection Tool

Uses Z-score method to detect unusual spikes or drops.

Identifies values where |Z-score| > 3

Returns anomaly count and dates

Example Query:

Find anomalies in throughput


Output Format:

{
  "anomalies_detected": 3,
  "dates": ["2024-03-12", "2024-07-21"],
  "summary": "Detected unusual spikes/drops in throughput"
}

## Agent Behavior

The agent follows a ReAct reasoning pattern:

Interprets user intent

Selects appropriate tool

Passes structured parameters

Receives tool output

Generates natural language explanation

The agent is configured with:

Maximum iteration control (prevents infinite loops)

Error-safe tool execution

Natural language → column alias mapping

## Natural Language Handling

Users may refer to metrics differently than dataset column names.

Example:

"cycle time" → cycle_time_in_days

"commit count" → commits_count

This is handled using an internal column alias mapping system.

## How to Run
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Add Groq API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here

3️⃣ Run the Program
python main.py
