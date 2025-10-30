from setuptools import setup, find_packages

setup(
    name="performance_table",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    description="Custom Streamlit component for performance data table with delta indicators",
    install_requires=["streamlit>=0.63"],
)

