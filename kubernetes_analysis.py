# ============================================
# LIBRARIES IMPORT KARNA
# ============================================

import pandas as pd
# pandas = data ko table format mein handle karta hai
# jaise Excel ka kaam Python mein karta hai

import numpy as np
# numpy = numbers aur calculations ke liye
# random numbers generate karne mein help karta hai

import sqlite3
# sqlite3 = ek lightweight database
# ye Python mein already built-in hota hai, alag install nahi karna

from datetime import datetime, timedelta
# datetime = date aur time ke saath kaam karne ke liye
# timedelta = dates mein days add/subtract karne ke liye

# ============================================
# STEP 1: NAMESPACES DEFINE KARNA
# ============================================

np.random.seed(42)
# seed(42) = iska matlab hai ki har baar same random numbers aayenge
# isse results consistent rehte hain - agar aap dobara chalao toh same data milega

namespaces = [
    'payment-service', 'user-auth', 'product-catalog',
    'order-management', 'inventory', 'notification-service',
    'analytics', 'reporting', 'ml-pipeline', 'data-ingestion',
    'dev-testing', 'staging', 'logging', 'monitoring'
]
# namespace = company mein alag alag teams/departments hoti hain
# jaise payment-service = payment team ka Kubernetes area
# total 14 namespaces hain jaise video mein mention tha

# ============================================
# STEP 2: PODS DEFINE KARNA
# ============================================

pods_per_namespace = {
    'payment-service':      ['pay-pod-1', 'pay-pod-2', 'pay-pod-3'],
    'user-auth':            ['auth-pod-1', 'auth-pod-2'],
    'product-catalog':      ['catalog-pod-1', 'catalog-pod-2', 'catalog-pod-3'],
    'order-management':     ['order-pod-1', 'order-pod-2'],
    'inventory':            ['inv-pod-1', 'inv-pod-2', 'inv-pod-3'],
    'notification-service': ['notif-pod-1', 'notif-pod-2'],
    'analytics':            ['analytics-pod-1', 'analytics-pod-2'],
    'reporting':            ['report-pod-1', 'report-pod-2'],
    'ml-pipeline':          ['ml-pod-1', 'ml-pod-2', 'ml-pod-3'],
    'data-ingestion':       ['ingest-pod-1', 'ingest-pod-2'],
    'dev-testing':          ['dev-pod-1', 'dev-pod-2', 'dev-pod-3'],
    'staging':              ['stage-pod-1', 'stage-pod-2'],
    'logging':              ['log-pod-1', 'log-pod-2'],
    'monitoring':           ['monitor-pod-1', 'monitor-pod-2']
}
# pod = Kubernetes mein ek chhota container/application hota hai
# har namespace ke andar multiple pods hote hain
# ye dictionary hai - namespace ka naam = uske pods ki list

# ============================================
# STEP 3: CLUSTERS DEFINE KARNA
# ============================================

clusters = ['cluster-prod-1', 'cluster-prod-2', 'cluster-dev-1']
# cluster = ek group of servers jahan pods run hote hain
# prod = production (real users ke liye)
# dev = development (testing ke liye)

# ============================================
# STEP 4: 60 DAYS KA DATA GENERATE KARNA
# ============================================

start_date = datetime(2024, 1, 1)
# data 1 January 2024 se shuru hoga

records = []
# khali list banai - isme saare records store honge

for day in range(60):
# range(60) = 0 se 59 tak loop chalega = 60 din ka data

    timestamp = start_date + timedelta(days=day)
    # har din ka date calculate karo
    # day=0 → 2024-01-01, day=1 → 2024-01-02, aur aage...

    for namespace in namespaces:
    # har din ke liye, har namespace mein jao

        for pod in pods_per_namespace[namespace]:
        # har namespace ke har pod ke liye data banao

            cpu_requested = round(np.random.choice([0.5, 1.0, 1.5, 2.0, 4.0]), 1)
            # cpu_requested = team ne kitna CPU manga (cores mein)
            # randomly 0.5, 1.0, 1.5, 2.0 ya 4.0 cores mein se ek choose hoga
            # ye "booking" hai - actual use nahi

            utilization_rate = np.random.uniform(0.15, 0.75)
            # utilization = actual mein kitna use hua
            # 0.15 to 0.75 matlab 15% to 75% ke beech kuch bhi
            # isse pata chalega ki resource waste hua ya nahi

            cpu_actual_peak = round(cpu_requested * utilization_rate, 3)
            # actual CPU usage = requested * utilization
            # agar 2 cores manga aur 30% use kiya toh = 0.6 cores actual use

            memory_requested = round(np.random.choice([0.5, 1.0, 2.0, 4.0, 8.0]), 1)
            # memory_requested = kitni RAM mangi (GB mein)
            # randomly 0.5 se 8 GB ke beech

            mem_utilization = np.random.uniform(0.20, 0.80)
            # memory utilization bhi random 20% to 80%

            memory_actual_peak = round(memory_requested * mem_utilization, 3)
            # actual memory use = requested * utilization

            records.append({
            # har pod ka ek record banao aur list mein daalo
                'timestamp':          timestamp.strftime('%Y-%m-%d'),
                # date ko YYYY-MM-DD format mein convert karo
                'cluster_id':         np.random.choice(clusters),
                # randomly koi ek cluster assign karo
                'namespace':          namespace,
                # team/department ka naam
                'pod_name':           pod,
                # pod ka naam
                'cpu_requested':      cpu_requested,
                # kitna CPU manga
                'cpu_actual_peak':    cpu_actual_peak,
                # kitna CPU actually use hua
                'memory_requested':   memory_requested,
                # kitni memory mangi
                'memory_actual_peak': memory_actual_peak
                # kitni memory actually use hui
            })

# ============================================
# STEP 5: DATAFRAME BANAO AUR SAVE KARO
# ============================================

df = pd.DataFrame(records)
# records list ko pandas DataFrame mein convert karo
# DataFrame = ek table jisme rows aur columns hote hain

df.to_csv('data/cluster_metrics.csv', index=False)
# DataFrame ko CSV file mein save karo
# index=False = extra numbering column mat add karo

# ============================================
# STEP 6: CONFIRMATION PRINT KARO
# ============================================

print("===== Data Generated Successfully! =====")
print(f"Total Records: {len(df)}")
# kitne total records bane

print(f"Namespaces: {df['namespace'].nunique()}")
# kitne unique namespaces hain

print(f"Date Range: {df['timestamp'].min()} to {df['timestamp'].max()}")
# data kab se kab tak ka hai

print("\n=== Sample Data (pehli 5 rows) ===")
print(df.head())
# pehli 5 rows dikhao