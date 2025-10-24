"""
Sidebar Module - Custom React Component
----------------------------------------
Using custom React/TypeScript component for exact Figma design match.
"""

import streamlit as st
import base64
from custom_sidebar import custom_sidebar


def get_base64_encoded_image(image_path):
    """Convert image file to base64 string for embedding in HTML."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
        return ""


def render_sidebar():
    """Main function to render the complete sidebar using custom React component."""
    # Initialize session state
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Dashboard'
    
    # Get base64 encoded images
    logo_base64 = get_base64_encoded_image("assets/icons/logo 1.svg")
    home_icon_base64 = get_base64_encoded_image("assets/icons/Home.png")
    pie_chart_icon_base64 = get_base64_encoded_image("assets/icons/Pie Chart.png")
    upload_icon_base64 = get_base64_encoded_image("assets/icons/Upload Square.png")
    notebook_icon_base64 = get_base64_encoded_image("assets/icons/Notebook.png")
    dialog_icon_base64 = get_base64_encoded_image("assets/icons/Dialog.png")
    
    # Define navigation items
    nav_items = [
        {"name": "Dashboard", "icon": home_icon_base64, "icon_type": "png"},
        {"name": "Performance Data", "icon": pie_chart_icon_base64, "icon_type": "png"},
        {"name": "Upload Keyword", "icon": upload_icon_base64, "icon_type": "png"},
        {"name": "Model Run Results", "icon": notebook_icon_base64, "icon_type": "png"},
        {"name": "Help", "icon": dialog_icon_base64, "icon_type": "png"}
    ]
    
    # Render custom React component
    clicked_page = custom_sidebar(
        logo_base64=logo_base64,
        nav_items=nav_items,
        current_page=st.session_state.selected_page,
        key="sidebar_navigation"
    )
    
    # Debug: print what was received
    if clicked_page:
        print(f"[Sidebar Python] Received clicked_page: {clicked_page}")
        print(f"[Sidebar Python] Current page: {st.session_state.selected_page}")
    
    # Handle page navigation
    if clicked_page and clicked_page != st.session_state.selected_page:
        print(f"[Sidebar Python] Changing page from {st.session_state.selected_page} to {clicked_page}")
        st.session_state.selected_page = clicked_page
        st.rerun()
