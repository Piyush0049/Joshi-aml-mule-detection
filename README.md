# AML Mule Account Detection Challenge

## Team Name
**Joshi**

## Team Members
- **Prerna Joshi** — M.Tech, Indian Institute of Technology Delhi (IIT Delhi)
- **Piyush Joshi** — B.Tech, Netaji Subhas University of Technology (NSUT Delhi)

---

# Project Overview

This project focuses on detecting **mule accounts used for money laundering** in banking systems. Mule accounts are legitimate-looking bank accounts that criminals use to move illicit funds through financial networks.

The objective of this project is to analyze **customer data, account metadata, and transaction history** to identify suspicious accounts and assign a probability score indicating the likelihood that an account is a mule account.

The dataset provided includes multiple sources of information:

- Customer demographic data
- Account-level attributes
- Product holdings
- Branch metadata
- Five years of transaction history
- Training labels identifying known mule accounts

Using these datasets, we developed a machine learning pipeline that identifies behavioral patterns commonly associated with mule accounts.

---

# Approach

The solution is based on **feature engineering combined with machine learning models** designed for large tabular datasets.

The pipeline consists of four major stages:

1. Data Processing
2. Feature Engineering
3. Model Training
4. Prediction Generation

---

# Data Processing

The transaction dataset contains **hundreds of millions of records** stored in Apache Parquet format. To efficiently process this large dataset, the **Polars library** was used due to its high performance with columnar data formats.

Multiple datasets were joined together using relational keys:

customers → customer_account_linkage → accounts → transactions

Additional information such as product holdings and demographics was incorporated to enrich account profiles.

---

# Feature Engineering

Feature engineering played a crucial role in identifying patterns related to mule activity.

## Account-Level Features

The following features were derived from account metadata:

- Account age (days since account opening)
- Time since last KYC update
- Average account balances
- Product family type
- Branch characteristics

These features help identify suspicious situations such as **new accounts performing unusually high-value transactions**.

---

## Transaction Behavior Features

Transaction data was aggregated at the **account level** to generate behavioral statistics.

Key features include:

- Total transaction count
- Total transaction amount
- Mean transaction amount
- Standard deviation of transaction values
- Maximum transaction amount

These statistics help capture abnormal financial activity patterns.

---

## Debit and Credit Behavior

The following features capture how money moves through the account:

- Total credit transaction count
- Total debit transaction count
- Total credited amount
- Total debited amount
- Credit-to-debit ratio

These features help detect **rapid pass-through behavior**, where funds are quickly transferred in and out of accounts.

---

## Suspicious Pattern Detection

Several domain-inspired AML indicators were included.

### Structuring Detection

Criminals often perform transactions just below regulatory thresholds (such as ₹50,000) to avoid triggering monitoring systems.

Feature created:
- Number of transactions between ₹48,000 and ₹50,000

---

### Round Amount Detection

Fraudulent transactions frequently use round numbers.

Feature created:
- Count of transactions divisible by 1000

---

### Counterparty Diversity

Mule accounts often interact with many counterparties.

Feature created:
- Number of unique counterparties

This helps detect **fan-in and fan-out laundering networks**.

---

### Channel Diversity

Feature created:
- Number of unique transaction channels (UPI, ATM, NEFT, etc.)

Unusual channel diversity can indicate suspicious activity.

---

# Machine Learning Models

Two powerful gradient boosting algorithms were used.

## LightGBM

LightGBM is a highly efficient gradient boosting algorithm optimized for large tabular datasets.

Advantages:

- Fast training speed
- High predictive accuracy
- Efficient handling of large feature sets

Key parameters:

- Number of trees: 800
- Learning rate: 0.03
- Maximum depth: 12
- Feature subsampling: 0.8
- Data subsampling: 0.8

---

## CatBoost

CatBoost is another gradient boosting algorithm specifically designed to handle categorical features effectively.

Advantages:

- Automatic categorical encoding
- Strong performance on structured datasets
- Reduced overfitting

Key parameters:

- Iterations: 800
- Learning rate: 0.03
- Tree depth: 10

---

# Ensemble Strategy

Predictions from both models were combined using a simple averaging strategy.

Final Prediction:

0.5 × LightGBM Prediction + 0.5 × CatBoost Prediction

Ensembling improves prediction stability and often results in better performance compared to individual models.

---

# Evaluation Metric

Model performance was evaluated using:

**ROC-AUC (Area Under the Receiver Operating Characteristic Curve)**

ROC-AUC measures the model's ability to distinguish between mule and legitimate accounts.

This metric is particularly suitable for fraud detection problems where the dataset is typically **imbalanced**.

---

# Running the Project

## Environment Setup

**Python Version:** Python 3.10 or higher recommended

## Install Dependencies

```
pip install -r requirements.txt
```

Required libraries:

- pandas
- numpy
- polars
- lightgbm
- catboost
- pyarrow
- scikit-learn
- tqdm
- joblib

---

## Run the Training Pipeline

```
python solution.py
```

This script will:

1. Load all datasets
2. Perform feature engineering
3. Train the machine learning models
4. Generate predictions for test accounts

---

# Output

The pipeline generates a prediction file:

```
submission.csv
```

Format:

```
account_id,is_mule,suspicious_start,suspicious_end
ACCT_000001,0.12,,
ACCT_000002,0.87,,
```

Where:

- **account_id** = unique account identifier  
- **is_mule** = probability score between 0 and 1  
- **suspicious_start** = predicted start time of suspicious activity  
- **suspicious_end** = predicted end time of suspicious activity  

---

# Future Improvements

Several improvements could further enhance the model:

- Graph-based analysis of transaction networks
- Temporal anomaly detection models
- Deep learning approaches for sequential transaction data
- Counterparty risk propagation modeling

These techniques could improve detection of complex laundering networks.

---

# Team

**Team Name:** Joshi

**Team Members**

Prerna Joshi  
M.Tech — Indian Institute of Technology Delhi (IIT Delhi)

Piyush Joshi  
B.Tech — Netaji Subhas University of Technology (NSUT Delhi)