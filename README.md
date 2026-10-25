# EU ICT & AI Employment: End-to-End Data Pipeline & Forecasting

## Executive Summary
This project is a complete, end-to-end data analytics pipeline designed to analyze historical Information and Communication Technology (ICT) employment trends across the European Union and evaluate the current demand for Artificial Intelligence (AI) skills. The objective is to provide actionable intelligence for strategic workforce planning and policy-making.

## Architecture & Technology Stack
* **Data Engineering (ETL):** Python (Pandas, NLP libraries)
* **Database / Data Warehouse:** PostgreSQL, SQLAlchemy
* **Machine Learning & Predictive Modeling:** Scikit-Learn (Linear Regression), XGBoost
* **Business Intelligence (BI):** Microsoft Power BI

## Methodology & Pipeline
1. **Data Extraction & Cleaning:** Ingested unstructured AI job posting data (Kaggle) and macroeconomic historical employment data (Eurostat). Applied rigorous data wrangling and NLP techniques in Python to sanitize textual data and harmonize schemas.
2. **Database Ingestion:** Engineered an automated ETL process to load the cleaned datasets into a local PostgreSQL relational database, establishing a centralized Data Warehouse.
3. **Predictive Analytics:** Trained multiple machine learning algorithms. Evaluated XGBoost and Linear Regression to forecast the trajectory of EU ICT employment for the 2027-2031 period, successfully deploying the optimal model for time-series extrapolation.
4. **Data Visualization:** Connected the PostgreSQL database directly to Power BI to develop a dynamic, executive-level dashboard highlighting historical trends, 5-year forecasts, and the most highly demanded AI job roles in the market.

## Key Insights
* Consistent, structural growth in ICT employment across the EU over the past decade.
* Predictive models indicate a robust, continued upward trajectory for the 2027-2031 forecasting period.
* High market demand is currently concentrated in core technical roles: Software Engineering, Data Engineering, and Data Science.
