"""
Configuration file for the Streamlit Dashboard
------------------------------------------------
This file contains all configurable settings for the application.
Modify these values to change app behavior without touching the main code.
"""

# =============================================================================
# DATA SOURCE CONFIGURATION
# =============================================================================
# Change this value to switch between data sources
# Options: "databricks" or "snowflake"
DATA_SOURCE = "databricks"


# =============================================================================
# DATABRICKS CONFIGURATION
# =============================================================================
# IMPORTANT: Do NOT hardcode credentials here!
# Set these values in environment variables or .streamlit/secrets.toml
#
# For environment variables, use:
#   - DATABRICKS_HOST
#   - DATABRICKS_TOKEN
#   - DATABRICKS_HTTP_PATH
#
# For Streamlit secrets, add to .streamlit/secrets.toml:
#   [databricks]
#   host = "your-workspace.cloud.databricks.com"
#   token = "your-token-here"
#   http_path = "/sql/1.0/warehouses/your-warehouse-id"

DATABRICKS_CONFIG = {
    "host": "",  # Set via environment variable DATABRICKS_HOST or secrets.toml
    "token": "",  # Set via environment variable DATABRICKS_TOKEN or secrets.toml
    "http_path": "",  # Set via environment variable DATABRICKS_HTTP_PATH or secrets.toml
    "catalog": "default",
    "schema": "bid_sample",
    "table_name": ""  # Add your table name here after testing in Help page
}


# =============================================================================
# SNOWFLAKE CONFIGURATION
# =============================================================================
SNOWFLAKE_CONFIG = {
    "account": "",
    "user": "",
    "password": "",
    "warehouse": "",
    "database": "",
    "schema": "",
    "role": ""
}


# =============================================================================
# APP CONFIGURATION
# =============================================================================
APP_CONFIG = {
    "page_title": "Dashboard",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

