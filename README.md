# Retail Media Analytics Dashboard

A comprehensive Streamlit-based analytics dashboard for retail media campaign management, featuring bid optimization, performance tracking, and keyword data management.

## 🎯 Features

- **Performance Dashboard**: Real-time KPI tracking with interactive charts
- **Upload Keyword Data**: CSV-based keyword upload and bid configuration
- **Model Run Results**: View optimization results and recommendations
- **Custom Sidebar**: Beautiful navigation with icons and active state indicators
- **Responsive Design**: Modern UI with custom Gilroy fonts

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your PC:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **Node.js 14.x or higher** ([Download Node.js](https://nodejs.org/)) - Required for building custom React components
- **npm** (comes with Node.js)
- **Git** (optional, for cloning the repository)

### Check if you have Python and Node.js installed:

```bash
# Check Python version
python --version

# Check Node.js version
node --version

# Check npm version
npm --version
```

## 🚀 Installation & Setup

### Step 1: Get the Project Files

**Option A: Clone with Git**
```bash
git clone <repository-url>
cd try2
```

**Option B: Download ZIP**
1. Download the project as a ZIP file
2. Extract it to a folder (e.g., `C:\Users\YourName\try2`)
3. Open Command Prompt or PowerShell and navigate to that folder:
   ```bash
   cd C:\Users\YourName\try2
   ```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

If you encounter permission errors on Windows, try:
```bash
pip install --user -r requirements.txt
```

### Step 3: Configure Secrets (IMPORTANT!)

This application requires database credentials. **Never commit secrets to Git!**

Choose one of these methods to configure your credentials:

#### Option A: Using Environment Variables (Recommended)

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your actual credentials:
   ```bash
   DATABRICKS_HOST=your-workspace.cloud.databricks.com
   DATABRICKS_TOKEN=your-actual-token
   DATABRICKS_HTTP_PATH=/sql/1.0/warehouses/your-warehouse-id
   ```

3. The application will automatically load these variables.

#### Option B: Using Streamlit Secrets

1. Create a `.streamlit` directory if it doesn't exist:
   ```bash
   mkdir .streamlit
   ```

2. Copy the example secrets file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

3. Edit `.streamlit/secrets.toml` and add your actual credentials:
   ```toml
   [databricks]
   host = "your-workspace.cloud.databricks.com"
   token = "your-actual-token"
   http_path = "/sql/1.0/warehouses/your-warehouse-id"
   ```

**Note:** Both `.env` and `.streamlit/secrets.toml` are already included in `.gitignore` to prevent accidental commits.

### Step 4: Build Custom React Components

The dashboard uses custom React components for the sidebar and KPI tiles. You need to build them first.

#### Build Custom Sidebar:
```bash
cd custom_sidebar/frontend
npm install
npm run build
cd ../..
```

#### Build KPI Tiles Component:
```bash
cd kpi_tiles/frontend
npm install
npm run build
cd ../..
```

### Step 5: Install Python Components

After building the React components, install them as Python packages:

```bash
# Install custom sidebar
pip install -e custom_sidebar/

# Install KPI tiles
pip install -e kpi_tiles/
```

### Step 6: Run the Application

**Before running, make sure you've configured your secrets (Step 3 above)!**

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 📁 Project Structure

```
try2/
├── app.py                      # Main application entry point
├── config.py                   # Configuration settings
├── styles.py                   # Custom styling and fonts
├── dashboard.py                # Performance Dashboard page
├── upload_keyword.py           # Upload Keyword Data page
├── model_run_results.py        # Model Run Results page
├── help.py                     # Help & Support page
├── sidebar.py                  # Sidebar navigation
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── fonts/                      # Custom Gilroy font files
│   ├── Gilroy-Light.ttf
│   ├── Gilroy-Regular.ttf
│   ├── Gilroy-Medium.ttf
│   ├── Gilroy-Bold.ttf
│   └── Gilroy-Heavy.ttf
│
├── assets/                     # Icons and images
│   └── icons/
│       ├── Home.png
│       ├── Upload Square.png
│       ├── Notebook.png
│       ├── Dialog.png
│       └── logo 1.svg
│
├── custom_sidebar/             # Custom React sidebar component
│   ├── __init__.py
│   ├── setup.py
│   ├── MANIFEST.in
│   └── frontend/
│       ├── package.json
│       ├── tsconfig.json
│       ├── public/
│       └── src/
│           ├── index.tsx
│           ├── CustomSidebar.tsx
│           └── CustomSidebar.css
│
└── kpi_tiles/                  # Custom React KPI tiles component
    ├── __init__.py
    ├── setup.py
    ├── MANIFEST.in
    └── frontend/
        ├── package.json
        ├── tsconfig.json
        ├── public/
        └── src/
            ├── index.tsx
            ├── KPITiles.tsx
            └── KPITiles.css
```

## 🎨 Usage Guide

### Performance Dashboard
- View key performance indicators (KPIs)
- Filter by date range, retailer, and category
- Analyze trends with interactive dual-axis charts
- Switch between primary and secondary KPIs

### Upload Keyword Data
1. Select a retailer from the dropdown
2. Click "Upload a file" to select your CSV
3. Required CSV columns: `Search Term`, `Cost`, `Conversions`, `Current Bid`
4. Configure bid parameters for each keyword
5. Click "Save Data & Run Model"

### Model Run Results
- View optimization recommendations
- Track model performance metrics
- Export results for further analysis

## 🛠️ Troubleshooting

### Common Issues

**Issue: `ModuleNotFoundError: No module named 'streamlit'`**
- Solution: Make sure you installed requirements: `pip install -r requirements.txt`

**Issue: `ModuleNotFoundError: No module named 'custom_sidebar'`**
- Solution: Build and install the custom components (see Step 3 & 4)

**Issue: React build fails with `npm: command not found`**
- Solution: Install Node.js from https://nodejs.org/

**Issue: Port 8501 is already in use**
- Solution: Either:
  - Close other Streamlit apps
  - Or run on a different port: `streamlit run app.py --server.port 8502`

**Issue: Fonts not loading**
- Solution: Make sure the `fonts/` folder contains all Gilroy font files

**Issue: Custom components not showing**
- Solution: 
  1. Delete `custom_sidebar/frontend/build` and `kpi_tiles/frontend/build` folders
  2. Rebuild both components (Step 3)
  3. Reinstall them (Step 4)
  4. Restart the Streamlit app

### Getting Help

If you encounter issues:
1. Check the terminal/console for error messages
2. Make sure all dependencies are installed
3. Verify Python and Node.js versions meet requirements
4. Try rebuilding the custom components

## 🔄 Development Workflow

### Making Changes to Custom Components

If you modify the React components (sidebar or KPI tiles):

1. Navigate to the component's frontend folder
2. Rebuild the component:
   ```bash
   npm run build
   ```
3. Restart Streamlit (press `Ctrl+C` then run `streamlit run app.py` again)

### Adding New Dependencies

**Python packages:**
1. Install the package: `pip install package-name`
2. Update requirements.txt: `pip freeze > requirements.txt`

**JavaScript packages (for custom components):**
1. Navigate to the component's frontend folder
2. Install: `npm install package-name`
3. Rebuild: `npm run build`

## 📊 Sample CSV Format

For the Upload Keyword Data page, use this CSV format:

```csv
Search Term,Cost,Conversions,Current Bid
snacks marshmallow,150.50,25,0.35
cereal oaties,200.00,40,0.28
crisps pringles,180.25,30,0.42
```

## 🎨 Customization

### Changing Colors

Edit the color values in the respective files:
- **Sidebar**: `custom_sidebar/frontend/src/CustomSidebar.css`
- **KPI Tiles**: `kpi_tiles/frontend/src/KPITiles.css`
- **Main pages**: CSS in `dashboard.py`, `upload_keyword.py`, etc.

### Modifying the Logo

Replace `assets/icons/logo 1.svg` with your own logo file.

## 🔐 Data Source Configuration

### Switching Between Databricks and Snowflake

Edit `DATA_SOURCE` in `config.py`:
```python
DATA_SOURCE = "databricks"  # or "snowflake"
```

### Databricks Setup

**IMPORTANT: Never hardcode credentials in `config.py`!**

Use environment variables (`.env`) or Streamlit secrets (`.streamlit/secrets.toml`) as described in Step 3 of the installation.

The application will automatically load credentials from:
1. Environment variables (highest priority)
2. `.streamlit/secrets.toml` (medium priority)
3. `config.py` (lowest priority - should be left empty)

You can also configure catalog and schema in `config.py`:
```python
DATABRICKS_CONFIG = {
    "host": "",  # Set via .env or secrets.toml
    "token": "",  # Set via .env or secrets.toml
    "http_path": "",  # Set via .env or secrets.toml
    "catalog": "your_catalog",
    "schema": "your_schema"
}
```

### Snowflake Setup

Similarly, configure Snowflake credentials using environment variables or secrets:

**In `.env`:**
```bash
SNOWFLAKE_ACCOUNT=your-account.snowflakecomputing.com
SNOWFLAKE_USER=your-username
SNOWFLAKE_PASSWORD=your-password
SNOWFLAKE_WAREHOUSE=your-warehouse
SNOWFLAKE_DATABASE=your-database
SNOWFLAKE_SCHEMA=your-schema
SNOWFLAKE_ROLE=your-role
```

**Or in `.streamlit/secrets.toml`:**
```toml
[snowflake]
account = "your-account.snowflakecomputing.com"
user = "your-username"
password = "your-password"
warehouse = "your-warehouse"
database = "your-database"
schema = "your-schema"
role = "your-role"
```

## 📝 System Requirements

**Minimum:**
- OS: Windows 10/11, macOS 10.14+, or Linux
- RAM: 4 GB
- Storage: 500 MB free space
- Python: 3.8+
- Node.js: 14.x+

**Recommended:**
- RAM: 8 GB or more
- Python: 3.10+
- Node.js: 18.x+

## 📄 License

[Add your license information here]

## 🤝 Contributing

[Add contribution guidelines here]

## 📧 Contact

[Add contact information here]

---

**Happy analyzing! 📊✨**
