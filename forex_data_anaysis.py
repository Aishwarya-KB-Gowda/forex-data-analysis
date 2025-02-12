""" 
Problem Statement: Forex Data Analysis with Python

Objective

The goal of this task is to analyze historical Forex trading data to derive insights such as daily price 
changes and market volatility. The processed data will be stored in a CSV file and sorted based on volatility.

Tasks

*Read Forex Data from a CSV file containing Date, Currency Pair, Open, High, Low, and Close prices.
*Calculate Daily Price Change as Close - Open for each day.
*Calculate Volatility as High - Low to measure market fluctuations.
*Store the processed data in a new CSV file with additional columns: Price Change and Volatility.
*Identify the Most Volatile Day (the day with the highest volatility).
*Sort the Data by Volatility in descending order and print the results.
 """
import csv

# Function to read forex data from CSV
def read_forex_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to process forex data (calculate price change & volatility)
def process_forex_data(data):
    for row in data:
        row['Open'] = float(row['Open'])
        row['Close'] = float(row['Close'])
        row['High'] = float(row['High'])
        row['Low'] = float(row['Low'])

        row['Price Change'] = round(row['Close'] - row['Open'], 4)
        row['Volatility'] = round(row['High'] - row['Low'], 4)
    
    return data

# Function to write processed & sorted data to a CSV file
def write_processed_data(filename, data, most_volatile_day):
    fieldnames = ['Date', 'Currency Pair', 'Open', 'High', 'Low', 'Close', 'Price Change', 'Volatility', 'Most Volatile']

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in data:
            row['Most Volatile'] = 'Yes' if row['Date'] == most_volatile_day['Date'] else 'No'
            writer.writerow(row)

    print(f'Results saved to {filename}')

# Main execution
input_file = 'forex_prices.csv'  # Input CSV file
output_file = 'forex_analysis.csv'  # Output CSV file

# Step 1: Read data
forex_data = read_forex_data(input_file)

# Step 2: Process data
processed_data = process_forex_data(forex_data)

# Step 3: Find the most volatile day
most_volatile_day = max(processed_data, key=lambda x: x['Volatility'])

# Step 4: Sort by volatility (descending order)
sorted_data = sorted(processed_data, key=lambda x: x['Volatility'], reverse=True)

# Step 5: Save results to a single CSV file
write_processed_data(output_file, sorted_data, most_volatile_day)
