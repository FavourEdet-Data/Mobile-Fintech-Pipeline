# 🤖 Real-Time Crypto Analytics Pipeline with AI Agent

> Automated cryptocurrency market analysis system that ingests real-time data, generates AI-powered insights, and delivers actionable alerts to Slack. Built entirely on mobile device using Termux.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-Data_Warehouse-29B5E8.svg)](https://www.snowflake.com/)
[![AI Agent](https://img.shields.io/badge/AI-Agent_Powered-orange.svg)]()
[![Slack](https://img.shields.io/badge/Slack-Notifications-4A154B.svg)](https://slack.com/)

## 📊 Project Overview

This project demonstrates an end-to-end automated data pipeline that:
- Ingests real-time cryptocurrency data from CoinGecko API
- Stores and transforms data in Snowflake data warehouse
- Uses AI agents to analyze market trends and identify opportunities
- Sends intelligent alerts to Slack for actionable insights
- Runs entirely on mobile infrastructure (Termux)

## 🏗️ Architecture
CoinGecko API → Python Ingestion → Snowflake DWH → AI Analysis → Slack Alerts
↓              (Termux)            ↓           (AI Agent)       ↓
Real-time                        Transformed                   Insights
Data                              Data                       Delivered
## ✨ Key Features

- **Real-Time Data Ingestion:** Automated API calls to CoinGecko every [X minutes/hours]
- **Cloud Data Warehouse:** Snowflake for scalable storage and transformation
- **AI-Powered Analysis:** LLM-based agent analyzes market patterns and anomalies
- **Intelligent Alerting:** Context-aware Slack notifications for significant events
- **Mobile-First Architecture:** Entire pipeline built and orchestrated on Android via Termux

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Data Source** | CoinGecko API |
| **Ingestion** | Python, Requests, Schedule |
| **Storage** | Snowflake Data Warehouse |
| **Transformation** | [SQL] |
| **AI Layer** | [OpenAI API] |
| **Orchestration** | [Python scripts] |
| **Alerting** | Slack Webhooks / Slack API |
| **Environment** | Termux (Android) |

## 🚀 What Makes This Unique

1. **Mobile-Native Development:** Entire pipeline built on smartphone using Termux
2. **AI-Driven Insights:** Not just data collection - intelligent analysis and recommendations
3. **Production-Grade Architecture:** Implements industry best practices (error handling, logging, scheduling)
4. **Real Business Value:** Delivers actionable intelligence, not just dashboards

## 📈 Sample Insights Generated

[Include 2-3 examples of actual insights your AI agent provided, e.g.:]

- "Bitcoin volatility increased 45% in last 4 hours - potential buying opportunity detected"
- "Ethereum trading volume spike detected across 3 major exchanges - investigating correlation with news events"
- "Portfolio alert: Top 3 holdings down 8% - consider rebalancing"

## 🔧 Setup & Usage

### Prerequisites
- Termux installed on Android device
- Snowflake account (free trial available)
- CoinGecko API key (free tier)
- Slack workspace with webhook URL
- [AI API key - Claude/OpenAI/etc.]

### Installation


# Install Termux packages
pkg install python git

# Clone repository
git clone https://github.com/FavourEdet-Data/Mobile-Fintech-Pipeline.git
cd Mobile-Fintech-Pipeline

# Install Python dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
Configuration
# config.py
SNOWFLAKE_ACCOUNT = "my_account"
SNOWFLAKE_USER = "snowflake_user"
SNOWFLAKE_WAREHOUSE = "compute_warehouse"
COINGECKO_API_KEY = "your_api_key"
SLACK_WEBHOOK_URL = "my_webhook_url"
AI_API_KEY = "my_ai_api_key"
Running the Pipeline
# One-time data ingestion
python ingest_crypto_data.py

# Start scheduled pipeline (runs every X hours)
python run_pipeline.py

# Test AI agent
python test_agent.py





📊 Data Model
Raw Layer:
crypto_prices_raw - Real-time price data from CoinGecko
market_metrics_raw - Volume, market cap, volatility metrics
Transformed Layer:
crypto_prices_hourly - Aggregated hourly price movements
price_changes_daily - Daily percentage changes and trends
volatility_metrics - Calculated volatility indicators
Insights Layer:
ai_generated_insights - AI agent analysis results
alert_history - Log of all Slack notifications sent

🎯 Business Impact
Automated 24/7 monitoring of cryptocurrency markets
Reduced analysis time from hours to seconds using AI
Proactive alerting for trading opportunities
Scalable architecture ready for production deployment

🔮 Future Enhancements
[ ] Add more data sources (Binance, Coinbase APIs)
[ ] Implement predictive models for price forecasting
[ ] Build interactive dashboard for historical insights
[ ] Add portfolio tracking and automated trading signals
[ ] Expand AI agent capabilities with RAG for news analysis

📝 Lessons Learned
Technical Challenges:
Managing API rate limits on free tier
Handling mobile network interruptions
Optimizing Snowflake costs with smart data retention
Solutions Implemented:
Implemented exponential backoff for API requests
Added error logging and automatic retry logic
Used dynamic tables in Snowflake for efficient updates

🤝 Connect
Built this project as part of my journey into AI-powered data engineering. I'm passionate about building systems that combine data infrastructure with intelligent automation.
LinkedIn: Favour Edet
Portfolio: favouredet-data.github.io

⭐ If you found this project interesting, please give it a star!

📬 Open to collaboration, feedback, and opportunities in Analytics Engineering and AI Automation.