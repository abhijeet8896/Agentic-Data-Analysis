from agent import agent

print("\n📊 Agentic Data Analysis System (Groq Powered)")
print("Type 'exit' to quit.")
print("\nTry questions like:")
print("- What is the mean of cycle time?")
print("- Find anomalies in throughput")
print("- Is throughput correlated with cycle time?")

while True:
    query = input("\nAsk a question: ")

    if query.lower() == "exit":
        print("Exiting...")
        break

    try:
        response = agent.invoke({"input": query})
        print("\nAnswer:\n", response["output"])
    except Exception as e:
        print("\nError occurred:", str(e))
