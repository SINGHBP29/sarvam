import requests


TOGETHER_AI_API_KEY = "c849a64789c9d5386edbfde68053abb598eca6e37d8b63f3fcb38f743e65dcd2"
TOGETHER_AI_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"  
TOGETHER_AI_URL = "https://api.together.xyz/v1/chat/completions"  

def get_together_ai_response(prompt: str):
    """Fetches a response from Together AI's LLaMA 3.1 8B model based on the given prompt."""
    headers = {
        "Authorization": f"Bearer {TOGETHER_AI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": TOGETHER_AI_MODEL,
        "messages": [{"role": "user", "content": prompt}],  # Format for chat models
        "temperature": 0.7,
        "max_tokens": 150,  
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stream": False  
    }

    try:
        # Make the API request
        response = requests.post(TOGETHER_AI_URL, headers=headers, json=payload, timeout=20)
        response.raise_for_status()  # Raises an error for any HTTP issues

        data = response.json()
        if "choices" in data and "message" in data["choices"][0]:
            generated_response = data["choices"][0]["message"]["content"].strip()

          
            if len(generated_response.split()) < 3:  
                print("Response was too short. Retrying with a different prompt.")
                return get_together_ai_response(prompt)  # Retry the request

            return generated_response
        else:
            return "Error: 'choices' or 'message' key not found in response."

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to Together AI. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Error: Request to Together AI timed out."
    except requests.RequestException as e:
        return f"Error connecting to Together AI: {str(e)}"

prompt = input("Please enter a prompt for the AI model: ")
response = get_together_ai_response(prompt)
if response:
    print("\nGenerated Response:")
    print(response)
