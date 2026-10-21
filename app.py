import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Nassau Candy Shipping Analytics", layout="wide")
st.title("Factory Reallocation & Shipping Optimization")
st.caption("Nassau Candy Distributor | Analytics prototype")
st.warning("This prototype analyzes uploaded historical data. It does not claim factory savings or make validated reassignment recommendations unless factory mapping and cost assumptions are supplied and checked.")

uploaded = st.file_uploader("Upload your Nassau Candy CSV file", type=["csv"])
if uploaded is None:
    st.info("Upload the CSV dataset to begin. Use the exact file you analyzed in SQL/Power BI.")
    st.stop()

try:
    df = pd.read_csv(uploaded)
except Exception as exc:
    st.error(f"Could not read the CSV: {exc}")
    st.stop()

df.columns = [str(c).strip() for c in df.columns]
st.subheader("Data preview")
st.write(f"Rows: {len(df):,} | Columns: {len(df.columns)}")
st.dataframe(df.head(20), use_container_width=True)

def find_col(options):
    lower = {c.lower(): c for c in df.columns}
    for option in options:
        if option.lower() in lower:
            return lower[option.lower()]
    return None

sales_col = find_col(["Sales", "Sum of Sales"])
profit_col = find_col(["Gross Profit", "Profit", "Gross_Profit"])
order_col = find_col(["Order ID", "Order_ID"])
date_order = find_col(["Order Date", "Order_Date"])
date_ship = find_col(["Ship Date", "Ship_Date"])
region_col = find_col(["Region", "Country/Region", "Country_Region"])
division_col = find_col(["Division"])
shipmode_col = find_col(["Ship Mode", "Ship_Mode"])
product_col = find_col(["Product Name", "Product_Name"])

if date_order and date_ship:
    df[date_order] = pd.to_datetime(df[date_order], errors="coerce")
    df[date_ship] = pd.to_datetime(df[date_ship], errors="coerce")
    df["Calculated Lead Time (days)"] = (df[date_ship] - df[date_order]).dt.days
    df.loc[df["Calculated Lead Time (days)"] < 0, "Calculated Lead Time (days)"] = None

def numeric_sum(col):
    if not col:
        return None
    return pd.to_numeric(df[col], errors="coerce").sum()

total_sales = numeric_sum(sales_col)
total_profit = numeric_sum(profit_col)
total_orders = df[order_col].nunique() if order_col else len(df)
lead_col = "Calculated Lead Time (days)" if "Calculated Lead Time (days)" in df.columns else None
avg_lead = pd.to_numeric(df[lead_col], errors="coerce").mean() if lead_col else None

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"{total_sales:,.2f}" if total_sales is not None else "Column not found")
c2.metric("Gross Profit", f"{total_profit:,.2f}" if total_profit is not None else "Column not found")
c3.metric("Distinct Orders", f"{total_orders:,.0f}")
c4.metric("Average Lead Time", f"{avg_lead:.2f} days" if pd.notna(avg_lead) else "Date columns unavailable")

if sales_col and region_col:
    st.subheader("Sales by region")
    temp = df.copy()
    temp[sales_col] = pd.to_numeric(temp[sales_col], errors="coerce")
    agg = temp.groupby(region_col, dropna=False)[sales_col].sum().reset_index()
    st.plotly_chart(px.bar(agg, x=region_col, y=sales_col, title="Sales by Region"), use_container_width=True)

if profit_col and division_col:
    st.subheader("Gross profit by division")
    temp = df.copy()
    temp[profit_col] = pd.to_numeric(temp[profit_col], errors="coerce")
    agg = temp.groupby(division_col, dropna=False)[profit_col].sum().reset_index()
    st.plotly_chart(px.bar(agg, x=division_col, y=profit_col, title="Gross Profit by Division"), use_container_width=True)

if lead_col and region_col:
    st.subheader("Lead time by region")
    agg = df.groupby(region_col, dropna=False)[lead_col].mean().reset_index()
    st.plotly_chart(px.bar(agg, x=region_col, y=lead_col, title="Average Lead Time by Region (days)"), use_container_width=True)

st.subheader("Data quality checks")
quality = pd.DataFrame({
    "Check": ["Missing cells", "Duplicate rows"],
    "Result": [int(df.isna().sum().sum()), int(df.duplicated().sum())]
})
st.dataframe(quality, use_container_width=True)

st.subheader("Optimization readiness")
required = {
    "Product field": product_col,
    "Destination region/city": region_col,
    "Order date": date_order,
    "Ship date": date_ship,
    "Factory assignment": find_col(["Factory", "Factory Name", "Origin Factory"]),
    "Shipping cost": find_col(["Shipping Cost", "Ship Cost", "Freight"])
}
st.dataframe(pd.DataFrame([{"Field": k, "Status": "Found" if v else "Not found — verify source/mapping"} for k,v in required.items()]), use_container_width=True)
st.caption("No factory recommendation or savings figure is generated in this starter until a reliable factory mapping and defensible cost/distance method are provided.")
