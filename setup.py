"""
Setup configuration for deploying the Streamlit app to Databricks
"""
from setuptools import setup, find_packages

setup(
    name="retail-media-dashboard",
    version="1.0.0",
    description="Retail Media Analytics Dashboard - Performance tracking and bid optimization",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.28.0",
        "plotly>=5.17.0",
        "pandas>=2.0.0",
        "databricks-sql-connector>=2.9.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "streamlit_app=streamlit.web.cli:main",
        ],
    },
    package_data={
        "": [
            "*.py",
            "fonts/*.ttf",
            "assets/**/*",
            "custom_sidebar/frontend/build/**/*",
            "kpi_tiles/frontend/build/**/*",
            "performance_table/frontend/build/**/*",
        ],
    },
)

