import subprocess

class ChatbotAgent:
    def __init__(self, model="llama3"):
        self.model = model

    def ask(self, query):
        try:
            result = subprocess.run(
                ["ollama", "run", self.model],
                input=query.encode(),
                capture_output=True,
                timeout=60
            )
            response = result.stdout.decode().strip()
            return response or "No response from model."
        except subprocess.TimeoutExpired:
            return "Model took too long to respond."
        except Exception as e:
            return f"Error: {str(e)}"
