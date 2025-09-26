import os
import sys

# Add the parent directory to Python path BEFORE importing api_client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from dotenv import load_dotenv
from api_client import ApiClient

async def main():
    """
    Fetches and prints the available USDT balance for perpetuals trading.
    """
    load_dotenv()
    API_USER = os.getenv("API_USER")
    API_SIGNER = os.getenv("API_SIGNER")
    API_PRIVATE_KEY = os.getenv("API_PRIVATE_KEY")
    # API_KEY and API_SECRET are not needed for this client
    
    print("--- Testing Available Balance Endpoint ---")

    try:
        # Only pass the 3 required arguments (release_mode defaults to True)
        client = ApiClient(API_USER, API_SIGNER, API_PRIVATE_KEY)
    except ValueError as e:
        print(f"Initialization Error: {e}")
        return

    async with client:
        try:
            # You'll need to add a get_account_balance method to ApiClient
            # or use an existing method. Let me check what methods are available...
            
            # Looking at the code, I don't see a get_account_balance method
            # You might need to implement it or use a different method
            # For now, let's try to get position risk which might show balance info
            
            balance_data = await client.get_position_risk()
            print("\nPosition risk response:")
            print(balance_data)

        except Exception as e:
            print(f"\nAn error occurred during the test: {e}")

if __name__ == "__main__":
    asyncio.run(main())