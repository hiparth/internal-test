import React, { useEffect, useState } from "react"
import { Streamlit } from "streamlit-component-lib"
import "./KPITiles.css"

interface KPIItem {
  label: string
  value: string
  is_primary: boolean
}

interface ComponentProps {
  grid_data: KPIItem[]
}

const KPITiles: React.FC = () => {
  const [componentProps, setComponentProps] = useState<ComponentProps | null>(null)

  useEffect(() => {
    Streamlit.setComponentReady()
    // Set exact height to avoid extra margins
    Streamlit.setFrameHeight(160)
    
    Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
    
    return () => {
      Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRender)
    }
  }, [])

  const onRender = (event: any): void => {
    const data = event.detail
    const props = data.args as ComponentProps
    setComponentProps(props)
  }

  if (!componentProps || !componentProps.grid_data) {
    return null
  }

  // Always render as 3x2 grid
  const grid = componentProps.grid_data.slice(0, 6)
  
  return (
    <div className="kpi-tiles-wrapper">
      <table className="kpi-grid">
        <tbody>
          <tr>
            <td>{grid[0]?.label && grid[0]?.value ? <><div className="kpi-label">{grid[0].label}</div><div className="kpi-value">{grid[0].value}</div></> : <span>&nbsp;</span>}</td>
            <td>{grid[1]?.label && grid[1]?.value ? <><div className="kpi-label">{grid[1].label}</div><div className="kpi-value">{grid[1].value}</div></> : <span>&nbsp;</span>}</td>
            <td className="last-col">{grid[2]?.label && grid[2]?.value ? <><div className="kpi-label">{grid[2].label}</div><div className="kpi-value">{grid[2].value}</div></> : <span>&nbsp;</span>}</td>
          </tr>
          <tr className="last-row">
            <td>{grid[3]?.label && grid[3]?.value ? <><div className="kpi-label">{grid[3].label}</div><div className="kpi-value">{grid[3].value}</div></> : <span>&nbsp;</span>}</td>
            <td>{grid[4]?.label && grid[4]?.value ? <><div className="kpi-label">{grid[4].label}</div><div className="kpi-value">{grid[4].value}</div></> : <span>&nbsp;</span>}</td>
            <td className="last-col">{grid[5]?.label && grid[5]?.value ? <><div className="kpi-label">{grid[5].label}</div><div className="kpi-value">{grid[5].value}</div></> : <span>&nbsp;</span>}</td>
          </tr>
        </tbody>
      </table>
    </div>
  )
}

export default KPITiles

