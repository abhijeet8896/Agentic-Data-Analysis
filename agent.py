import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.tools import Tool
from langchain_groq import ChatGroq

from tools import detect_anomalies, aggregate_metric, calculate_correlation

load_dotenv()

# Initialize Groq model (stable working model)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Define tools
tools = [
    Tool(
        name="Aggregator",
        func=aggregate_metric,
        description="Use this to calculate mean, sum, median, max or min of a metric. Input format: metric,operation"
    ),
    Tool(
        name="CorrelationTool",
        func=calculate_correlation,
        description="Use this to calculate correlation between two metrics. Input format: metric1,metric2"
    ),
    Tool(
        name="AnomalyDetector",
        func=detect_anomalies,
        description="Use this to detect anomalies in a metric. Input: metric name"
    )
]

# Create agent (stable version)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    max_iterations=5,   # prevents infinite loop
    early_stopping_method="generate"
)
