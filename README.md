# Europe Sales Records Analysis

## Overview

This project explores and analyzes the Europe Sales Records dataset using Python for data analysis and visualization. The analysis focuses on sales performance, profit trends, country comparisons, item profitability, shipping delays, and sales channel performance.

The project demonstrates practical data analytics skills including:

* Data cleaning
* Exploratory Data Analysis (EDA)
* Aggregation and grouping
* Business insight generation
* Visualization with Matplotlib and Seaborn

Dataset source:
[Europe Sales Records Dataset (Kaggle)] https://www.kaggle.com/datasets/mustafabayar/europe-sales-records

---

# Objectives

* Analyze sales and profit performance across European countries
* Discover the most profitable products and regions
* Compare online vs offline sales performance
* Identify monthly sales and profit trends
* Investigate shipping delays across item categories
* Practice real-world data analysis workflows using Python

---

# Technologies Used

* Python
* pandas
* NumPy
* Matplotlib
* Seaborn
* scikit-learn
* imbalanced-learn
* joblib

---

# Dataset Information

The dataset contains:

* Country information
* Product categories
* Sales channel data
* Order and shipping dates
* Revenue, cost, and profit metrics

### Main Features

* Country
* Item Type
* Sales Channel
* Order Priority
* Units Sold
* Unit Price
* Total Revenue
* Total Cost
* Total Profit

---

# Data Cleaning & Preparation

The following preprocessing steps were performed:

* Removed unnecessary columns

  * `Region`
  * `Order ID`

* Converted date columns to datetime format

  * `Order Date`
  * `Ship Date`

* Checked for:

  * Missing values
  * Duplicate records
  * Outliers

* Created additional features:

  * Month name
  * Month number
  * Shipping delay (days)

---

# Exploratory Data Analysis (EDA)

## Country Profit Analysis

* Identified the countries generating the highest profits
* Compared total profits across European countries
* Analyzed yearly country performance for 2017

### Key Insight

Countries such as:

* Andorra
* Norway
* Albania
* Germany

generated some of the highest individual transaction profits.

---

## Monthly Profit Trends

Monthly profit trends were analyzed using aggregated sales data.

### Findings

* January and March showed strong profit performance
* August and October had comparatively lower profits

This analysis helps identify seasonal sales behavior.

---

## Item Type Profitability

The profitability of different product categories was analyzed.

### Most Profitable Categories (2017)

* Cosmetics
* Office Supplies
* Household
* Snacks

### Least Profitable Categories

* Fruits
* Cereal
* Personal Care

---

## Online vs Offline Sales Performance

Sales channels were compared based on total generated profit.

### Insight

Offline and online channels showed a profit difference of approximately:

```text
$5.7 Million
```

This comparison helps evaluate sales strategy effectiveness.

---

## Shipping Delay Analysis

Shipping delays were calculated using:

```python
Shipping Delay = Ship Date - Order Date
```

Average shipping delays were analyzed by item type.

### Purpose

* Identify inefficient shipping categories
* Evaluate logistics performance

---

# Visualizations Included

The project includes multiple visualizations such as:

* Bar charts
* Horizontal bar plots
* Pie charts
* Monthly trend analysis
* Profit comparisons
* Shipping delay visualizations

# Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Business Analytics
* Feature Engineering
* Aggregation & Grouping
* Trend Analysis
* Insight Generation

# Business Insights

* Certain countries consistently generate high profits
* Cosmetics and office supplies are highly profitable categories
* Sales performance changes significantly across months
* Shipping delays vary depending on product category
* Online and offline sales channels perform differently

---

# Future Improvements

Possible future enhancements include:

* Interactive dashboards using Power BI or Tableau
* Sales forecasting models
* Customer segmentation
* Profit prediction models
* SQL integration
* Deployment as a web dashboard

---

# Author

Data analytics project focused on business insight generation using Python and real-world sales data.
