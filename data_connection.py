"""
Data Connection Module
----------------------
This module handles connections to different data sources (Databricks or Snowflake).
It provides a unified interface regardless of which source is being used.
"""

import streamlit as st
from config import DATA_SOURCE, DATABRICKS_CONFIG, SNOWFLAKE_CONFIG


def get_data_source_name():
    """
    Returns the name of the currently configured data source.
    
    Returns:
        str: Name of the data source ("Databricks" or "Snowflake")
    """
    return DATA_SOURCE.title()


def initialize_databricks_connection():
    """
    Initialize connection to Databricks.
    
    Returns:
        connection: Databricks connection object (or None if not configured)
    """
    try:
        from databricks import sql
        import os
        

        # Check if required config is available
        # Priority: environment variables > secrets.toml > config.py
        host = os.getenv("DATABRICKS_HOST") or st.secrets.get("databricks", {}).get("host") or DATABRICKS_CONFIG.get("host")
        http_path = os.getenv("DATABRICKS_HTTP_PATH") or st.secrets.get("databricks", {}).get("http_path") or DATABRICKS_CONFIG.get("http_path")
        token = os.getenv("DATABRICKS_TOKEN") or st.secrets.get("databricks", {}).get("token") or DATABRICKS_CONFIG.get("token")
        
        if not all([host, http_path, token]):
            st.warning("Databricks configuration incomplete. Please set host, http_path, and token in config.py or environment variables.")
            return None
        
        # Create connection
        connection = sql.connect(
            server_hostname=host,
            http_path=http_path,
            access_token=token
        )
        
        return connection
        
    except ImportError:
        st.error("databricks-sql-connector not installed. Please run: pip install databricks-sql-connector")
        return None
    except Exception as e:
        st.error(f"Failed to connect to Databricks: {str(e)}")
        return None


def initialize_snowflake_connection():
    """
    Initialize connection to Snowflake.
    
    Returns:
        connection: Snowflake connection object (or None if not configured)
    """
    # TODO: Implement Snowflake connection logic
    # Example:
    # import snowflake.connector
    # connection = snowflake.connector.connect(
    #     account=SNOWFLAKE_CONFIG["account"],
    #     user=SNOWFLAKE_CONFIG["user"],
    #     password=SNOWFLAKE_CONFIG["password"],
    #     warehouse=SNOWFLAKE_CONFIG["warehouse"],
    #     database=SNOWFLAKE_CONFIG["database"],
    #     schema=SNOWFLAKE_CONFIG["schema"]
    # )
    # return connection
    
    return None


def get_connection():
    """
    Get the appropriate database connection based on the configured data source.
    This is the main function you'll call to get a connection.
    
    Returns:
        connection: Database connection object
    
    Raises:
        ValueError: If DATA_SOURCE is not "databricks" or "snowflake"
    """
    if DATA_SOURCE.lower() == "databricks":
        return initialize_databricks_connection()
    elif DATA_SOURCE.lower() == "snowflake":
        return initialize_snowflake_connection()
    else:
        raise ValueError(
            f"Invalid DATA_SOURCE: {DATA_SOURCE}. "
            "Must be 'databricks' or 'snowflake'"
        )


def run_query(query):
    """
    Execute a SQL query against the configured data source.
    
    Args:
        query (str): SQL query to execute
    
    Returns:
        DataFrame: Query results as a pandas DataFrame
    """
    import pandas as pd
    
    try:
        connection = get_connection()
        
        if connection is None:
            st.error("No database connection available")
            return pd.DataFrame()
        
        if DATA_SOURCE.lower() == "databricks":
            # Execute query using Databricks
            cursor = connection.cursor()
            cursor.execute(query)
            
            # Fetch results and convert to DataFrame
            columns = [desc[0] for desc in cursor.description]
            results = cursor.fetchall()
            df = pd.DataFrame(results, columns=columns)
            
            cursor.close()
            return df
            
        elif DATA_SOURCE.lower() == "snowflake":
            # Execute query using Snowflake
            df = pd.read_sql(query, connection)
            return df
        
        else:
            st.error(f"Unsupported data source: {DATA_SOURCE}")
            return pd.DataFrame()
            
    except Exception as e:
        st.error(f"Query execution failed: {str(e)}")
        return pd.DataFrame()


def test_connection():
    """
    Test if the database connection is working.
    
    Returns:
        bool: True if connection successful, False otherwise
    """
    try:
        connection = get_connection()
        if connection is None:
            return False
        
        # Test the connection with a simple query
        if DATA_SOURCE.lower() == "databricks":
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchall()
            cursor.close()
        elif DATA_SOURCE.lower() == "snowflake":
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchall()
            cursor.close()
        
        return True
        
    except Exception as e:
        st.error(f"Connection test failed: {str(e)}")
        return False


def close_connection(connection):
    """
    Close a database connection.
    
    Args:
        connection: Database connection object to close
    """
    try:
        if connection:
            connection.close()
    except Exception as e:
        st.warning(f"Error closing connection: {str(e)}")


def get_sample_data(table_name, limit=10):
    """
    Fetch sample data from a table.
    
    Args:
        table_name (str): Name of the table to query
        limit (int): Number of rows to fetch (default: 10)
    
    Returns:
        DataFrame: Sample data from the table
    """
    import pandas as pd
    
    # Add catalog and schema if configured for Databricks
    if DATA_SOURCE.lower() == "databricks":
        catalog = DATABRICKS_CONFIG.get("catalog", "")
        schema = DATABRICKS_CONFIG.get("schema", "")
        
        if catalog and schema:
            full_table_name = f"{catalog}.{schema}.{table_name}"
        else:
            full_table_name = table_name
    else:
        full_table_name = table_name
    
    query = f"SELECT * FROM {full_table_name} LIMIT {limit}"
    return run_query(query)


def list_tables():
    """
    List all available tables in the database.
    
    Returns:
        DataFrame: List of available tables
    """
    import pandas as pd
    
    try:
        if DATA_SOURCE.lower() == "databricks":
            catalog = DATABRICKS_CONFIG.get("catalog", "")
            schema = DATABRICKS_CONFIG.get("schema", "")
            
            if catalog and schema:
                query = f"SHOW TABLES IN {catalog}.{schema}"
            else:
                query = "SHOW TABLES"
        elif DATA_SOURCE.lower() == "snowflake":
            query = "SHOW TABLES"
        else:
            return pd.DataFrame()
        
        return run_query(query)
        
    except Exception as e:
        st.error(f"Failed to list tables: {str(e)}")
        return pd.DataFrame()

