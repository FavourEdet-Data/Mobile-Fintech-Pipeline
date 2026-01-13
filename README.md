<<<<<<< HEAD
# Mobile-Fintech-Pipeline
=======
# Mobile Fintech Pipeline: Project 1
An automated end-to-end data pipeline built entirely on Android via Termux.

## Tech Stack
- **Ingestion**: Python (Requests + Snowflake Connector)
- **Warehouse**: Snowflake (Cloud Data Warehouse)
- **Agentic AI**: Python + Slack SDK for automated market alerts
- **Environment**: Termux (Linux on Android)

## Steps Taken 
- **Environment Provisioning**: Configured a Termux (Android) Linux environment with a complete Python 3.12 data stack and managed environment variables via .env.
- **Snowflake Integration**: Established a secure connection to a Snowflake account to build the primary storage layer.
- **Agent Development**: Created observer_agent.py to act as an automated monitor, querying a Snowflake view and communicating findings to Slack.
- **Scheduler Deployment**: Leveraged the crond process to automate script execution every 30 minutes, verified with PID monitoring (pgrep crond).
- **Repository Sanitization**: Conducted a security overhaul by force-pushing a clean orphan branch to GitHub, effectively removing sensitive history and establishing a professional public codebase.

## Project Status
- **Active Protocol**: Step 1-4 & 6-7 Complete.
- **Next Phase**: Step 5 (dbt Transformation).
>>>>>>> 98d6fdc (Complete Automated Mobile Fintech Pipeline (Python + Snowflake + Slack))
