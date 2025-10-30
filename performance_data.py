"""
Performance Data Page
---------------------
This module contains the Performance Data page component.
"""

import streamlit as st
import pandas as pd


def render_performance_data():
    """
    Render the Performance Data page content.
    """
    # Add page background and styling to match Dashboard
    st.markdown("""
        <style>
        /* Light grey background for entire page */
        [data-testid="stAppViewContainer"] {
            background-color: #FCFCFC !important;
        }
        
        /* White container for main content with border shadow */
        section[data-testid="stMain"] > div:first-child {
            background-color: white;
            border-radius: 12px;
            padding: 32px;
            margin: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border: 1px solid #E5E7EB;
            max-width: 100%;
            overflow-x: hidden;
        }
        
        /* Prevent horizontal scroll */
        [data-testid="stAppViewContainer"] {
            overflow-x: hidden !important;
        }
        section[data-testid="stMain"] {
            overflow-x: hidden !important;
        }
        
        /* Custom background color for sidebar */
        section[data-testid="stSidebar"] {
            background-color: #FCFCFC !important;
            border-right: 1px solid #E5E7EB;
        }
        
        /* Ensure columns fit within viewport */
        [data-testid="column"] {
            max-width: 100% !important;
            overflow-x: hidden !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    render_performance_data_header()
    
    # Filter Section
    render_performance_filters()
    
    # Data Table
    render_performance_table()
    
    # Pagination
    render_pagination()


def render_performance_data_header():
    """Render the performance data header with title, description, and export button."""
    # Create columns for title/description and export button
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div style="margin-bottom: 8px;">
                <h1 style="font-family: 'Gilroy', sans-serif; font-weight: 700; font-size: 32px; color: #1F2937; margin: 0 0 8px 0;">
                    Performance Data
                </h1>
                <p style="font-family: 'Gilroy', sans-serif; font-weight: 400; font-size: 16px; color: #6B7280; margin: 0 0 8px 0;">
                    Monitor campaigns, review bids, and optimize performance all in one place.
                </p>
                <p style="font-family: 'Gilroy', sans-serif; font-size: 12px; color: #9CA3AF; margin: 0; font-style: italic;">
                    *all values are in the local currency
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Export Report Data Button
        st.markdown("""
            <div style="display: flex; justify-content: flex-end; align-items: flex-start; margin-top: 8px;">
                <button style="
                    background-color: #9333EA;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px 16px;
                    font-family: 'Gilroy', sans-serif;
                    font-weight: 500;
                    font-size: 14px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    gap: 8px;
                ">
                    <span>📥</span>
                    <span>Export Report Data</span>
                </button>
            </div>
        """, unsafe_allow_html=True)


def render_performance_filters():
    """Render the filter dropdowns section."""
    st.markdown("""
        <style>
        /* Reduce width of filter dropdowns in performance data page */
        .stSelectbox {
            max-width: 200px !important;
        }
        /* Reduce spacing between header and filters */
        div[data-testid="stVerticalBlock"] > div:has(+ div div[data-testid="column"]) {
            margin-bottom: 0px !important;
        }
        </style>
        <div style="margin-bottom: 24px; margin-top: -16px;">
            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
    """, unsafe_allow_html=True)
    
    # Create filter dropdowns with narrower columns
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 2])
    
    with col1:
        retailer = st.selectbox(
            "Retailer",
            ["Tesco", "Sainsbury's", "Asda", "Morrisons"],
            index=0,
            key="retailer_filter_perf"
        )
    
    with col2:
        campaign = st.selectbox(
            "Campaign",
            ["All Campaign", "Campaign 1", "Campaign 2", "Campaign 3"],
            index=0,
            key="campaign_filter_perf"
        )
    
    with col3:
        keyword = st.selectbox(
            "Keywords",
            ["All Keywords", "Keyword 1", "Keyword 2", "Keyword 3"],
            index=0,
            key="keywords_filter_perf"
        )
    
    with col4:
        week = st.selectbox(
            "Select Week",
            ["Week of Feb 24 2025", "Week of Feb 17 2025", "Week of Feb 10 2025", "Week of Feb 3 2025"],
            index=0,
            key="week_filter_perf"
        )
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Store filter values in session state for use in table rendering
    st.session_state['perf_retailer'] = retailer
    st.session_state['perf_campaign'] = campaign
    st.session_state['perf_keyword'] = keyword
    st.session_state['perf_week'] = week


def render_performance_table():
    """Render the performance data table using custom component."""
    from performance_table import performance_table
    
    # Get filter values from session state (for future data filtering)
    retailer = st.session_state.get('perf_retailer', 'Tesco')
    campaign = st.session_state.get('perf_campaign', 'All Campaign')
    keyword = st.session_state.get('perf_keyword', 'All Keywords')
    week = st.session_state.get('perf_week', 'Week of Feb 24 2025')
    
    # Create sample data with delta indicators
    # Each cell is an object with 'value' and 'deltaPercent' properties
    # In a real application, this data would be filtered based on the selected filters
    table_data = [
        {
            "Keywords": "Pringle",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Party",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Picnic",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Breakfast",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Crip",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Buffet",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Cereal",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Snacking",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Lunchbox",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        },
        {
            "Keywords": "Cocoa",
            "Impressions": {"value": "2.0M", "deltaPercent": 10},
            "*CPA": {"value": "0.33", "deltaPercent": 10},
            "Avg. Rank": {"value": "3.25", "deltaPercent": 10},
            "CTR": {"value": "1.15%", "deltaPercent": 10},
            "Conversion Rate": {"value": "2.33%", "deltaPercent": 10},
            "Click": {"value": "23.0K", "deltaPercent": 10},
            "ROAS": {"value": "2.58", "deltaPercent": 10},
            "*CPC": {"value": "0.15", "deltaPercent": 10},
            "Sales (Con)": {"value": "24.0K", "deltaPercent": 10},
            "*Sales (Rev)": {"value": "25.8K", "deltaPercent": 10},
            "*Spend": {"value": "10.0K", "deltaPercent": 10}
        }
    ]
    
    # Render the custom performance table component
    performance_table(data=table_data, key="performance_data_table")


def render_pagination():
    """Render the pagination controls."""
    st.markdown("""
        <div style="display: flex; justify-content: flex-end; align-items: center; margin-top: 24px; gap: 8px;">
            <button style="
                background-color: transparent;
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                color: #6B7280;
            ">‹</button>
            <button style="
                background-color: #9333EA;
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                color: white;
                font-weight: 500;
            ">1</button>
            <button style="
                background-color: transparent;
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                color: #6B7280;
            ">2</button>
            <button style="
                background-color: transparent;
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                color: #6B7280;
            ">3</button>
            <span style="color: #6B7280; padding: 0 8px;">...</span>
            <button style="
                background-color: transparent;
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                color: #6B7280;
            ">12</button>
            <button style="
                background-color: transparent;
                border: 1px solid #D1D5DB;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                color: #6B7280;
            ">›</button>
        </div>
    """, unsafe_allow_html=True)
