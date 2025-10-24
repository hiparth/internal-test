import React, { useEffect, useState } from "react"
import { Streamlit } from "streamlit-component-lib"
import "./CustomSidebar.css"

interface NavItem {
  name: string
  icon: string
  icon_type: string
}

interface ComponentProps {
  logo_base64: string
  nav_items: NavItem[]
  current_page: string
}

const CustomSidebar: React.FC = () => {
  const [componentProps, setComponentProps] = useState<ComponentProps | null>(null)
  const [activePage, setActivePage] = useState<string>("Dashboard")

  useEffect(() => {
    // Set up Streamlit event listeners
    Streamlit.setComponentReady()
    Streamlit.setFrameHeight(600)
    
    // Register event handler for data from Python
    Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
    
    return () => {
      Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRender)
    }
  }, [])

  const onRender = (event: any): void => {
    const data = event.detail
    const props = data.args as ComponentProps
    setComponentProps(props)
    if (props.current_page) {
      setActivePage(props.current_page)
    }
  }

  const handleNavClick = (pageName: string) => {
    console.log(`[CustomSidebar] Clicked on: ${pageName}`)
    setActivePage(pageName)
    Streamlit.setComponentValue(pageName)
    console.log(`[CustomSidebar] Sent value to Streamlit: ${pageName}`)
  }

  if (!componentProps) {
    return <div>Loading...</div>
  }

  return (
    <div className="sidebar-container">
      {/* Logo and Collapse Icon */}
      <div className="logo-container">
        <img 
          src={`data:image/svg+xml;base64,${componentProps.logo_base64}`} 
          className="logo" 
          alt="Logo" 
        />
        <span className="collapse-icon">&lt;</span>
      </div>

      {/* Section Header - Temporarily Hidden */}
      {/* <div className="section-header">General</div> */}

      {/* Navigation Items */}
      {componentProps.nav_items.map((item) => (
        <button
          key={item.name}
          className={`nav-button ${activePage === item.name ? 'active' : ''}`}
          onClick={() => {
            console.log(`[CustomSidebar] Button clicked: ${item.name}`)
            handleNavClick(item.name)
          }}
          type="button"
        >
          <img 
            src={`data:image/${item.icon_type};base64,${item.icon}`}
            className="nav-icon"
            alt=""
          />
          <span>{item.name}</span>
        </button>
      ))}
    </div>
  )
}

export default CustomSidebar
