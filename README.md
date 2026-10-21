# Nassau_Candy_Distributors
Data Analytics project showcasing customer behaviour analysis using Python, SQL and Power BI

# Factory Reallocation & Shipping Optimization Recommendation System for Nassau Candy Distributor

## 📌 Project Overview

This project focuses on analyzing sales, profitability, shipping performance, delivery lead time, and shipping risks for Nassau Candy Distributor.

The objective is to identify opportunities to improve profitability, reduce shipping costs, and enhance operational efficiency through data analysis and interactive visualizations.

The project follows an end-to-end data analytics workflow using SQL, Python, Power BI, and Claude AI to transform raw data into meaningful business insights and recommendations.

## 🎯 Project Objectives

- Analyze sales, costs, gross profit, and profit margins.
- Identify high-performing and low-performing products and regions.
- Evaluate shipping methods and delivery lead times.
- Identify regions with high shipping risks.
- Develop recommendations to improve shipping efficiency.
- Build an interactive Power BI dashboard.
- Prepare a final analytical report and project presentation using Claude AI.

## 📂 Dataset Description

The dataset contains order, product, regional, financial, and shipping information.

| Category | Important Columns |
|---|---|
| Order Details | Order ID, Order Date, Ship Date |
| Product Details | Product ID, Product Name, Division |
| Location | City, State/Province, Region |
| Financial | Sales, Cost, Gross Profit, Profit Margin |
| Shipping | Ship Mode, Lead Time, Shipping Risk |
| Quantity | Units |
| Time | Order Year, Order Month, Order Quarter |
| Additional | Lead Time Category |

**Dataset source:** [Add your dataset source]

**Format:** CSV / Excel

## 🛠️ Tools & Technologies

- **Python:** Data analysis and preprocessing
- **Pandas & NumPy:** Data cleaning and manipulation
- **Matplotlib & Seaborn:** Exploratory Data Analysis (EDA)
- **MySQL / SQL Server:** Data validation and business queries
- **Power BI:** Interactive dashboards and KPI reporting
- **Claude AI:** Assistance with report writing and presentation preparation
- **GitHub:** Project documentation and version control

## 🔄 Project Workflow

### 1. Data Loading and Validation — SQL
- Import the dataset into MySQL or SQL Server.
- Check total records, column structure, and data types.
- Identify missing values, duplicates, and data quality issues.
- Validate the dataset before further analysis.

### 2. Data Cleaning and EDA — Python
- Load the dataset using Pandas.
- Handle missing values and duplicate records.
- Correct data types and inconsistent formats.
- Calculate descriptive statistics.
- Explore sales, profitability, lead times, and shipping risks.
- Create visualizations to identify patterns and trends.

### 3. SQL Business Analysis
- Calculate total sales and gross profit.
- Analyze product and regional profitability.
- Compare average lead times by shipping mode and region.
- Identify high-risk shipping regions.
- Analyze costs and identify areas for operational improvement.

### 4. Power BI Dashboard Development
Build a four-page interactive dashboard:

**Page 1: Executive Overview**
- Total Sales
- Total Gross Profit
- Profit Margin %
- Total Orders
- Average Lead Time
- Monthly Sales Trend

**Page 2: Sales & Profitability Analysis**
- Sales by Product
- Gross Profit by Product
- Profit by Region
- Sales by Division
- Product Profitability Table

**Page 3: Shipping & Risk Analysis**
- Average Lead Time by Ship Mode
- Average Lead Time by Region
- Shipping Risk by Region
- Shipping Risk by Ship Mode
- Lead Time Category Distribution

**Page 4: Optimization & Recommendations**
- Cost by Region
- Lead Time vs. Profit Analysis
- Regional Shipping Performance Matrix
- High-Risk Region Ranking
- Business Recommendation Table

### 5. Report and Presentation
- Prepare a report covering the methodology, analysis, and key findings.
- Use Claude AI to assist with report organization and presentation content.
- Create a PowerPoint presentation explaining the business problem, tools, workflow, dashboard, insights, and recommendations.
- Verify all reported figures and findings against the actual analysis.

## 📊 Dashboard Results

The Power BI dashboard is designed to provide a clear view of business performance across four key areas:

- **Profitability:** Understand which products, divisions, and regions contribute to gross profit.
- **Shipping Performance:** Compare delivery lead times across shipping methods and regions.
- **Shipping Risk:** Identify regions and shipping methods associated with high-risk orders.
- **Optimization Opportunities:** Highlight areas for further investigation to improve shipping efficiency and reduce costs.

### Dashboard Preview

Add your Power BI dashboard screenshot below:
<img width="1517" height="853" alt="Screenshot 2026-10-20 133536" src="https://github.com/user-attachments/assets/2e26de95-2757-44e1-8ff8-e533c5142614" />
<img width="1526" height="857" alt="Screenshot 2026-10-20 133635" src="https://github.com/user-attachments/assets/3e969b09-5dbd-4c34-880d-3e9dc8a3b6cc" />
<img width="1528" height="863" alt="Screenshot 2026-10-20 133728" src="https://github.com/user-attachments/assets/42ed0ce0-e262-4faf-9eea-fa95c7b5c438" />
<img width="1522" height="857" alt="Screenshot 2026-10-20 133744" src="https://github.com/user-attachments/assets/f4bba9b5-f5b8-4901-b647-b39717f1f4ba" />

`[Power BI Dashboard](images/dashboard.png)`

*Replace the image path with the actual screenshot location in your repository.*

## 💡 Key Business Questions

1. Which products and regions generate the highest gross profit?
2. Which divisions contribute the most to sales?
3. Which shipping methods have the longest average lead time?
4. Which regions experience the highest shipping risk?
5. Which regions have high costs and longer delivery times?
6. What operational improvements could help reduce shipping costs?

## 🚀 Factory Reallocation Recommendations

The available dataset supports regional cost analysis, lead-time analysis, shipping-risk analysis, and product profitability analysis.

For more advanced factory reallocation recommendations, additional information may be required, including:

- Factory location and identification
- Factory production capacity and available capacity
- Customer demand
- Factory-to-customer shipping distance
- Actual shipping costs
- Factory-level production costs

These additional data points can help evaluate factory allocation options more reliably.

## 📁 Repository Structure

```text
factory-shipping-optimization/
│
├── data/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── eda_analysis.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── powerbi/
│   └── dashboard.pbix
│
├── reports/
│   └── analysis_report.pdf
│
├── presentation/
│   └── project_presentation.pptx
│
├── images/
│   └── dashboard.png
│
├── requirements.txt
└── README.md
```

*This is a suggested structure. Adjust filenames and folders to match your actual repository.*

## ⚙️ How to Run the Project

### Prerequisites
- Python 3.x
- Jupyter Notebook
- MySQL or SQL Server
- Power BI Desktop
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/factory-shipping-optimization.git
cd factory-shipping-optimization
```

### Step 2: Install Python Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

Alternatively, install dependencies from the requirements file:

```bash
pip install -r requirements.txt
```

### Step 3: Run Python Analysis

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` folder and run them to perform data cleaning and EDA.

### Step 4: Execute SQL Queries

- Create a database in MySQL or SQL Server.
- Import the dataset into a database table.
- Open `sql/analysis_queries.sql`.
- Execute the queries to validate the data and analyze business performance.

### Step 5: Open the Power BI Dashboard

- Open `powerbi/dashboard.pbix` using Power BI Desktop.
- Update the data source connection if necessary.
- Refresh the dataset.
- Explore the four dashboard pages and available filters.

### Step 6: Review the Final Deliverables

Open the report in the `reports/` folder and the PowerPoint presentation in the `presentation/` folder.

## 📦 Project Deliverables

- Cleaned dataset
- Python notebooks for data cleaning and EDA
- SQL scripts for business analysis
- Four-page Power BI dashboard
- Analytical report
- PowerPoint presentation prepared with assistance from Claude AI
- GitHub documentation

## 👤 Author

**Siva Sakthi**

Aspiring Data Analyst

- **GitHub:** [Your GitHub Profile](https://github.com/your-username)
- **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/your-profile/)

## ⭐ Conclusion

This project demonstrates an end-to-end data analytics workflow, combining SQL, Python, and Power BI to analyze profitability, shipping performance, and operational risks. It provides a foundation for data-driven shipping optimization and further factory reallocation analysis.
