# Sarvam AI Agent Assignment

## Overview
The Sarvam AI Agent is designed to fetch real-time Bitcoin prices and handle language translation requests, while maintaining English as the primary output language. It leverages the Together AI API for natural language processing capabilities and a cryptocurrency API for live price data.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone [repository_url]
   ```
2. **Create the virtual environment**:
   ```bash
   python -m venv env
   ```
3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. **Run the AI Agent**:
   - Open a command prompt or terminal.
   - Run the following command:
     ```bash
     python ai_agent.py
     ```
2. **Using the AI Agent**:
   - After starting, you’ll see a prompt where you can type a command. Examples include:
     - Asking for Bitcoin prices by typing "Bitcoin."
     - Requesting language translations or other general questions.

3. **Sample Interaction**:
   - **Prompt**:
     ```bash
     You: What is Bitcoin, and why is it considered valuable?
     ```
   - **AI Agent**:
     ```bash
     AI Agent: Bitcoin is considered valuable because of its decentralized nature, scarcity, and widespread adoption...
     ```

4. **Fallback Response**:
   - If the AI Agent doesn’t understand the question, it will provide a fallback response to guide you toward supported queries.

## Sample Questions

Here are some questions to get you started with the AI Agent:

1. **Bitcoin Basics**:
   - "What is Bitcoin, and why is it considered valuable?"
   - "Who invented Bitcoin, and what is the history behind it?"
   - "How does Bitcoin’s blockchain differ from other cryptocurrencies?"

2. **Bitcoin Price and Market Data**:
   - "How can I retrieve real-time Bitcoin price data using the Bitcoin API?"
   - "What API endpoints are available for tracking Bitcoin transaction history?"
   - "How can I get information on Bitcoin’s market cap, volume, and price changes using the API?"

3. **Technical and API-Specific Queries**:
   - "How does Bitcoin mining work, and what is the significance of hash rates?"
   - "What are some common criticisms of Bitcoin, and how are they addressed?"

### Sample Screenshots

1. **AI Agent Prompt**:
   - ![image](https://github.com/user-attachments/assets/c0b72d89-2158-44ec-a0b5-28dcd11985f2)

2. **User Query Example**:
   - ![image](https://github.com/user-attachments/assets/2da5307a-0c12-40ef-a5f4-df02e4e7bc22)

3. **Fallback Response**:
   - ![image](https://github.com/user-attachments/assets/5e83bb14-5525-41d4-bb15-809036a5597c)

This setup provides a flexible and responsive AI Agent for cryptocurrency queries and translation services. Happy exploring!
