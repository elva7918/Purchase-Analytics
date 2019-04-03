# Purchase-Analytics
# Requirent
 * Python 2.6, 2.7, 3.3, 3.4, or 3.5
# Table of Contents
 1. Introduction
 2. Challenge
 3. Input datasets
 4. Output datasets
 5. Project Structure
# Introduction
The dataset for this competition is a relational set of files describing customers' orders over time. The goal of the competition is to predict which products will be in a user's next order. The dataset is anonymized and contains a sample of over 3 million grocery orders from more than 200,000 Instacart users. For each user, we provide between 4 and 100 of their orders, with the sequence of products purchased in each order. We also provide the week and hour of day the order was placed, and a relative measure of time between orders.
# Challenge
* For this challenge, I want to calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers.
* number_of_orders. How many times was a product requested from this department? (If the same product was ordered multiple times, I count it as multiple requests)
* number_of_first_orders. How many of those requests contain products ordered for the first time?
* percentage. What is the percentage of requests containing products ordered for the first time compared with the total number of requests for products from that department? (e.g., number_of_first_orders divided by number_of_orders)
# Input datasets
* order_products.csv
* products.csv
# Output datasets
* report.csv
  * department_id
  * number_of_orders
  * number_of_first_orders
  * percentage

