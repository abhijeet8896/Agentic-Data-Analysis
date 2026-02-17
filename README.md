# Agentic Data Analysis System

> An intelligent, tool-based data analysis agent powered by LangChain and Groq — capable of answering natural language questions about engineering performance metrics.

---

## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Tools](#tools)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
- [Agent Behavior](#agent-behavior)
- [Natural Language Handling](#natural-language-handling)

---

## Overview

The **Agentic Data Analysis System** is a CLI-based intelligent agent that lets you ask plain English questions about engineering performance data — and receive structured, insightful answers.

Built on LangChain's ReAct reasoning framework with Groq's Mixtral-8x7B model as the underlying LLM, the system autonomously selects the right analytical tool, processes your data with Pandas, and returns results as natural language explanations.

### Key Capabilities

-  **Anomaly Detection** — Spot unusual spikes or drops in any metric using Z-score analysis
-  **Aggregation** — Compute mean, sum, median, max, and min across any column
-  **Correlation Analysis** — Measure the Pearson correlation between any two variables
-  **Natural Language Interface** — Ask questions the way you'd ask a colleague

---

## System Architecture

```
User Query
    ↓
LangChain Agent  (ReAct-based reasoning)
    ↓
Tool Selection   (Aggregation / Correlation / Anomaly)
    ↓
Pandas Data Processing
    ↓
Structured Result
    ↓
Natural Language Explanation
```

The agent uses a **ReAct (Reasoning + Acting)** loop: it interprets your query, reasons about which tool to call, executes the tool, and generates a human-readable response — all in one seamless interaction.

---

## Project Structure

```
Agentic-data-analysis/
│
├── data/
│   └── samples_dev_metrics_daily.csv   # Engineering metrics dataset
│
├── tools.py          # Data analysis tool definitions
├── agent.py          # Agent setup (Groq + LangChain)
├── main.py           # CLI entry point
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Tools

### 1. Aggregation Tool

Performs standard statistical operations on any numeric column.

**Supported operations:** `mean` · `sum` · `median` · `max` · `min`

**Example Query:**
```
What is the mean of cycle time?
```

**Output:**
```json
{
  "metric": "cycle_time_in_days",
  "aggregation": "mean",
  "value": 12.8
}
```

---

### 2. Correlation Tool

Calculates the **Pearson correlation coefficient** between two variables and interprets the strength and direction of the relationship.

**Example Query:**
```
Is throughput correlated with cycle time?
```

**Output:**
```json
{
  "correlation": -0.62,
  "interpretation": "Moderate negative correlation"
}
```

---

### 3. Anomaly Detection Tool

Uses the **Z-score method** to identify statistical outliers — values where `|Z-score| > 3`. Returns the count of anomalies and the dates on which they occurred.

**Example Query:**
```
Find anomalies in throughput
```

**Output:**
```json
{
  "anomalies_detected": 3,
  "dates": ["2024-03-12", "2024-07-21"],
  "summary": "Detected unusual spikes/drops in throughput"
}
```

---

## Technologies

| Technology | Purpose |
|---|---|
| **Python** | Core language |
| **Pandas** | Data loading and processing |
| **NumPy** | Numerical computations (Z-scores) |
| **LangChain 0.1.x** | Agent framework and tool orchestration |
| **Groq API** | LLM inference backend |
| **llama-3.3-70b-versatile** | Underlying language model |

---

## Getting Started

### Prerequisites

- Python 3.8+
- A [Groq API key](https://console.groq.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-data-analysis.git
cd agentic-data-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your API Key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Run the Program

```bash
python main.py
```

---

## Usage Examples

Once the CLI is running, you can type natural language questions:

```
You: What is the average cycle time?
Agent: The mean cycle time is 12.8 days.

You: Find anomalies in throughput
Agent: 3 anomalies were detected in throughput on 2024-03-12 and 2024-07-21,
       indicating unusual spikes or drops during those periods.

You: Is commit count correlated with deployment frequency?
Agent: There is a moderate positive correlation (0.58) between commit count
       and deployment frequency.
```

---

## Agent Behavior

The agent follows the **ReAct** (Reason + Act) pattern on every query:

1. **Interpret** — Understand the user's intent and identify the target metric(s)
2. **Select** — Choose the most appropriate tool (aggregation, correlation, or anomaly detection)
3. **Execute** — Pass structured parameters to the tool and run the Pandas computation
4. **Explain** — Translate the raw result into a natural language response

Additional safeguards include:
- **Maximum iteration control** to prevent infinite reasoning loops
- **Error-safe tool execution** with graceful failure handling

---

## Natural Language Handling

Users can refer to metrics using casual language. The agent resolves these to the correct dataset column names via an internal alias mapping:

| User Says | Mapped Column |
|---|---|
| `"cycle time"` | `cycle_time_in_days` |
| `"commit count"` | `commits_count` |
| `"throughput"` | `throughput` |
| `"deployment frequency"` | `deployment_frequency` |

This makes the system robust to natural variation in how users describe their data.
