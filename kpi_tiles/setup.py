import setuptools

setuptools.setup(
    name="kpi_tiles",
    version="1.0.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["streamlit >= 0.63"],
)

