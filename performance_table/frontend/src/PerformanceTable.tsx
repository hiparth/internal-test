import React, { useEffect, useState } from "react"
import {
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"
import "./PerformanceTable.css"

interface TableRow {
  [key: string]: any
}

interface ComponentProps {
  args: {
    data: TableRow[]
  }
}

type SortConfig = {
  key: string
  direction: 'asc' | 'desc'
} | null

const PerformanceTable: React.FC<ComponentProps> = (props) => {
  const originalData = props.args.data || []
  const columns = originalData.length > 0 ? Object.keys(originalData[0]) : []
  const [sortConfig, setSortConfig] = useState<SortConfig>(null)
  const [tableData, setTableData] = useState<TableRow[]>(originalData)

  useEffect(() => {
    Streamlit.setFrameHeight()
  })

  useEffect(() => {
    setTableData(originalData)
    setSortConfig(null)
  }, [originalData])

  const handleSort = (columnKey: string) => {
    let direction: 'asc' | 'desc' = 'asc'
    
    if (sortConfig && sortConfig.key === columnKey && sortConfig.direction === 'asc') {
      direction = 'desc'
    }

    const sortedData = [...tableData].sort((a, b) => {
      let aVal = a[columnKey]
      let bVal = b[columnKey]

      // Extract value from object if it has a 'value' property
      if (typeof aVal === 'object' && aVal !== null && 'value' in aVal) {
        aVal = aVal.value
      }
      if (typeof bVal === 'object' && bVal !== null && 'value' in bVal) {
        bVal = bVal.value
      }

      // Convert to comparable values
      const aNum = parseFloat(String(aVal).replace(/[^0-9.-]/g, ''))
      const bNum = parseFloat(String(bVal).replace(/[^0-9.-]/g, ''))

      // If both are numbers, compare numerically
      if (!isNaN(aNum) && !isNaN(bNum)) {
        return direction === 'asc' ? aNum - bNum : bNum - aNum
      }

      // Otherwise compare as strings
      const aStr = String(aVal).toLowerCase()
      const bStr = String(bVal).toLowerCase()
      
      if (aStr < bStr) return direction === 'asc' ? -1 : 1
      if (aStr > bStr) return direction === 'asc' ? 1 : -1
      return 0
    })

    setTableData(sortedData)
    setSortConfig({ key: columnKey, direction })
  }

  const getSortIndicator = (columnKey: string) => {
    if (!sortConfig || sortConfig.key !== columnKey) {
      return <span className="sort-indicator">⇅</span>
    }
    return sortConfig.direction === 'asc' 
      ? <span className="sort-indicator active">↑</span>
      : <span className="sort-indicator active">↓</span>
  }

  const renderCellValue = (value: any, columnKey: string) => {
    // Check if it's a button object
    if (typeof value === 'object' && value !== null && 'type' in value && value.type === 'button') {
      return (
        <button 
          className={`table-button ${value.variant || 'primary'}`}
          onClick={() => value.onClick && value.onClick()}
        >
          {value.label}
        </button>
      )
    }
    
    // Check if the value is an object with 'value' and 'delta' properties
    if (typeof value === 'object' && value !== null && 'value' in value) {
      const deltaPercent = value.deltaPercent || 0
      const isPositive = deltaPercent >= 0
      
      return (
        <div className="cell-content">
          <div className="cell-value">{value.value}</div>
          <div className={`cell-delta ${isPositive ? 'positive' : 'negative'}`}>
            ({isPositive ? '+' : ''}{deltaPercent}%) {isPositive ? '▲' : '▼'}
          </div>
        </div>
      )
    }
    
    // Regular value
    return <div className="cell-value">{value}</div>
  }

  return (
    <div className="performance-table-container">
      <table className="performance-table">
        <thead>
          <tr>
            <th className="row-number-header">#</th>
            {columns.map((col, index) => (
              <th 
                key={index} 
                onClick={() => handleSort(col)}
                className="sortable-header"
              >
                <div className="header-content">
                  <span>{col}</span>
                  {getSortIndicator(col)}
                </div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {tableData.map((row, rowIndex) => (
            <tr key={rowIndex}>
              <td className="row-number">{rowIndex + 1}</td>
              {columns.map((col, colIndex) => (
                <td key={colIndex}>
                  {renderCellValue(row[col], col)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default withStreamlitConnection(PerformanceTable)

