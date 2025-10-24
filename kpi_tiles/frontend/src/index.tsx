import React from "react"
import ReactDOM from "react-dom/client"
import KPITiles from "./KPITiles"

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
)

root.render(
  <React.StrictMode>
    <KPITiles />
  </React.StrictMode>
)

