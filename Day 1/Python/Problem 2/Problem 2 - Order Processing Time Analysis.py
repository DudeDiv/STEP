"""Problem Statement:
Analyze the time taken for processing customer orders using Python and
Pandas. Implement a program that:
• Reads the order processing log from a CSV file.
• Calculates the average processing time per order.
• Identifies orders that took longer than the average.
• Displays the top 5 slowest orders by processing time.

Business Insight:
• Helps identify inefficiencies in the order fulfillment process.

Recommended Output Format:

Average Order Processing Time: 3.5 hours

Orders Taking Longer Than Average:
Order_ID Processing_Time (hours)
1023 5.2
1056 4.8

Top 5 Slowest Orders:
Order_ID Processing_Time (hours)
1089 6.1
1090 5.9
1023 5.2

Hint:
• Use pd.to_datetime() to convert timestamps.
• Compute the time difference between Order_Placed and Order_Completed.
• Use .nlargest(5, 'Processing_Time') to get slowest orders."""

#Code (Run in Colab by Uploading CSV File):

import pandas as pd

# Load the CSV file into a Pandas DataFrame
file_name = 'order_processing_log.csv'
data = pd.read_csv(file_name)

# Convert timestamps to datetime objects
data['Order_Placed'] = pd.to_datetime(data['Order_Placed'])
data['Order_Completed'] = pd.to_datetime(data['Order_Completed'])

# Calculate processing time in hours
data['Processing_Time'] = (data['Order_Completed'] - data['Order_Placed']).dt.total_seconds() / 3600

# Calculate average processing time
average_processing_time = data['Processing_Time'].mean()
print(f"Average Order Processing Time: {average_processing_time:.2f} hours")

# Identify orders taking longer than average
long_orders = data[data['Processing_Time'] > average_processing_time]
print("\nOrders Taking Longer Than Average:")
print(long_orders[['Order_ID', 'Processing_Time']])

# Display top 5 slowest orders
top_slowest_orders = data.nlargest(5, 'Processing_Time')
print("\nTop 5 Slowest Orders:")
print(top_slowest_orders[['Order_ID', 'Processing_Time']])
