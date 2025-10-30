"""
Upload Keyword Page
-------------------
This module contains the Upload Keyword page component.
"""

import streamlit as st
import streamlit.components.v1 as components


def render_upload_keyword():
    """
    Render the Upload Keyword page content.
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
    st.markdown("""
        <div style="margin-bottom: 24px;">
            <h1 style="font-family: 'Gilroy', sans-serif; font-weight: 700; font-size: 32px; color: #1F2937; margin: 0 0 8px 0;">
                Upload Keyword Data
            </h1>
            <p style="font-family: 'Gilroy', sans-serif; font-weight: 400; font-size: 16px; color: #6B7280; margin: 0;">
                Upload Keyword data via CSV/API integration, provide bid constraints and run bid optimization models.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Retailer Selection Section
    st.markdown("""
        <style>
        /* Limit the width of the retailer selectbox */
        div[data-testid="stSelectbox"][data-baseweb="select"] {
            max-width: 300px !important;
        }
        /* Reduce spacing between sections */
        div[data-testid="stVerticalBlock"] > div {
            margin-bottom: 0px !important;
        }
        </style>
        <div style="margin-bottom: 24px; margin-top: 0px;">
            <label style="font-family: 'Gilroy', sans-serif; font-weight: 500; font-size: 14px; color: #1F2937; display: block; margin-bottom: 8px;">
                Retailer
            </label>
    """, unsafe_allow_html=True)
    
    # Create a column to limit width
    col1, col2 = st.columns([1, 3])
    
    with col1:
        # Retailer dropdown
        retailer = st.selectbox(
            "Select Retailer",
            ["Tesco", "Sainsbury's", "Asda", "Morrisons"],
            index=None,
            key="retailer_select",
            label_visibility="collapsed"
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Show upload section if retailer is selected
    if retailer:
        render_upload_section()
    else:
        # Placeholder Section
        st.markdown("""
            <div style="
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 80px 20px;
                text-align: center;
            ">
                <div style="
                    font-size: 48px;
                    color: #D1D5DB;
                    margin-bottom: 16px;
                    opacity: 0.5;
                ">
                    👆
                </div>
                <p style="
                    font-family: 'Gilroy', sans-serif;
                    font-size: 18px;
                    color: #9CA3AF;
                    margin: 0;
                ">
                    Select Retailer for Results
                </p>
            </div>
        """, unsafe_allow_html=True)


def render_upload_section():
    """Render the CSV upload section."""
    # Add CSS to remove all unnecessary margins
    st.markdown("""
        <style>
        /* Remove all element container margins in upload section */
        .element-container {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
        }
        [data-testid="stFileUploader"] {
            position: absolute;
            opacity: 0;
            width: 0;
            height: 0;
            overflow: hidden;
            margin: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="font-family: 'Gilroy', sans-serif; font-weight: 600; font-size: 18px; color: #1F2937; margin: 0 0 12px 0; padding: 0;">
            Upload keyword data in CSV
        </h2>
    """, unsafe_allow_html=True)
    
    # Hidden but functional file uploader
    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=['csv'],
        key="csv_upload",
        label_visibility="collapsed"
    )
    
    # Show upload bar only if no file is uploaded
    if uploaded_file is None:
        # Single Upload bar
        st.markdown("""
            <div id="uploadBar" style="
                border: 1px solid #E5E7EB;
                border-radius: 8px;
                background-color: white;
                padding: 16px 20px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                margin-bottom: 16px;
            ">
                <div>
                    <p style="
                        font-family: 'Gilroy', sans-serif;
                        font-size: 14px;
                        color: #6B7280;
                        margin: 0;
                    ">
                        Click upload or drag and drop CSV files only
                    </p>
                </div>
                <button id="uploadButton" style="
                    background-color: transparent;
                    color: #9333EA;
                    border: 1px solid #9333EA;
                    border-radius: 6px;
                    padding: 10px 20px;
                    font-family: 'Gilroy', sans-serif;
                    font-weight: 500;
                    font-size: 14px;
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    gap: 8px;
                ">
                    <span>⬆️</span>
                    <span>Upload a file</span>
                </button>
            </div>
        """, unsafe_allow_html=True)
        
        # Use components.html to run JavaScript that connects the button
        components.html("""
            <script>
            (function() {
                function connectButton() {
                    const uploadBtn = window.parent.document.getElementById('uploadButton');
                    const fileInput = window.parent.document.querySelector('input[type="file"]');
                    
                    if (uploadBtn && fileInput) {
                        uploadBtn.onclick = function(e) {
                            e.preventDefault();
                            fileInput.click();
                        };
                        console.log('Upload button connected');
                    } else {
                        setTimeout(connectButton, 100);
                    }
                }
                connectButton();
            })();
            </script>
        """, height=0)
        
        # Requirements
        st.markdown("""
            <ul style="
                font-family: 'Gilroy', sans-serif;
                font-size: 14px;
                color: #1F2937;
                margin: 0;
                padding-left: 20px;
            ">
                <li><strong>Required Columns:</strong> Search Term, Cost, Conversions, Current Bid</li>
                <li><strong>Maximum file size:</strong> 10MB</li>
                <li><strong>Accepted format:</strong> CSV (.csv)</li>
            </ul>
        """, unsafe_allow_html=True)
    
    # Show uploaded file info and configuration form
    else:
        import pandas as pd
        
        # Add CSS to remove default margins from success message
        st.markdown("""
            <style>
            .element-container:has(> .stAlert) {
                margin-top: 0 !important;
                padding-top: 0 !important;
            }
            div.stAlert {
                margin-top: 0 !important;
                margin-bottom: 8px !important;
                padding: 10px 14px !important;
            }
            </style>
        """, unsafe_allow_html=True)
        
        # Success message
        st.success(f"✓ Your Document Uploaded Successfully !")
        
        # Display filename and size
        file_size_kb = uploaded_file.size / 1024
        st.markdown(f"""
            <div style="
                font-family: 'Gilroy', sans-serif;
                font-size: 14px;
                color: #6B7280;
                margin-top: 0;
                margin-bottom: 16px;
            ">
                📄 {uploaded_file.name} &nbsp; {file_size_kb:.0f}kb
            </div>
        """, unsafe_allow_html=True)
        
        # Read CSV
        try:
            df = pd.read_csv(uploaded_file)
            
            # Extract unique keys from 'Search Term' or 'Key' column
            if 'Search Term' in df.columns:
                unique_keys = df['Search Term'].unique().tolist()
            elif 'Key' in df.columns:
                unique_keys = df['Key'].unique().tolist()
            else:
                # Use first column as key
                unique_keys = df.iloc[:, 0].unique().tolist()
            
            # Render configuration form
            render_bid_configuration_form(unique_keys)
            
        except Exception as e:
            st.error(f"Error reading CSV file: {str(e)}")


def render_bid_configuration_form(unique_keys):
    """Render the bid configuration form with unique keys."""
    # Clean CSS implementation for table inputs
    st.markdown("""
        <style>
        /* Clean compact table styling */
        div[data-testid="column"] {
            padding: 2px 4px !important;
            margin: 0 !important;
        }
        
        div[data-testid="stHorizontalBlock"] {
            gap: 8px !important;
            margin-bottom: 4px !important;
        }
        
        .element-container {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Text input styling - compact and centered */
        div[data-testid="stTextInput"] {
            margin: 0 !important;
        }
        
        div[data-testid="stTextInput"] > div {
            margin: 0 !important;
        }
        
        div[data-testid="stTextInput"] input {
            width: 70px !important;
            padding: 6px 8px !important;
            font-size: 13px !important;
            text-align: center !important;
            font-family: 'Gilroy', sans-serif !important;
        }
        
        /* Selectbox styling - compact */
        div[data-testid="stSelectbox"] {
            margin: 0 !important;
        }
        
        div[data-testid="stSelectbox"] > div {
            margin: 0 !important;
        }
        
        div[data-testid="stSelectbox"] select {
            width: 100px !important;
            padding: 6px 8px !important;
            font-size: 13px !important;
            font-family: 'Gilroy', sans-serif !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Section header
    st.markdown("""
        <div style="margin-bottom: 12px; margin-top: 8px;">
            <h2 style="font-family: 'Gilroy', sans-serif; font-weight: 600; font-size: 18px; color: #1F2937; margin: 0 0 4px 0;">
                Configure Campaign Bid Inputs
            </h2>
            <p style="font-family: 'Gilroy', sans-serif; font-size: 12px; color: #6B7280; margin: 0; padding-left: 24px; font-style: italic;">
                *all values are in the local currency
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Table header
    st.markdown("""
        <div style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 16px;
            background-color: #F9FAFB;
            border-bottom: 1px solid #E5E7EB;
            font-family: 'Gilroy', sans-serif;
            font-weight: 600;
            font-size: 13px;
            color: #1F2937;
            margin-bottom: 8px;
        ">
            <div style="flex: 2;">Campaign Name</div>
            <div style="flex: 1; text-align: center;">*Min Bid</div>
            <div style="flex: 1; text-align: center;">*Max Bid</div>
            <div style="flex: 1.5; text-align: center;">Bid Adjustment Volatility</div>
            <div style="flex: 1; text-align: center;">ROAS Target</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Table rows for each unique key
    for idx, key in enumerate(unique_keys[:10]):  # Show first 10 for now
        col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1.5, 1])
        
        with col1:
            st.markdown(f"""
                <div style="
                    font-family: 'Gilroy', sans-serif;
                    font-size: 13px;
                    color: #1F2937;
                    padding: 4px 0;
                    margin: 0;
                    line-height: 1.2;
                ">
                    {key}
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.text_input(
                "Min Bid",
                value="0.30",
                key=f"min_bid_{idx}",
                label_visibility="collapsed"
            )
        
        with col3:
            st.text_input(
                "Max Bid",
                value="0.50",
                key=f"max_bid_{idx}",
                label_visibility="collapsed"
            )
        
        with col4:
            st.selectbox(
                "Volatility",
                ["5%", "10%", "15%", "20%"],
                index=0,
                key=f"volatility_{idx}",
                label_visibility="collapsed"
            )
        
        with col5:
            st.text_input(
                "ROAS Target",
                value="2.50",
                key=f"roas_{idx}",
                label_visibility="collapsed"
            )
    
    # Save button - purple and right-aligned
    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([3, 1.5, 1])
    
    with col3:
        st.markdown("""
            <style>
            /* Style the Save button to be purple and compact */
            .stButton > button {
                background-color: #8400FF !important;
                color: white !important;
                border: none !important;
                border-radius: 6px !important;
                padding: 8px 16px !important;
                font-family: 'Gilroy', sans-serif !important;
                font-weight: 500 !important;
                font-size: 13px !important;
                width: auto !important;
                white-space: nowrap !important;
            }
            .stButton > button:hover {
                background-color: #6B00CC !important;
            }
            </style>
        """, unsafe_allow_html=True)
        
        if st.button("💾 Save Data & Run Model"):
            st.success("Data saved and model started!")
