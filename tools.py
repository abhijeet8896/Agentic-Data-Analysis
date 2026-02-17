import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/samples_dev_metrics_daily.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Normalize column names
df.columns = df.columns.str.strip()

# Column alias mapping (natural language → dataset column)
COLUMN_ALIASES = {
    "cycle count": "cycle_time_in_days",
    "cycle time": "cycle_time_in_days",
    "cycle time in days": "cycle_time_in_days",
    "throughput": "throughput",
    "commit count": "commits_count",
    "commits": "commits_count",
    "incidents": "incidents",
    "employee count": "employee_count",
    "employees": "employee_count"
}


def resolve_column(name: str):
    name = name.strip().lower()
    return COLUMN_ALIASES.get(name, name)


# 1️⃣ Aggregation Tool
def aggregate_metric(input_text: str):
    try:
        parts = input_text.split(",")

        if len(parts) != 2:
            return "Use format: metric,operation (example: throughput,mean)"

        metric, operation = parts
        metric = resolve_column(metric)
        operation = operation.strip().lower()

        if metric not in df.columns:
            return f"Invalid metric. Available: {list(df.columns)}"

        if operation not in ["mean", "sum", "median", "max", "min"]:
            return "Supported operations: mean, sum, median, max, min"

        value = getattr(df[metric], operation)()

        return {
            "metric": metric,
            "aggregation": operation,
            "value": round(float(value), 2)
        }

    except Exception as e:
        return f"Aggregation Error: {str(e)}"


# 2️⃣ Correlation Tool
def calculate_correlation(input_text: str):
    try:
        parts = input_text.split(",")

        if len(parts) != 2:
            return "Use format: metric1,metric2"

        metric1 = resolve_column(parts[0])
        metric2 = resolve_column(parts[1])

        if metric1 not in df.columns or metric2 not in df.columns:
            return f"Invalid metric. Available: {list(df.columns)}"

        correlation = df[metric1].corr(df[metric2])

        if abs(correlation) > 0.7:
            interpretation = "Strong correlation"
        elif abs(correlation) > 0.4:
            interpretation = "Moderate correlation"
        else:
            interpretation = "Weak correlation"

        return {
            "correlation": round(float(correlation), 2),
            "interpretation": interpretation
        }

    except Exception as e:
        return f"Correlation Error: {str(e)}"


# 3️⃣ Anomaly Detection Tool (Z-score method)
def detect_anomalies(metric: str):
    try:
        metric = resolve_column(metric)

        if metric not in df.columns:
            return f"Invalid metric. Available: {list(df.columns)}"

        series = df[metric]
        mean = series.mean()
        std = series.std()

        if std == 0:
            return "Standard deviation is zero. No anomalies possible."

        z_scores = (series - mean) / std
        anomalies = df[abs(z_scores) > 3]

        return {
            "anomalies_detected": int(len(anomalies)),
            "dates": anomalies["date"].dt.strftime("%Y-%m-%d").dropna().tolist(),
            "summary": f"Detected unusual spikes/drops in {metric}"
        }

    except Exception as e:
        return f"Anomaly Detection Error: {str(e)}"
