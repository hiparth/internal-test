# Databricks Deployment Guide

This guide will help you deploy the Retail Media Analytics Dashboard to Databricks.

## Prerequisites

1. **Databricks Workspace** with appropriate permissions
2. **Databricks CLI** installed and configured
3. **Node.js and npm** for building React components
4. **Python 3.8+** with pip

## Deployment Methods

### Method 1: Using Databricks Asset Bundles (Recommended)

This is the modern, recommended approach for deploying apps to Databricks.

#### Step 1: Install Databricks CLI

```bash
# Install via pip
pip install databricks-cli

# Or download from https://github.com/databricks/cli/releases
```

#### Step 2: Configure Databricks CLI

```bash
# Configure authentication
databricks configure

# You'll be prompted for:
# - Databricks Host (e.g., https://your-workspace.cloud.databricks.com)
# - Personal Access Token (create one in User Settings > Access Tokens)
```

#### Step 3: Set Up Secrets in Databricks

Store your database credentials securely using Databricks Secrets:

```bash
# Create a secret scope
databricks secrets create-scope --scope retail-media-dashboard

# Add your database credentials
databricks secrets put --scope retail-media-dashboard --key databricks_host
databricks secrets put --scope retail-media-dashboard --key databricks_token
databricks secrets put --scope retail-media-dashboard --key databricks_http_path
```

#### Step 4: Build Custom React Components

Before deployment, build all custom components:

```bash
# Build custom sidebar
cd custom_sidebar/frontend
npm install
npm run build
cd ../..

# Build KPI tiles
cd kpi_tiles/frontend
npm install
npm run build
cd ../..

# Build performance table
cd performance_table/frontend
npm install
npm run build
cd ../..
```

#### Step 5: Deploy with Databricks Asset Bundles

```bash
# Validate the configuration
databricks bundle validate

# Deploy to development environment
databricks bundle deploy -t dev

# Deploy to production environment
databricks bundle deploy -t prod
```

#### Step 6: Run the Application

```bash
# Run the app
databricks bundle run retail_media_dashboard -t dev
```

The Databricks workspace will provide a URL to access your Streamlit app.

---

### Method 2: Manual Deployment via Databricks Repos

If you prefer a simpler approach without Asset Bundles:

#### Step 1: Set Up Databricks Repo

1. In your Databricks workspace, go to **Repos**
2. Click **Add Repo**
3. Enter your Git repository URL
4. Click **Create Repo**

#### Step 2: Build Components in Databricks

Create a notebook in Databricks to build the React components:

```python
# Install Node.js (if not available)
%sh
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Navigate to your repo directory
%sh
cd /Workspace/Repos/your-username/retail-media-dashboard

# Build custom components
cd custom_sidebar/frontend && npm install && npm run build && cd ../..
cd kpi_tiles/frontend && npm install && npm run build && cd ../..
cd performance_table/frontend && npm install && npm run build && cd ../..
```

#### Step 3: Install Python Dependencies

```python
%pip install -r /Workspace/Repos/your-username/retail-media-dashboard/requirements.txt
%pip install -e /Workspace/Repos/your-username/retail-media-dashboard/custom_sidebar/
%pip install -e /Workspace/Repos/your-username/retail-media-dashboard/kpi_tiles/
%pip install -e /Workspace/Repos/your-username/retail-media-dashboard/performance_table/
```

#### Step 4: Configure Secrets

In a Databricks notebook, set up your secrets:

```python
# Using Databricks dbutils.secrets
import os

# These will read from your secret scope
os.environ['DATABRICKS_HOST'] = dbutils.secrets.get(scope="retail-media-dashboard", key="databricks_host")
os.environ['DATABRICKS_TOKEN'] = dbutils.secrets.get(scope="retail-media-dashboard", key="databricks_token")
os.environ['DATABRICKS_HTTP_PATH'] = dbutils.secrets.get(scope="retail-media-dashboard", key="databricks_http_path")
```

#### Step 5: Run the Streamlit App

```python
%sh
cd /Workspace/Repos/your-username/retail-media-dashboard
streamlit run app.py --server.port 8501 --server.headless true
```

Or create a Databricks App directly from the workspace UI.

---

### Method 3: Using Databricks Apps (Beta)

Databricks Apps is the newest way to deploy Streamlit apps with one click.

#### Step 1: Navigate to Apps

1. In your Databricks workspace, click **Apps** in the left sidebar
2. Click **Create App**

#### Step 2: Configure the App

1. **Name**: Retail Media Analytics Dashboard
2. **Source**: Git repository or upload files
3. **Entry point**: `app.py`
4. **Python version**: 3.10 or higher
5. **Compute**: Select or create a cluster

#### Step 3: Add Environment Variables

In the app configuration, add:
- `DATABRICKS_HOST`
- `DATABRICKS_TOKEN`
- `DATABRICKS_HTTP_PATH`

Or reference secrets:
- `{{secrets/retail-media-dashboard/databricks_host}}`
- `{{secrets/retail-media-dashboard/databricks_token}}`
- `{{secrets/retail-media-dashboard/databricks_http_path}}`

#### Step 4: Deploy

1. Click **Deploy**
2. Wait for the build to complete
3. Access your app via the provided URL

---

## Important Configuration Files

### `databricks.yml`
The main configuration file for Databricks Asset Bundles. It defines:
- Bundle metadata
- Workspace paths
- Build artifacts
- Job configurations
- Environment variables
- Deployment targets

### `setup.py`
Python package configuration for installing the app as a wheel package.

### `.streamlit/config.toml`
Streamlit-specific configuration for:
- Server settings
- CORS and security
- Theme customization
- Performance optimization

### `MANIFEST.in`
Specifies which files to include/exclude in the distribution package.

---

## Post-Deployment

### Verify the Deployment

1. Check that all custom components are rendering correctly
2. Verify database connections are working
3. Test all pages (Dashboard, Upload Keyword, Performance Data, Model Run Results)
4. Check that filters and interactions work as expected

### Monitoring

Monitor your app's performance in Databricks:
- Check the Job Runs page for logs
- Monitor cluster metrics
- Review any error messages

### Updating the App

When you make changes:

**Using Asset Bundles:**
```bash
databricks bundle deploy -t dev
```

**Using Repos:**
1. Commit and push changes to your Git repo
2. Pull the latest changes in Databricks Repos
3. Restart the app

**Using Databricks Apps:**
1. Commit and push changes
2. Click **Redeploy** in the Apps UI

---

## Troubleshooting

### Issue: Custom components not showing

**Solution**: Ensure React components are built before deployment:
```bash
# Rebuild all components
cd custom_sidebar/frontend && npm run build && cd ../..
cd kpi_tiles/frontend && npm run build && cd ../..
cd performance_table/frontend && npm run build && cd ../..
```

### Issue: Database connection errors

**Solution**: Verify secrets are set correctly:
```bash
# List secrets in scope
databricks secrets list --scope retail-media-dashboard
```

### Issue: Port conflicts

**Solution**: Change the port in `.streamlit/config.toml`:
```toml
[server]
port = 8502  # or another available port
```

### Issue: Module not found errors

**Solution**: Ensure all custom components are installed:
```bash
pip install -e custom_sidebar/
pip install -e kpi_tiles/
pip install -e performance_table/
```

---

## Security Best Practices

1. **Never commit secrets** to Git (already configured in `.gitignore`)
2. **Use Databricks Secrets** for all sensitive credentials
3. **Enable RBAC** to control who can access the app
4. **Use separate environments** (dev, staging, prod) with different secret scopes
5. **Regularly rotate** access tokens and database credentials
6. **Monitor access logs** in Databricks

---

## Cost Optimization

1. **Use Spot Instances** for non-production environments
2. **Auto-terminate clusters** when not in use
3. **Right-size your cluster** - Streamlit doesn't need many workers
4. **Use serverless SQL** for database queries when possible

---

## Need Help?

- **Databricks Documentation**: https://docs.databricks.com/
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Databricks Asset Bundles**: https://docs.databricks.com/dev-tools/bundles/
- **Databricks Apps**: https://docs.databricks.com/apps/

---

**Happy deploying! 🚀**

