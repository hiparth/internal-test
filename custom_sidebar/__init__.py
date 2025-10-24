"""
Custom Sidebar Component
------------------------
A React-based custom Streamlit component for the sidebar navigation.
"""

import os
import streamlit.components.v1 as components

# Use production build (static files)
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend", "build")

# Debug: print the build path
print(f"[Custom Sidebar] Looking for build files at: {build_dir}")
print(f"[Custom Sidebar] Build directory exists: {os.path.exists(build_dir)}")
if os.path.exists(build_dir):
    print(f"[Custom Sidebar] Files in build dir: {os.listdir(build_dir)}")
    index_html_path = os.path.join(build_dir, "index.html")
    print(f"[Custom Sidebar] index.html exists: {os.path.exists(index_html_path)}")

# Declare component using the built files
try:
    _component_func = components.declare_component(
        "custom_sidebar",
        path=build_dir
    )
    print("[Custom Sidebar] Component declared successfully!")
except Exception as e:
    print(f"[Custom Sidebar] Error declaring component: {e}")
    _component_func = None


def custom_sidebar(logo_base64, nav_items, current_page, key=None):
    """
    Render custom sidebar component.
    
    Args:
        logo_base64 (str): Base64 encoded logo SVG
        nav_items (list): List of navigation items with icons
        current_page (str): Currently selected page
        key (str): Unique key for the component
    
    Returns:
        str: Selected page name (or None if no change)
    """
    if _component_func is None:
        print("[Custom Sidebar] Component function is None, cannot render")
        return None
    
    try:
        component_value = _component_func(
            logo_base64=logo_base64,
            nav_items=nav_items,
            current_page=current_page,
            key=key,
            default=None
        )
        return component_value
    except Exception as e:
        print(f"[Custom Sidebar] Error rendering component: {e}")
        return None
