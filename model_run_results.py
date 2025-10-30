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
        <div style="margin-bottom: 24px;">
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
    st.markdown("""
        <style>
        /* Reduce width of filter dropdowns */
        .stSelectbox {
            max-width: 200px !important;
        }
        /* Reduce spacing between sections */
        div[data-testid="stVerticalBlock"] > div {
            margin-bottom: 0px !important;
        }
        </style>
        <div style="margin-bottom: 24px; margin-top: 0px;">
    """, unsafe_allow_html=True)
    
    # Create filter dropdowns close together
    col1, col2, col3 = st.columns([1, 1, 6])
    
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
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_model_run_table():
    """Render the model run results table using custom component."""
    from performance_table import performance_table
    
    # Create sample data with button objects
    table_data = [
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        },
        {
            "Retailer": "Tesco",
            "Timestamp": "2024-09-23 14:30:00",
            "View Results": {"type": "button", "label": "View Results", "variant": "primary"},
            "Rows Processed": "250",
            "Status": "Completed",
            "Download": {"type": "button", "label": "Download", "variant": "secondary"}
        }
    ]
    
    # Render the custom performance table component with buttons
    performance_table(data=table_data, key="model_run_results_table")


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
