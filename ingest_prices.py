import requests
import snowflake.connector
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_and_load():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1"
    data = requests.get(url).json()

    ctx = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse='COMPUTE_WH',
        database='RAW',
        schema='COINGECKO'
    )
    cs = ctx.cursor()
    cs.execute("USE WAREHOUSE COMPUTE_WH")

    try:
        for coin in data:
            cs.execute("""
                INSERT INTO PRICES (id, symbol, name, current_price, market_cap, total_volume)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (coin['id'], coin['symbol'], coin['name'], coin['current_price'], coin['market_cap'], coin['total_volume']))
        print("Success: Data pushed to Snowflake!")
    finally:
        cs.close()
        ctx.close()

if __name__ == "__main__":
    fetch_and_load()
