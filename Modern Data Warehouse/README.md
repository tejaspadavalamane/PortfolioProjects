# Modern Data Warehouse Project – Microsoft Fabric

This project showcases the implementation of a **Modern Data Warehouse (MDW)** using **Microsoft Fabric**, following the **Medallion Architecture** principles (Bronze, Silver, Gold). It demonstrates how raw data is ingested, processed, and visualized using Microsoft's modern analytics stack.

## Project Overview

This project involves designing a modular and scalable data architecture for handling diverse sales-related datasets. The pipeline transforms raw data into actionable insights through layered processing and powerful reporting tools.

### Tools & Technologies

- **Microsoft Fabric**
  - Lakehouse
  - Synapse Data Engineering
  - Notebooks
  - Data Pipelines
- **Power BI**
- **Schematic Model**
- **Python**
- **Excel (.xlsx)** – Source data

---

## Medallion Architecture

The project follows a three-layered data architecture:

- **Bronze Layer:** Ingests raw, unprocessed data from multiple sources.
- **Silver Layer:** Cleans and transforms the data for consistency.
- **Gold Layer:** Curated and optimized datasets ready for reporting and analytics.

---

## Data Sources

- `Sales_01.xlsx`, `Sales_02.xlsx`, `Sales_03.xlsx`: Sales and transaction data
- `Customer`, `Product`, `Ship Mode`, `Order Priority`, `Return`: Additional customer and order metadata

---

## Dashboard

A Power BI dashboard was built to provide insights including:

- Sales trends and revenue performance
- Order priority analysis
- Customer segmentation
- Return and shipping performance

### Power BI Report: `Tejas.pbix`

---

## Project Structure

```
modern-data-warehouse/
>data/
     Sales_01.xlsx
     Sales_02.xlsx
     Sales_03.xlsx

>code/
     TejasPadavalamane_MDW_Code.zip

>docs/
     TejasPadavalamane_MDWFinalProj.docx
     TejasPadavalamane_PowerBI.pdf\

>dashboard/
     Tejas.pbix


---

## How to Use

1. Load the `.xlsx` files into Microsoft Fabric’s Lakehouse.
2. Use Notebooks and Pipelines to process data through Bronze → Silver → Gold layers.
3. Open `Tejas.pbix` to explore and interact with the dashboard.
4. Review documentation and code in the `docs/` and `code/` folders.

---

## Author

**Tejas Padavalamane**  
Master’s in IT and Management – Data Analytics and Management  
Illinois Institute of Technology
