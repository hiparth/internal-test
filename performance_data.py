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
            <div style="margin-bottom: 24px;">
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
        <div style="margin-bottom: 32px;">
            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
    """, unsafe_allow_html=True)
    
    # Create filter dropdowns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.selectbox(
            "Retailer",
            ["Tesco", "Sainsbury's", "Asda", "Morrisons"],
            index=0,
            key="retailer_filter_perf"
        )
    
    with col2:
        st.selectbox(
            "Campaign",
            ["All Campaign", "Campaign 1", "Campaign 2", "Campaign 3"],
            index=0,
            key="campaign_filter_perf"
        )
    
    with col3:
        st.selectbox(
            "Keywords",
            ["All Keywords", "Keyword 1", "Keyword 2", "Keyword 3"],
            index=0,
            key="keywords_filter_perf"
        )
    
    with col4:
        st.selectbox(
            "Select Week",
            ["Week of Feb 24 2025", "Week of Feb 17 2025", "Week of Feb 10 2025", "Week of Feb 3 2025"],
            index=0,
            key="week_filter_perf"
        )
    
    st.markdown("</div></div>", unsafe_allow_html=True)


def render_performance_table():
    """Render the performance data table."""
    # Create sample data
    data = {
        'Keywords': ['Pringle', 'Party', 'Picnic', 'Breakfast', 'Crip', 'Buffet', 'Cereal', 'Snacking', 'Lunchbox', 'Cocoa'],
        'Impressions': ['2.0M', '2.0M', '2.0M', '2.0M', '2.0M', '2.0M', '2.0M', '2.0M', '2.0M', '2.0M'],
        '*CPA': ['0.33', '0.33', '0.33', '0.33', '0.33', '0.33', '0.33', '0.33', '0.33', '0.33'],
        'Avg. Rank': ['3.25', '3.25', '3.25', '3.25', '3.25', '3.25', '3.25', '3.25', '3.25', '3.25'],
        'CTR': ['1.15%', '1.15%', '1.15%', '1.15%', '1.15%', '1.15%', '1.15%', '1.15%', '1.15%', '1.15%'],
        'Conversion Rate': ['2.33%', '2.33%', '2.33%', '2.33%', '2.33%', '2.33%', '2.33%', '2.33%', '2.33%', '2.33%'],
        'Click': ['23.0K', '23.0K', '23.0K', '23.0K', '23.0K', '23.0K', '23.0K', '23.0K', '23.0K', '23.0K'],
        'ROAS': ['2.58', '2.58', '2.58', '2.58', '2.58', '2.58', '2.58', '2.58', '2.58', '2.58'],
        '*CPC': ['0.15', '0.15', '0.15', '0.15', '0.15', '0.15', '0.15', '0.15', '0.15', '0.15'],
        'Sales (Con)': ['24.0K', '24.0K', '24.0K', '24.0K', '24.0K', '24.0K', '24.0K', '24.0K', '24.0K', '24.0K'],
        '*Sales (Rev)': ['25.8K', '25.8K', '25.8K', '25.8K', '25.8K', '25.8K', '25.8K', '25.8K', '25.8K', '25.8K'],
        '*Spend': ['10.0K', '10.0K', '10.0K', '10.0K', '10.0K', '10.0K', '10.0K', '10.0K', '10.0K', '10.0K']
    }
    
    df = pd.DataFrame(data)
    
    # Apply custom styling to the table
    st.markdown("""
        <style>
        .stDataFrame {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        .stDataFrame table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .stDataFrame th {
            background-color: #F9FAFB;
            color: #374151;
            font-family: 'Gilroy', sans-serif;
            font-weight: 500;
            font-size: 14px;
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid #E5E7EB;
        }
        
        .stDataFrame td {
            padding: 12px 16px;
            border-bottom: 1px solid #F3F4F6;
            font-family: 'Gilroy', sans-serif;
            font-size: 14px;
            color: #374151;
        }
        
        .stDataFrame tr:hover {
            background-color: #F9FAFB;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Display the table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Keywords": st.column_config.TextColumn("Keywords", width="medium"),
            "Impressions": st.column_config.TextColumn("Impressions", width="small"),
            "*CPA": st.column_config.TextColumn("*CPA", width="small"),
            "Avg. Rank": st.column_config.TextColumn("Avg. Rank", width="small"),
            "CTR": st.column_config.TextColumn("CTR", width="small"),
            "Conversion Rate": st.column_config.TextColumn("Conversion Rate", width="small"),
            "Click": st.column_config.TextColumn("Click", width="small"),
            "ROAS": st.column_config.TextColumn("ROAS", width="small"),
            "*CPC": st.column_config.TextColumn("*CPC", width="small"),
            "Sales (Con)": st.column_config.TextColumn("Sales (Con)", width="small"),
            "*Sales (Rev)": st.column_config.TextColumn("*Sales (Rev)", width="small"),
            "*Spend": st.column_config.TextColumn("*Spend", width="small")
        }
    )


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
