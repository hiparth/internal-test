import streamlit.components.v1 as components
import os

# Create a _RELEASE constant
_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "performance_table",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("performance_table", path=build_dir)


def performance_table(data, key=None):
    """
    Render a performance data table with delta indicators.
    
    Parameters:
    -----------
    data : list of dict
        Table data where each dict represents a row with columns as keys
    key : str
        Unique key for the component
    """
    component_value = _component_func(data=data, key=key, default=None)
    return component_value

