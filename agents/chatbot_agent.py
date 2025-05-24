# agents/chatbot_agent.py

class ChatbotAgent:
    def __init__(self):
        # In the future, connect to an AI model or local LLM here
        pass

    def chat(self, query):
        # Basic demo logic
        if "sales" in query.lower():
            return "Sales performance depends on pricing, customer demand, seasonal trends, and competitor activity."
        elif "inventory" in query.lower():
            return "Inventory optimization requires monitoring stock levels, turnover rates, and supplier reliability."
        elif "profit" in query.lower():
            return "Profitability in retail is influenced by margins, operational costs, and customer retention."
        else:
            return "I'm still learning. Please ask about sales, inventory, or profit for more insight."
