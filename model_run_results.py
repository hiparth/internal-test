"""
Model Run Results Page
----------------------
This module contains the Model Run Results page component.
"""

import streamlit as st
import pandas as pd


def render_model_run_results():
    """
    Render the Model Run Results page content.
    """
    # Header Section
    render_model_run_header()
    
    # Filter Section
    render_model_run_filters()
    
    # Data Table
    render_model_run_table()
    
    # Pagination
    render_model_run_pagination()


def render_model_run_header():
    """Render the model run results header with title and description."""
    st.markdown("""
        <div style="margin-bottom: 32px;">
            <h1 style="font-family: 'Gilroy', sans-serif; font-weight: 700; font-size: 32px; color: #1F2937; margin: 0 0 8px 0;">
                Model Run Results
            </h1>
            <p style="font-family: 'Gilroy', sans-serif; font-weight: 400; font-size: 16px; color: #6B7280; margin: 0;">
                View and download current and previously run model results.
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_model_run_filters():
    """Render the filter dropdowns section."""
    # Create filter dropdowns side by side with much closer spacing
    col1, col2 = st.columns([1, 1], gap="small")
    
    with col1:
        st.selectbox(
            "Retailer",
            ["Tesco", "Sainsbury's", "Asda", "Morrisons"],
            index=0,
            key="retailer_filter_model"
        )
    
    with col2:
        st.selectbox(
            "Date",
            ["2024-09-23", "2024-09-22", "2024-09-21", "2024-09-20"],
            index=0,
            key="date_filter_model"
        )
    
    # Add custom CSS to make selectboxes more compact and much closer
    st.markdown("""
        <style>
        .stSelectbox > div > div {
            max-width: 160px;
        }
        .stColumns {
            gap: 0.5rem !important;
        }
        .stSelectbox {
            margin-bottom: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)


def render_model_run_table():
    """Render the model run results table with clickable buttons."""
    import pandas as pd
    
    # Create sample data with clickable links
    data = {
        '': list(range(1, 11)),  # Row numbers
        'Retailer': ['Tesco'] * 10,
        'Timestamp': ['2024-09-23 14:30:00'] * 10,
        'View Results': ['https://example.com/view#View Results'] * 10,  # Using # for display text
        'Rows Processed': [250] * 10,
        'Status': ['Completed'] * 10,
        'Download': ['https://example.com/download#Download'] * 10  # Using # for display text
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
        
        /* Style button cells with purple background */
        .stDataFrame td:nth-child(4),
        .stDataFrame td:nth-child(7) {
            background-color: #9333EA !important;
            text-align: center !important;
            vertical-align: middle !important;
            padding: 0 !important;
        }
        
        /* Style for clickable links to look like buttons */
        .stDataFrame a {
            background-color: transparent !important;
            color: white !important;
            padding: 12px 16px !important;
            border-radius: 0 !important;
            text-decoration: none !important;
            font-family: 'Gilroy', sans-serif !important;
            font-weight: 600 !important;
            font-size: 13px !important;
            display: block !important;
            text-align: center !important;
            border: none !important;
            cursor: pointer !important;
            width: 100% !important;
            height: 100% !important;
            line-height: 1.2 !important;
            box-sizing: border-box !important;
            transition: background-color 0.2s ease !important;
        }
        
        .stDataFrame a:hover {
            background-color: rgba(126, 34, 206, 0.2) !important;
            color: white !important;
            text-decoration: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Display the table with clickable buttons
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "": st.column_config.TextColumn("", width="small"),
            "Retailer": st.column_config.TextColumn("Retailer", width="medium"),
            "Timestamp": st.column_config.TextColumn("Timestamp", width="large"),
            "View Results": st.column_config.LinkColumn(
                "View Results",
                display_text=r"https://.*?#(.*)$"  # Extract text after #
            ),
            "Rows Processed": st.column_config.TextColumn("Rows Processed", width="medium"),
            "Status": st.column_config.TextColumn("Status", width="medium"),
            "Download": st.column_config.LinkColumn(
                "Download",
                display_text=r"https://.*?#(.*)$"  # Extract text after #
            )
        }
    )


def render_model_run_pagination():
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
