from crypto_api import get_crypto_price
from together_ai import get_together_ai_response

class AIAgent:
    def __init__(self):
        self.context = []

    def handle_message(self, message: str) -> str:
        """Processes the user's message and returns an appropriate response."""
        if "bitcoin price" in message.lower():
            price_data = get_crypto_price()
            # Check if price_data is a dictionary and contains currency prices
            if isinstance(price_data, dict):
                usd_price = price_data.get("USD")
                if usd_price:
                    response = f"The current price of Bitcoin is ${usd_price} USD."
                else:
                    response = "Sorry, Bitcoin price data is currently unavailable."
            else:
                response = price_data  # Return error message from get_crypto_price
        elif "translate" in message.lower():
            response = self.handle_translation_request(message)
        else:
            self.context.append(message)
            prompt = "\n".join(self.context)
            response = get_together_ai_response(prompt)
        
        self.context.append(response)
        return response

    def handle_translation_request(self, message: str) -> str:
        """Handles translation requests but keeps responses in English."""
        if "translate to" in message.lower():
            language = message.split("translate to")[-1].strip()
            return f"Translation feature activated for language: {language}. However, responses will remain in English."
        else:
            return "Please specify the language you want translation for."


if __name__ == "__main__":
    agent = AIAgent()
    print("AI Agent is running. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Ending conversation.")
            break
        response = agent.handle_message(user_input)
        print(f"AI Agent: {response}")
