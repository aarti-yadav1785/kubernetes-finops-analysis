# kubernetes-finops-analysis
Kubernetes Cloud Spend &amp; Cluster Optimization using Python, SQL and Power BI

#  Kubernetes FinOps Dashboard — Cloud Waste Analysis

##  Project Overview
Analyzed 60 days of infrastructure metrics across 14 active Kubernetes 
namespaces to identify over-provisioned cluster nodes. Developed a 
Power BI FinOps dashboard that isolated 44-54% resource utilization 
rates. Provided recommendations to reduce monthly cloud spend by $573/month.

##  Tech Stack
- **Python** — Data Generation (Pandas, NumPy)
- **SQLite + SQL** — Data Analysis & Waste Calculation
- **Power BI** — Interactive CFO Dashboard

##  Key Metrics Calculated
- Resource Utilization Rate (CPU & Memory)
- Monthly FinOps Waste ($) per namespace
- Potential Monthly Savings

##  Key Findings
- **Staging** team = highest waste ($46.59/month)
- **Analytics** team = worst CPU & Memory utilization (both low!)
- **Total company waste** = ~$573/month
- Potential savings if optimized = ~$343/month

##  Files
| File | Description |
|------|-------------|
| `kubernetes_analysis.py` | Data generation script |
| `cluster_metrics.csv` | Raw 60-day metrics data |
| `finops_analysis.csv` | Processed waste analysis |
| `*.sql` | SQL queries for analysis |
| `kubernetes_finops_dashboard.pbix` | Power BI Dashboard |
