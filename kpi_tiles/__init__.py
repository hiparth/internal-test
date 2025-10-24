"""
KPI Tiles Component
-------------------
React component for rendering KPI grid tiles.
"""

import os
import streamlit.components.v1 as components

# Use production build
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend", "build")

_component_func = components.declare_component("kpi_tiles", path=build_dir)


def kpi_tiles(grid_data, key=None):
    """
    Render KPI tiles component.
    
    Args:
        grid_data (list): List of KPI items [{"label": str, "value": str, "is_primary": bool}, ...]
        key (str): Unique key for the component
    
    Returns:
        None
    """
    if _component_func is None:
        return None
    
    try:
        return _component_func(
            grid_data=grid_data,
            key=key,
            default=None,
            height=160
        )
    except Exception as e:
        print(f"[KPI Tiles] Error: {e}")
        return None

