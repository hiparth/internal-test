"""
Dashboard Page - Performance Dashboard
------------------------------------
This module contains the Performance Dashboard page component.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import streamlit_shadcn_ui as ui


def render_dashboard():
    """
    Render the Performance Dashboard page content.
    """
    # Header Section
    render_dashboard_header()
    
    # Filter Section
    render_filter_section()
    
    # Main Content Area
    render_main_content()


def render_dashboard_header():
    """Render the dashboard header with title, description, and export button."""
    # Create columns for title/description and export button
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
            <div style="margin-bottom: 24px;">
                <h1 style="font-family: 'Gilroy', sans-serif; font-weight: 700; font-size: 32px; color: #1F2937; margin: 0 0 8px 0;">
                    Performance Dashboard
                </h1>
                <p style="font-family: 'Gilroy', sans-serif; font-weight: 400; font-size: 16px; color: #6B7280; margin: 0;">
                    Monitor campaigns, review bids, and optimize performance all in one place.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Export Report Button
        st.markdown("""
            <div style="display: flex; justify-content: flex-end; align-items: flex-start; margin-top: 8px;">
                <button style="
                    background-color: #F9FAFB;
                    border: 1px solid #E5E7EB;
                    border-radius: 8px;
                    padding: 10px 16px;
                    font-family: 'Gilroy', sans-serif;
                    font-weight: 500;
                    font-size: 14px;
                    color: #9333EA;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    gap: 8px;
                ">
                    <span>📥</span>
                    <span>Export Report</span>
                </button>
            </div>
        """, unsafe_allow_html=True)


def render_filter_section():
    """Render the filter dropdowns section."""
    st.markdown("""
        <div style="margin-bottom: 32px;">
    """, unsafe_allow_html=True)
    
    # Create filter dropdowns that span 2/3 width (same as chart column)
    # Using ratio 2:1 to match the chart:KPI cards layout
    col_filters, col_spacer = st.columns([2, 1])
    
    with col_filters:
        # 4 equal filters within the 2/3 width
        filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)
        
        with filter_col1:
            st.selectbox(
                "Retailer",
                ["Tesco", "Sainsbury's", "Asda", "Morrisons"],
                index=0,
                key="retailer_filter"
            )
        
        with filter_col2:
            st.selectbox(
                "Campaign",
                ["All Campaign", "Campaign 1", "Campaign 2", "Campaign 3"],
                index=0,
                key="campaign_filter"
            )
        
        with filter_col3:
            st.selectbox(
                "Keywords",
                ["All Keywords", "Keyword 1", "Keyword 2", "Keyword 3"],
                index=0,
                key="keywords_filter"
            )
        
        with filter_col4:
            st.selectbox(
                "Select Week",
                ["Week of Feb 24 2025", "Week of Feb 17 2025", "Week of Feb 10 2025", "Week of Feb 3 2025"],
                index=0,
                key="week_filter"
            )
    
    st.markdown("</div>", unsafe_allow_html=True)


def render_main_content():
    """Render the main content area with chart and KPI cards."""
    # Create main layout with chart on left and KPI cards on right (2:1 ratio for narrower graph)
    col1, col2 = st.columns([2, 1], gap="medium")
    
    with col1:
        render_performance_chart()
    
    with col2:
        render_kpi_cards()


def render_performance_chart():
    """Render the performance chart with dual-axis line chart."""
    # Add CSS to style the column's inner div
    st.markdown("""
        <style>
        /* Style the first column in the main content row */
        main div[data-testid="column"]:first-of-type > div {
            background-color: white !important;
            border-radius: 12px !important;
            padding: 20px !important;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
            margin-bottom: 16px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Use st.container to group everything
    with st.container():
        
        # KPI Selectors
        col1, col2 = st.columns(2)
        
        with col1:
            st.selectbox(
                "Primary KPI",
                ["Impressions", "Clicks", "CTR", "Conversion Rate"],
                index=0,
                key="primary_kpi"
            )
        
        with col2:
            st.selectbox(
                "Secondary KPI",
                ["ROAS", "CPA", "CPC", "Spend"],
                index=0,
                key="secondary_kpi"
            )
        
        # Create sample data for the chart
        weeks = ["Wo Feb 3 2025", "Wo Feb 10 2025", "Wo Feb 17 2025", "Wo Feb 24 2025"]
        impressions = [45, 55, 40, 50]
        roas = [2.2, 2.8, 2.0, 2.6]
        
        # Create dual-axis line chart
        fig = go.Figure()
        
        # Add Impressions line (left axis)
        fig.add_trace(go.Scatter(
            x=weeks,
            y=impressions,
            mode='lines+markers',
            name='Impressions',
            line=dict(color='#9333EA', width=3),
            fill='tonexty',
            fillcolor='rgba(147, 51, 234, 0.1)'
        ))
        
        # Add ROAS line (right axis)
        fig.add_trace(go.Scatter(
            x=weeks,
            y=roas,
            mode='lines+markers',
            name='ROAS',
            line=dict(color='#7C3AED', width=3),
            fill='tonexty',
            fillcolor='rgba(124, 58, 237, 0.1)',
            yaxis='y2'
        ))
        
        # Update layout for dual-axis
        fig.update_layout(
            title=None,
            xaxis=dict(
                title=None,
                showgrid=True,
                gridcolor='#F3F4F6',
                tickfont=dict(family='Gilroy', size=12, color='#6B7280')
            ),
            yaxis=dict(
                title="Impressions",
                side="left",
                showgrid=True,
                gridcolor='#F3F4F6',
                tickfont=dict(family='Gilroy', size=12, color='#6B7280'),
                titlefont=dict(family='Gilroy', size=12, color='#6B7280')
            ),
            yaxis2=dict(
                title="ROAS",
                side="right",
                overlaying="y",
                showgrid=False,
                tickfont=dict(family='Gilroy', size=12, color='#6B7280'),
                titlefont=dict(family='Gilroy', size=12, color='#6B7280')
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                font=dict(family='Gilroy', size=12)
            ),
            plot_bgcolor='white',
            paper_bgcolor='white',
            height=300,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)


def render_kpi_cards():
    """Render the KPI cards using React component."""
    from kpi_tiles import kpi_tiles
    
    # Add CSS to remove Streamlit margins around components
    st.markdown("""
        <style>
        iframe[title="kpi_tiles.kpi_tiles"] {
            margin: 0 !important;
            padding: 0 !important;
        }
        div:has(> iframe[title="kpi_tiles.kpi_tiles"]) {
            margin: 0 !important;
            padding: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Grid 1 data
    grid1_data = [
        {"label": "Impressions", "value": "2.0M", "is_primary": True},
        {"label": "*CPA", "value": "0.33", "is_primary": False},
        {"label": "ROAS", "value": "2.58", "is_primary": False},
        {"label": "CTR", "value": "1.15%", "is_primary": False},
        {"label": "Conversion Rate", "value": "2.33%", "is_primary": False},
        {"label": "", "value": "", "is_primary": False}
    ]
    
    kpi_tiles(grid_data=grid1_data, key="kpi_grid_1")
    
    # Small gap
    st.markdown('<div style="height: 8px;"></div>', unsafe_allow_html=True)
    
    # Grid 2 data
    grid2_data = [
        {"label": "Clicks", "value": "23.0K", "is_primary": True},
        {"label": "Avg. Rank", "value": "3.25", "is_primary": False},
        {"label": "*CPC", "value": "0.15", "is_primary": False},
        {"label": "*Spend", "value": "10.0K", "is_primary": False},
        {"label": "*Sales (Con)", "value": "24.0K", "is_primary": False},
        {"label": "*Sales (Rev)", "value": "25.8K", "is_primary": False}
    ]
    
    kpi_tiles(grid_data=grid2_data, key="kpi_grid_2")
    
    # Footer note
    st.markdown("""
        <div style="margin-top: 4px;">
            <p style="font-family: 'Gilroy', sans-serif; font-size: 12px; color: #9CA3AF; margin: 0;">
                *all values are in the local currency
            </p>
        </div>
    """, unsafe_allow_html=True)


def render_kpi_grid_html(data, grid_id):
    """Render a 3x2 KPI grid using pure HTML table."""
    st.markdown(f"""
        <style>
        .kpi-grid-{grid_id} {{
            width: 100%;
            max-width: 350px;
            margin: 0 auto;
            border-collapse: separate;
            border-spacing: 0;
            border: 5px solid #E5E7EB;
            border-radius: 8px;
            overflow: hidden;
            background-color: white;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }}
        
        .kpi-grid-{grid_id} td {{
            padding: 14px 10px;
            min-height: 70px;
            border-right: 2px solid #E5E7EB;
            border-bottom: 2px solid #E5E7EB;
            vertical-align: top;
        }}
        
        .kpi-grid-{grid_id} td:last-child {{
            border-right: none;
        }}
        
        .kpi-grid-{grid_id} tr:last-child td {{
            border-bottom: none;
        }}
        
        .kpi-grid-{grid_id} .kpi-label {{
            font-family: 'Gilroy', 'Poppins', sans-serif;
            font-size: 12px;
            color: #3B82F6;
            margin-bottom: 6px;
        }}
        
        .kpi-grid-{grid_id} .kpi-value {{
            font-family: 'Gilroy', 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 18px;
            color: #1F2937;
        }}
        </style>
        
        <table class="kpi-grid-{grid_id}">
            <tr>
                <td>
                    {f'<div class="kpi-label">{data[0][0]}</div><div class="kpi-value">{data[0][1]}</div>' if data[0][0] else ''}
                </td>
                <td>
                    {f'<div class="kpi-label">{data[1][0]}</div><div class="kpi-value">{data[1][1]}</div>' if data[1][0] else ''}
                </td>
                <td>
                    {f'<div class="kpi-label">{data[2][0]}</div><div class="kpi-value">{data[2][1]}</div>' if data[2][0] else ''}
                </td>
            </tr>
            <tr>
                <td>
                    {f'<div class="kpi-label">{data[3][0]}</div><div class="kpi-value">{data[3][1]}</div>' if data[3][0] else '&nbsp;'}
                </td>
                <td>
                    {f'<div class="kpi-label">{data[4][0]}</div><div class="kpi-value">{data[4][1]}</div>' if data[4][0] else '&nbsp;'}
                </td>
                <td>
                    {f'<div class="kpi-label">{data[5][0]}</div><div class="kpi-value">{data[5][1]}</div>' if data[5][0] else '&nbsp;'}
                </td>
            </tr>
        </table>
    """, unsafe_allow_html=True)


def render_kpi_grid_3x2(kpi_data, grid_id):
    """Render a 3x2 grid (3 columns, 2 rows) using Streamlit columns."""
    # Outer container with visible borders
    st.markdown(f"""
        <div style="
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            margin-bottom: 16px;
            max-width: 300px;
            margin-left: auto;
            margin-right: auto;
            border: 2px solid #E5E7EB;
            padding: 2px;
        ">
            <div style="
                background-color: white;
                border-radius: 6px;
                overflow: hidden;
            ">
    """, unsafe_allow_html=True)
    
    # Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        render_kpi_cell(kpi_data[0][0], kpi_data[0][1], kpi_data[0][2], True, True)
    with col2:
        render_kpi_cell(kpi_data[1][0], kpi_data[1][1], kpi_data[1][2], True, True)
    with col3:
        render_kpi_cell(kpi_data[2][0], kpi_data[2][1], kpi_data[2][2], False, True)
    
    # Row 2 (last row - no bottom borders)
    col1, col2, col3 = st.columns(3)
    with col1:
        render_kpi_cell(kpi_data[3][0], kpi_data[3][1], kpi_data[3][2], True, False)
    with col2:
        render_kpi_cell(kpi_data[4][0], kpi_data[4][1], kpi_data[4][2], True, False)
    with col3:
        render_kpi_cell(kpi_data[5][0], kpi_data[5][1], kpi_data[5][2], False, False)
    
    st.markdown("</div></div>", unsafe_allow_html=True)




def render_kpi_cell(label, value, is_primary, has_right_border, has_bottom_border):
    """Render a single KPI cell with proper borders."""
    label_color = "#3B82F6" if is_primary else "#6B7280"
    
    border_right = "1px solid #E5E7EB" if has_right_border else ""
    border_bottom = "1px solid #E5E7EB" if has_bottom_border else ""
    
    # Render empty cell with borders
    if not label and not value:
        st.markdown(f"""
            <div style="
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                padding: 14px 10px;
                border-right: {border_right};
                border-bottom: {border_bottom};
                min-height: 70px;
                box-sizing: border-box;
                background-color: white;
            ">
            </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown(f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            padding: 14px 10px;
            border-right: {border_right};
            border-bottom: {border_bottom};
            min-height: 70px;
            box-sizing: border-box;
        ">
            <div style="
                font-family: 'Gilroy', sans-serif;
                font-size: 12px;
                color: {label_color} !important;
                margin-bottom: 6px;
                line-height: 1.2;
            ">{label}</div>
            <div style="
                font-family: 'Gilroy', sans-serif;
                font-weight: 700;
                font-size: 18px;
                color: #1F2937 !important;
                line-height: 1.2;
            ">{value}</div>
        </div>
    """, unsafe_allow_html=True)
