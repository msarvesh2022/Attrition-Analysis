# Bank Customer Churn Analysis

## Core Objective
The objective is not merely to create random and visually appealing charts under the name of insights. This project focuses on numbers that may appear small but can have a significant impact. In the finance and banking sector, revenue, customers, and transactions are vast in scale, so even a 2–3% error in prediction or insight can lead to major consequences. This project primarily explores customer behavior across different geographical locations, analyzes key factors contributing to customer attrition, and identifies ways to improve customer experience. It also predicts borderline customers to help prevent CLV oss, which we calculated in our Excel analysis

So The objective of this project is to analyze customer data from a bank to identify the key factors that influence customer churn (whether a customer leaves the bank or not).  
By understanding these factors, the project aims to generate insights that can help improve customer retention strategies and reduce churn.

Summary - 

- As customers reach the age of 45, they mostly decide whether to continue with the bank’s services or leave.
- However, the average age in the dataset is 37.
- The churn rate is 8% higher among females compared to males. This behavior is consistent across demographics.
- Germany has the highest percentage of customer attrition at around 32%, meaning the bank loses roughly one out of every three customers, which is a very high number.
  
## Dataset Overview
The dataset contains customer-level information such as demographics, account balance, banking products, and churn status.

### Important Columns
- **CustomerId**: Unique ID assigned to each customer.  
- **CreditScore**: Credit score of the customer (indicator of financial health).  
- **Geography**: Country/region of the customer (e.g., France, Spain, Germany).  
- **Gender**: Gender of the customer (Male/Female).  
- **Age**: Age of the customer.  
- **Tenure**: Number of years the customer has been with the bank.  
- **Balance**: Account balance of the customer.  
- **NumOfProducts**: Number of bank products the customer is using (e.g., savings, credit card).  
- **HasCrCard**: Whether the customer has a credit card (Yes/No).  
- **IsActiveMember**: Whether the customer is actively using bank services (Yes/No).  
- **EstimatedSalary**: Estimated annual salary of the customer.  
- **Exited**: Churn indicator (1 = Customer left, 0 = Customer stayed).  
- **Complain**: Whether the customer raised complaints (1 = Yes, 0 = No).  
- **Satisfaction Score**: Rating of customer satisfaction (scale of 1–5).  
- **Card Type**: Type of credit card owned (DIAMOND, PLATINUM, etc.).  
- **Point Earned**: Loyalty/reward points earned by the customer.

## Insights through Visualization

### Total customer recods  of different demogaphic

![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn-1.png)

### Attrition Rate vs Balance in the account
- This Shows attrition rate is lower for lower balance but after the spending years and transaction bank is loosing their high value customers so there could be service problem

![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn-7.png)


### How age is affectiing the customer behaviour 

![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn-2.png)

- As age increases, the attrition rate also rises.
- The critical age is around 45, where the rates of attrition and retention are the same.
- After the age of 45, the bank loses customers significantly.

![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn-7.png)



### Here We added the comparison of retain rate.


![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn-3.png)

### Correation with customer's gender, here Germany shows different behaviour in number from the rest of the two.

![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn-4.png)

![](https://github.com/msarvesh2022/Customer-Churn-Prediction/blob/main/image_sc/bn5.png)




## Goal
- Identify the top factors driving churn.  
- Build visualizations and predictive models to analyze churn behavior.  
- Provide actionable insights for improving customer retention.  







