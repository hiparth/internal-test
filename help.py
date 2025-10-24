"""
Help Page
---------
This module contains the Help page component.
"""

import streamlit as st
from data_connection import test_connection, list_tables, get_sample_data, run_query
from config import DATA_SOURCE, DATABRICKS_CONFIG


def render_help():
    """
    Render the Help page content with database testing tools.
    """
    st.markdown("""
        <div style="margin-bottom: 32px;">
            <h1 style="font-family: 'Gilroy', sans-serif; font-weight: 700; font-size: 32px; color: #1F2937; margin: 0 0 8px 0;">
                Help & Database Testing
            </h1>
            <p style="font-family: 'Gilroy', sans-serif; font-weight: 400; font-size: 16px; color: #6B7280; margin: 0;">
                Test your database connection and explore available data.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Connection Status Section
    st.subheader("📊 Database Connection Status")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div style="background-color: #F9FAFB; padding: 16px; border-radius: 8px; margin-bottom: 16px;">
                <p style="font-family: 'Gilroy', sans-serif; font-size: 14px; color: #6B7280; margin: 0 0 8px 0;">
                    <strong>Data Source:</strong> {DATA_SOURCE.upper()}
                </p>
                <p style="font-family: 'Gilroy', sans-serif; font-size: 14px; color: #6B7280; margin: 0 0 8px 0;">
                    <strong>Host:</strong> {DATABRICKS_CONFIG.get('host', 'Not configured')}
                </p>
                <p style="font-family: 'Gilroy', sans-serif; font-size: 14px; color: #6B7280; margin: 0;">
                    <strong>HTTP Path:</strong> {DATABRICKS_CONFIG.get('http_path', 'Not configured')}
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button("🔌 Test Connection", type="primary", use_container_width=True):
            with st.spinner("Testing connection..."):
                if test_connection():
                    st.success("✅ Connection successful!")
                else:
                    st.error("❌ Connection failed. Check configuration.")
    
    st.markdown("---")
    
    # List Tables Section
    st.subheader("📋 Available Tables")
    
    if st.button("📊 List All Tables", use_container_width=False):
        with st.spinner("Fetching tables..."):
            tables_df = list_tables()
            if not tables_df.empty:
                st.dataframe(tables_df, use_container_width=True)
            else:
                st.warning("No tables found or connection failed.")
    
    st.markdown("---")
    
    # Query Testing Section
    st.subheader("🔍 Test Custom Query")
    
    # Table name input
    table_name = st.text_input(
        "Enter table name:",
        placeholder="e.g., performance_data",
        help="Enter the table name to query. If using Databricks with catalog/schema, just enter the table name."
    )
    
    # Buttons for different actions
    col1, col2 = st.columns(2)
    
    with col1:
        fetch_keys = st.button("🔑 Fetch Column Names Only", type="secondary", use_container_width=True)
    
    with col2:
        fetch_data = st.button("📥 Fetch Sample Data (10 rows)", type="primary", use_container_width=True)
    
    # Fetch column names only
    if fetch_keys:
        if table_name:
            with st.spinner(f"Fetching column names from {table_name}..."):
                sample_df = get_sample_data(table_name, limit=1)  # Fetch only 1 row to get columns
                if not sample_df.empty:
                    columns = sample_df.columns.tolist()
                    st.success(f"✅ Found {len(columns)} columns")
                    
                    # Display columns as a list
                    st.write("**Column Names:**")
                    for i, col in enumerate(columns, 1):
                        st.write(f"{i}. `{col}`")
                    
                    # Print to terminal for easy copying
                    print("\n" + "="*80)
                    print(f"TABLE: {table_name}")
                    print("="*80)
                    print(f"\nTotal Columns: {len(columns)}\n")
                    print("COLUMN NAMES:")
                    print("-" * 80)
                    for i, col in enumerate(columns, 1):
                        print(f"{i:3}. {col}")
                    print("\n" + "="*80)
                    print("\nPython List Format:")
                    print(columns)
                    print("\n" + "="*80 + "\n")
                else:
                    st.error("❌ Failed to fetch columns. Check table name and connection.")
        else:
            st.warning("⚠️ Please enter a table name.")
    
    # Fetch sample data
    if fetch_data:
        if table_name:
            with st.spinner(f"Fetching 10 rows from {table_name}..."):
                sample_df = get_sample_data(table_name, limit=10)
                if not sample_df.empty:
                    st.success(f"✅ Fetched {len(sample_df)} rows")
                    st.dataframe(sample_df, use_container_width=True)
                    
                    # Print to terminal for reference
                    print("\n" + "="*80)
                    print(f"TABLE: {table_name}")
                    print("="*80)
                    print(f"\nDataFrame Shape: {sample_df.shape}")
                    print(f"Columns: {sample_df.columns.tolist()}\n")
                    print(sample_df.to_string())
                    print("\n" + "="*80 + "\n")
                    
                    # Show column info
                    st.subheader("Column Information:")
                    col_info = {
                        "Column Name": sample_df.columns.tolist(),
                        "Data Type": [str(dtype) for dtype in sample_df.dtypes.tolist()],
                        "Non-Null Count": [sample_df[col].count() for col in sample_df.columns]
                    }
                    st.dataframe(col_info, use_container_width=True)
                    
                    # Print column info to terminal
                    print("COLUMN INFORMATION:")
                    print("-" * 80)
                    for col, dtype, count in zip(col_info["Column Name"], col_info["Data Type"], col_info["Non-Null Count"]):
                        print(f"{col:30} | {dtype:20} | Non-Null: {count}")
                    print("\n")
                else:
                    st.error("❌ Failed to fetch data. Check table name and connection.")
        else:
            st.warning("⚠️ Please enter a table name.")
    
    st.markdown("---")
    
    # Custom Query Section
    st.subheader("💻 Execute Custom SQL Query")
    
    custom_query = st.text_area(
        "Enter your SQL query:",
        placeholder="SELECT * FROM your_table WHERE condition LIMIT 100",
        height=150
    )
    
    if st.button("▶️ Execute Query", type="primary"):
        if custom_query:
            with st.spinner("Executing query..."):
                result_df = run_query(custom_query)
                if not result_df.empty:
                    st.success(f"✅ Query returned {len(result_df)} rows")
                    st.dataframe(result_df, use_container_width=True)
                    
                    # Print to terminal for reference
                    print("\n" + "="*80)
                    print("CUSTOM QUERY RESULTS")
                    print("="*80)
                    print(f"\nQuery:\n{custom_query}\n")
                    print(f"Result Shape: {result_df.shape}")
                    print(f"Columns: {result_df.columns.tolist()}\n")
                    print(result_df.to_string())
                    print("\n" + "="*80 + "\n")
                else:
                    st.error("❌ Query failed or returned no results.")
                    print(f"\n❌ Query failed: {custom_query}\n")
        else:
            st.warning("⚠️ Please enter a SQL query.")
