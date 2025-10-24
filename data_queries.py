"""
Data Queries Module
-------------------
This module contains SQL queries and data transformation functions
for fetching and processing data from Databricks.
"""

import pandas as pd
from data_connection import run_query
from config import DATABRICKS_CONFIG


def get_performance_data(retailer=None, campaign=None, keyword=None, week=None):
    """
    Fetch performance data with optional filters.
    
    Args:
        retailer (str): Filter by retailer (not in current schema, placeholder for future)
        campaign (str): Filter by campaign name
        keyword (str): Filter by keyword
        week (str): Filter by week commencing date
    
    Returns:
        DataFrame: Performance data with all metrics
    """
    catalog = DATABRICKS_CONFIG.get("catalog", "default")
    schema = DATABRICKS_CONFIG.get("schema", "bid_sample")
    
    # Base query - map columns to display names
    query = f"""
    SELECT 
        `Key` as keyword,
        `Name` as campaign_name,
        `Imp` as impressions,
        `Clicks` as clicks,
        `Sales` as sales_count,
        `Average auction ad rank` as avg_rank,
        `CTR` as ctr,
        `Conv. rate` as conversion_rate,
        `CPC` as cpc,
        `CPA` as cpa,
        `Cost` as spend,
        `Sales Val` as sales_value,
        `ROAS` as roas,
        `Week Commencing` as week_commencing,
        `Current Bid` as current_bid,
        `NewBids` as new_bids,
        `comments`,
        `Category` as category
    FROM {catalog}.{schema}.your_table_name
    WHERE 1=1
    """
    
    # Add filters
    if campaign and campaign != "All Campaign":
        query += f"\n    AND `Name` = '{campaign}'"
    
    if keyword and keyword != "All Keywords":
        query += f"\n    AND `Key` = '{keyword}'"
    
    if week:
        query += f"\n    AND `Week Commencing` = '{week}'"
    
    query += "\n    ORDER BY `Week Commencing` DESC, `Key`"
    
    return run_query(query)


def get_dashboard_metrics(week=None):
    """
    Fetch aggregated metrics for the dashboard KPI cards.
    
    Args:
        week (str): Filter by week commencing date
    
    Returns:
        dict: Dictionary of aggregated metrics
    """
    catalog = DATABRICKS_CONFIG.get("catalog", "default")
    schema = DATABRICKS_CONFIG.get("schema", "bid_sample")
    
    query = f"""
    SELECT 
        SUM(`Imp`) as total_impressions,
        AVG(`CPA`) as avg_cpa,
        AVG(`ROAS`) as avg_roas,
        AVG(`CTR`) as avg_ctr,
        AVG(`Conv. rate`) as avg_conversion_rate,
        AVG(`CPC`) as avg_cpc,
        SUM(`Clicks`) as total_clicks,
        AVG(`Average auction ad rank`) as avg_rank,
        SUM(`Cost`) as total_spend,
        SUM(`Sales`) as total_sales_count,
        SUM(`Sales Val`) as total_sales_value
    FROM {catalog}.{schema}.your_table_name
    WHERE 1=1
    """
    
    if week:
        query += f"\n    AND `Week Commencing` = '{week}'"
    
    df = run_query(query)
    
    if df.empty:
        return None
    
    # Convert to dictionary and format values
    row = df.iloc[0]
    
    return {
        'impressions': format_number(row['total_impressions']),
        'cpa': f"{row['avg_cpa']:.2f}",
        'roas': f"{row['avg_roas']:.2f}",
        'ctr': f"{row['avg_ctr']:.2f}%",
        'conversion_rate': f"{row['avg_conversion_rate']:.2f}%",
        'cpc': f"{row['avg_cpc']:.2f}",
        'clicks': format_number(row['total_clicks']),
        'avg_rank': f"{row['avg_rank']:.2f}",
        'spend': format_number(row['total_spend']),
        'sales_count': format_number(row['total_sales_count']),
        'sales_value': format_number(row['total_sales_value'])
    }


def get_chart_data(primary_kpi="Impressions", secondary_kpi="ROAS"):
    """
    Fetch time series data for the performance chart.
    
    Args:
        primary_kpi (str): Primary KPI metric name
        secondary_kpi (str): Secondary KPI metric name
    
    Returns:
        DataFrame: Time series data with weeks and selected KPIs
    """
    catalog = DATABRICKS_CONFIG.get("catalog", "default")
    schema = DATABRICKS_CONFIG.get("schema", "bid_sample")
    
    # Map display names to database columns
    kpi_mapping = {
        "Impressions": "Imp",
        "Clicks": "Clicks",
        "CTR": "CTR",
        "Conversion Rate": "Conv. rate",
        "ROAS": "ROAS",
        "CPA": "CPA",
        "CPC": "CPC",
        "Spend": "Cost"
    }
    
    primary_col = kpi_mapping.get(primary_kpi, "Imp")
    secondary_col = kpi_mapping.get(secondary_kpi, "ROAS")
    
    query = f"""
    SELECT 
        `Week Commencing` as week,
        SUM(`{primary_col}`) as primary_value,
        AVG(`{secondary_col}`) as secondary_value
    FROM {catalog}.{schema}.your_table_name
    GROUP BY `Week Commencing`
    ORDER BY `Week Commencing` ASC
    """
    
    return run_query(query)


def get_available_campaigns():
    """
    Get list of unique campaign names.
    
    Returns:
        list: List of campaign names
    """
    catalog = DATABRICKS_CONFIG.get("catalog", "default")
    schema = DATABRICKS_CONFIG.get("schema", "bid_sample")
    
    query = f"""
    SELECT DISTINCT `Name` as campaign_name
    FROM {catalog}.{schema}.your_table_name
    WHERE `Name` IS NOT NULL
    ORDER BY `Name`
    """
    
    df = run_query(query)
    if df.empty:
        return []
    return ["All Campaign"] + df['campaign_name'].tolist()


def get_available_keywords():
    """
    Get list of unique keywords.
    
    Returns:
        list: List of keywords
    """
    catalog = DATABRICKS_CONFIG.get("catalog", "default")
    schema = DATABRICKS_CONFIG.get("schema", "bid_sample")
    
    query = f"""
    SELECT DISTINCT `Key` as keyword
    FROM {catalog}.{schema}.your_table_name
    WHERE `Key` IS NOT NULL
    ORDER BY `Key`
    """
    
    df = run_query(query)
    if df.empty:
        return []
    return ["All Keywords"] + df['keyword'].tolist()


def get_available_weeks():
    """
    Get list of unique weeks.
    
    Returns:
        list: List of week commencing dates
    """
    catalog = DATABRICKS_CONFIG.get("catalog", "default")
    schema = DATABRICKS_CONFIG.get("schema", "bid_sample")
    
    query = f"""
    SELECT DISTINCT `Week Commencing` as week
    FROM {catalog}.{schema}.your_table_name
    WHERE `Week Commencing` IS NOT NULL
    ORDER BY `Week Commencing` DESC
    """
    
    df = run_query(query)
    if df.empty:
        return []
    return df['week'].tolist()


def format_number(num):
    """
    Format large numbers with K, M suffixes.
    
    Args:
        num: Number to format
    
    Returns:
        str: Formatted number string
    """
    if pd.isna(num):
        return "0"
    
    num = float(num)
    
    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return f"{num:.0f}"

