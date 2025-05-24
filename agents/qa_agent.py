from agents.gpt_agent import GPTAgent

class QAAgent:
    def __init__(self):
        self.gpt = GPTAgent()

    def answer_question(self, question, context=""):
        prompt = f"{context}\n\nQuestion: {question}"
        return self.gpt.ask(prompt)
