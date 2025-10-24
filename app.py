"""
Main Streamlit Dashboard Application
=====================================

This is the entry point for the dashboard application.
The code is organized into separate modules for easy maintenance:

- config.py: Configuration settings (data source, app settings)
- styles.py: All styling and CSS functions
- data_connection.py: Database connection logic
- app.py: Main application logic (this file)

HOW TO SWITCH DATA SOURCE:
---------------------------
Open config.py and change the DATA_SOURCE variable to either:
- "databricks" (default)
- "snowflake"
"""

import streamlit as st
from config import APP_CONFIG, DATA_SOURCE
from styles import load_custom_fonts, apply_light_theme, apply_custom_styles
from data_connection import get_data_source_name
from sidebar import render_sidebar
from dashboard import render_dashboard
from performance_data import render_performance_data
from upload_keyword import render_upload_keyword
from model_run_results import render_model_run_results
from help import render_help


def configure_page():
    """
    Configure the Streamlit page settings.
    
    This MUST be the first Streamlit command called.
    It sets up the page title, icon, layout, and sidebar.
    """
    st.set_page_config(
        page_title=APP_CONFIG["page_title"],
        page_icon=APP_CONFIG["page_icon"],
        layout=APP_CONFIG["layout"],
        initial_sidebar_state=APP_CONFIG["initial_sidebar_state"]
    )


def initialize_app_styles():
    """
    Initialize all visual styling for the app.
    
    This loads custom fonts and applies the light theme.
    """
    load_custom_fonts()
    apply_light_theme()
    apply_custom_styles()


def render_sidebar_content():
    """
    Render the sidebar navigation and components.
    """
    with st.sidebar:
        # Render the custom sidebar design
        render_sidebar()


def render_main_content():
    """
    Render the main content area of the dashboard.
    Displays the content for the currently selected page.
    """
    # Get the selected page from session state
    selected_page = st.session_state.get('selected_page', 'Dashboard')
    
    # Render the appropriate page content
    if selected_page == 'Dashboard':
        render_dashboard()
    elif selected_page == 'Performance Data':
        render_performance_data()
    elif selected_page == 'Upload Keyword':
        render_upload_keyword()
    elif selected_page == 'Model Run Results':
        render_model_run_results()
    elif selected_page == 'Help':
        render_help()
    else:
        # Default to Dashboard if unknown page
        render_dashboard()


def main():
    """
    Main application entry point.
    
    This is the function that runs when the app starts.
    It calls all the setup functions in the correct order.
    """
    # Step 1: Configure the page (must be first!)
    configure_page()
    
    # Step 2: Initialize styling
    initialize_app_styles()
    
    # Step 3: Render sidebar
    render_sidebar_content()
    
    # Step 4: Render main content
    render_main_content()


# This runs when the script is executed
if __name__ == "__main__":
    main()
