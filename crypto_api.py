import requests
from cachetools import TTLCache
from rate_limit_cache import rate_limited

# API URL and cache settings
CRYPTO_API_URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
CACHE_TTL = 300  # Cache TTL set to 5 minutes

# Initialize cache
cache = TTLCache(maxsize=100, ttl=CACHE_TTL)

def get_crypto_price():
    """Fetches the current price of Bitcoin in USD, JPY, and EUR, with caching and rate limiting."""
    rate_limited()  # Apply rate limiting

    # Check if data is already cached
    if 'bitcoin_price' in cache:
        return cache['bitcoin_price']
    
    try:
        # Fetch data from the API
        response = requests.get(CRYPTO_API_URL)
        response.raise_for_status()
        data = response.json()
        
        # Extract prices directly from the response data
        bitcoin_price = {
            "USD": data.get("USD"),
            "JPY": data.get("JPY"),
            "EUR": data.get("EUR")
        }
        
        # Store in cache and return the price
        cache['bitcoin_price'] = bitcoin_price
        return bitcoin_price
    except requests.RequestException as e:
        return f"Error fetching Bitcoin price: {str(e)}"

# Test the function
print(get_crypto_price())
