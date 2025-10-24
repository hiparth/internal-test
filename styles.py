"""
Styles Module
-------------
This module contains all styling functions for the Streamlit app.
It handles custom fonts, themes, and CSS styling.
"""

import streamlit as st
import base64


def load_custom_fonts():
    """
    Load custom Gilroy fonts from the fonts folder.
    
    This function reads all Gilroy font files and embeds them in the app
    using base64 encoding. The fonts are then available throughout the app.
    """
    # Define all font files and their corresponding weights
    font_files = {
        'Gilroy-Light': 'fonts/Gilroy-Light.ttf',
        'Gilroy-Regular': 'fonts/Gilroy-Regular.ttf',
        'Gilroy-Medium': 'fonts/Gilroy-Medium.ttf',
        'Gilroy-Bold': 'fonts/Gilroy-Bold.ttf',
        'Gilroy-Heavy': 'fonts/Gilroy-Heavy.ttf'
    }
    
    # Start building the CSS
    font_css = "<style>"
    
    # Create @font-face rules for each font weight
    for font_name, font_path in font_files.items():
        try:
            # Read the font file and convert to base64
            with open(font_path, 'rb') as f:
                font_data = base64.b64encode(f.read()).decode()
            
            # Map font names to CSS font-weight values
            weight_map = {
                'Gilroy-Light': '300',
                'Gilroy-Regular': '400',
                'Gilroy-Medium': '500',
                'Gilroy-Bold': '700',
                'Gilroy-Heavy': '900'
            }
            
            # Add the @font-face CSS rule
            font_css += f"""
            @font-face {{
                font-family: 'Gilroy';
                src: url(data:font/ttf;base64,{font_data}) format('truetype');
                font-weight: {weight_map[font_name]};
                font-style: normal;
            }}
            """
        except FileNotFoundError:
            st.error(f"Font file not found: {font_path}")
    
    # Apply Gilroy font to all elements in the app
    font_css += """
    html, body, [class*="css"], p, span, div, h1, h2, h3, h4, h5, h6, label, input, button, textarea, select {
        font-family: 'Gilroy', sans-serif !important;
    }
    </style>
    """
    
    # Inject the CSS into the app
    st.markdown(font_css, unsafe_allow_html=True)


def apply_light_theme():
    """
    Apply custom light theme styling to the app.
    
    This ensures the app always uses a light background,
    overriding any system dark mode preferences.
    """
    st.markdown("""
        <style>
        /* Force light theme background */
        .stApp {
            background-color: #FFFFFF;
        }
        </style>
    """, unsafe_allow_html=True)


def apply_custom_styles():
    """
    Apply any additional custom CSS styles to the app.
    
    Add your custom CSS here for specific components or layouts.
    """
    # Hide Streamlit's default sidebar collapse button and text
    st.markdown("""
        <style>
        /* Aggressively hide Streamlit's default sidebar collapse button */
        section[data-testid="stSidebar"] > div > div > button {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            width: 0 !important;
            height: 0 !important;
        }
        
        button[kind="header"] {
            display: none !important;
        }
        
        [data-testid="collapsedControl"] {
            display: none !important;
        }
        
        [data-testid="stSidebarCollapse"] {
            display: none !important;
        }
        
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }
        
        /* Hide by class names */
        .css-1544g2n, .css-163ttbj, .st-emotion-cache-1cypcdb {
            display: none !important;
        }
        
        /* Hide any span containing keyboard */
        section[data-testid="stSidebar"] span {
            content: "" !important;
        }
        
        section[data-testid="stSidebar"] button span:not(.collapse-icon) {
            visibility: hidden !important;
            font-size: 0 !important;
        }
        
        /* Force hide the header area */
        section[data-testid="stSidebar"] > div:first-child > div:first-child {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

