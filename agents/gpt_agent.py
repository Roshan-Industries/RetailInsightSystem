# gpt_agent.py

import requests

class GPTAgent:
    def __init__(self, model_name="tinyllama", api_url="http://localhost:11434/api/generate"):
        self.model = model_name
        self.api_url = api_url

    def ask(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.api_url, json=payload)
            if response.status_code == 200:
                return response.json().get("response", "No response generated.")
            else:
                return f"Error: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {str(e)}"
