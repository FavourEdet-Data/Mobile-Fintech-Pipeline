import snowflake.connector
from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration from Environment
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = "#general" 

def check_market_and_notify():
    # 1. Connect to Snowflake using Env Variables
    ctx = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse='COMPUTE_WH',
        database='RAW',
        schema='COINGECKO'
    )
    cs = ctx.cursor()
    
    try:
        # 2. Query the performance view
        cs.execute("SELECT SYMBOL, CURRENT_PRICE, PERCENT_CHANGE FROM RAW.COINGECKO.DAILY_PERFORMANCE")
        results = cs.fetchall()
        
        if not results:
            print("No data found in view.")
            return

        message = "*Morning Fintech Report from your Mobile AI Agent* 📱\n\n"
        for row in results:
            symbol, price, change = row
            change_val = change if change is not None else 0.0
            emoji = "🚀" if change_val > 0 else "📉"
            message += f"{emoji} *{symbol.upper()}*: ${price:,.2f} ({change_val:+.2f}%)\n"
            
        # 3. Send to Slack
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        print("Success: Alert sent to Slack!")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cs.close()
        ctx.close()

if __name__ == "__main__":
    check_market_and_notify()
