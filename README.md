# SEM Campaign Builder

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io)

> A professional-grade SEM (Search Engine Marketing) campaign builder with interactive Streamlit interface that generates comprehensive keyword analysis, ad budget recommendations, and campaign structure planning.

## Live Demo

**[Try the app now!](your-streamlit-app-url.streamlit.app)** 

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [App Interface](#app-interface)
- [Output & Downloads](#output--downloads)
- [Configuration Options](#configuration-options)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Features
-  **Interactive Web Interface** - Easy-to-use Streamlit dashboard
-  **Smart Budget Allocation** - Automated budget distribution across Shopping, Search, and PMax campaigns
-  **Keyword Generation** - Intelligent seed keyword generation from brand and competitor websites
-  **Ad Group Organization** - Automatic keyword grouping by campaign themes
-  **CPC Recommendations** - Data-driven cost-per-click suggestions based on target CPA
-  **Shopping Campaign Optimization** - Product-specific bidding strategies
-  **Performance Max Themes** - Search theme generation for automated campaigns
-  **Location Targeting** - Multi-location campaign planning
-  **Multiple Export Formats** - CSV and JSON download options
-  **Responsive Design** - Works on desktop and mobile devices

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation

### Option 1: Run Locally
```bash
git clone https://github.com/yourusername/sem-campaign-builder.git
cd sem-campaign-builder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

### Option 2: Use the Deployed Version
Simply visit the live app at: **[your-streamlit-app-url.streamlit.app](your-streamlit-app-url.streamlit.app)**

## Usage

### Quick Start
1. **Access the App**: Open the Streamlit interface in your browser.  
2. **Configure Campaign Settings** in the sidebar:
   -  Enter your **brand website URL**  
   -  Add **competitor website URL**  
   -  Select **service locations**  
   -  Set **total monthly budget**  
   -  Adjust **target CPA**  
3. **Generate SEM Plan**: Click the **Generate SEM Plan** button.  
4. **Review Results**: Explore the generated campaign data across multiple tabs.  
5. **Download Reports**: Export your data as **CSV** or **JSON**.

## Step-by-Step Guide

1. **Campaign Configuration**
   - **Brand Website:** `https://yourbrand.com`
   - **Competitor Website:** `https://competitor.com`
   - **Service Locations:** `New York, San Francisco, Los Angeles`
   - **Monthly Budget:** `$15,000`
   - **Target CPA:** `$50`

2. **Generated Outputs**
   - **Ad Budgets:** Automatically allocated across campaign types
   - **Keywords:** Brand and competitor-based seed keywords
   - **Ad Groups:** Organized keyword themes
   - **CPC Recommendations:** Optimized bidding strategies
   - **Shopping Bids:** Product-specific recommendations

---

## App Interface

### Sidebar Configuration
-  **Brand Website URL:** Your company website for keyword generation  
-  **Competitor Website URL:** Competitor analysis for keyword opportunities  
-  **Service Locations:** Geographic targeting options (multi-select)  
-  **Total Monthly Budget:** Campaign budget allocation  
-  **Target CPA:** Cost per acquisition goals

### Main Dashboard Tabs

####  Ad Budgets & Keywords
- Real-time budget breakdown visualization  
- Shopping Ads: 33.3% of total budget  
- Search Ads: 46.7% of total budget  
- Performance Max: 20% of total budget  
- Complete seed keyword analysis

####  Keyword Groups
- **Brand Terms:** Company-specific keywords  
- **Category Terms:** Industry-related keywords  
- **Competitor Terms:** Alternative and comparison keywords  
- **Location-based Queries:** Geographic targeting keywords  
- **Long-Tail Informational:** Detailed search queries

####  CPC Recommendations
- Target CPC based on 2% conversion rate  
- Competition-adjusted bidding multipliers  
- Expected conversions and costs estimates  
- Suggested match types (Exact, Phrase, Broad Match Modifier)

####  Search Themes
- **Product Category Themes:** Core product keywords  
- **Use-case Based Themes:** Application-specific terms  
- **Demographic Themes:** Audience-targeted keywords  
- **Location-based Themes:** Geographic variations

####  Shopping Campaign Bids
- Product-specific CPC recommendations  
- Priority-based budget allocation (high / medium / low volume)  
- Expected conversion metrics and daily budget distribution

---

## Output & Downloads

### Available Export Formats
- **CSV Export** (`sem_keywords.csv`)  
  - Complete keyword list with metrics  
  - Search volume and competition data  
  - CPC recommendations and suggested match types  
  - Expected performance metrics (CTR, CVR estimates)

- **JSON Export** (`sem_plan.json`)  
  - Structured plan for API ingestion or further processing  
  - Contains budgets, keywords, ad groups, PMax themes, and shopping bids

### CSV Export (`sem_keywords.csv`)
- Columns included:
  - `keyword`
  - `avg_monthly_searches`
  - `competition`
  - `top_of_page_bid_low`
  - `top_of_page_bid_high`
  - `priority_score`
  - `suggested_match_types`
  - `suggested_cpc`

---

## JSON Export (`sem_plan.json`)

```json
{
  "ad_budgets": {
    "Shopping Ads Budget": 5000,
    "Search Ads Budget": 7000,
    "PMax Ads Budget": 3000
  },
  "keywords": [],
  "ad_groups": {},
  "search_themes": {},
  "shopping_bids": []
}
```

## Sample Output Metrics

 Ad Budgets:
- Shopping Ads: $5,000 ($167/day)
- Search Ads: $7,000 ($233/day)
- PMax Ads: $3,000 ($100/day)
- Total: $15,000 ($500/day)

 Top Keywords Generated:
- yourbrand software (Volume: 8,500)
- yourbrand platform (Volume: 6,200)
- best yourbrand (Volume: 7,200)
- yourbrand alternatives (Volume: 3,900)

## Configuration Options

### Budget Allocation Logic
```python
shopping_ads_budget = total_budget * 0.333  # 33.3%target_cpc = target_cpa * conversion_rate  # Default: 2%
search_ads_budget = total_budget * 0.467    # 46.7%
pmax_ads_budget = total_budget * 0.200      # 20.0%
```

### CPC Calculation Formula
```python
competition_multipliers = {
    "Low": 0.8,
    "Medium": 1.0, 
    "High": 1.2
}
```

## Supported Locations

- New York  
- San Francisco  
- Los Angeles  
- Chicago  
- Austin  
- Seattle  
- Denver  
- Miami  

## Project Structure
```bash
sem-campaign-builder/
├── 📄 app.py # Main Streamlit application
├── 📄 requirements.txt # Python dependencies
├── 📄 README.md # This file
├── 📄 .gitignore # Git ignore rules
├── 📁 pages/ # Additional Streamlit pages (if any)
├── 📁 utils/ # Utility functions (if separated)
└── 📄 streamlit_app.py # Alternative entry point
```

## Key Dependencies
```bash
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

## Deployment

### Streamlit Cloud Deployment
1. **Push to GitHub**: Ensure your code is in a GitHub repository  
2. **Connect Streamlit Cloud**: Visit [share.streamlit.io](https://share.streamlit.io)  
3. **Deploy**: Select your repository and branch  
4. **Configure**: Set `app.py` as your main file  

---

### Local Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Docker Deployment 
```bash
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## Contributing

We welcome contributions! Here's how you can help:

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/sem-campaign-builder.git

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes and test locally
streamlit run app.py
```

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the interactive interface  
- Designed for Google Ads campaign optimization  
- Created for digital marketing professionals and agencies  
- Optimized for SEM campaign planning and budget allocation  

> Tip: show the CSV preview in the app right after generating the plan, then render the Download button immediately below the table so users can review before downloading.
