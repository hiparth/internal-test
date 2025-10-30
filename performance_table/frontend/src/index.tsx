import React from "react"
import { createRoot } from "react-dom/client"
import PerformanceTable from "./PerformanceTable"

const container = document.getElementById("root")
const root = createRoot(container!)

root.render(
  <React.StrictMode>
    <PerformanceTable />
  </React.StrictMode>
)

