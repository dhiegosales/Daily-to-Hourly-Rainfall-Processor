"""
Daily-to-Hourly-Rainfall-Processor
Version: 1.0
Date: 2024-06-18

Author: Dhiego da Silva Sales
Affiliation: Instituto Federal Fluminense
Degree: Master in Environmental Engineering

Description:
This Python script processes a CSV file containing daily rainfall data and converts it into hourly rainfall data.
"""

import csv
from datetime import datetime, timedelta

# Function to convert date from 'dd/mm/yyyy' to 'dd/mm/yyyy hh:min'
def convert_date(date_str, hour):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    date_obj = date_obj.replace(hour=hour)
    return date_obj.strftime('%d/%m/%Y %H:%M')

# Function to process the CSV file
def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile, delimiter=';')
        data = list(reader)

    num_columns = len(data[0])  # Number of columns in the input file
    output_data = []

    header = data[0]  # Extract header
    data = data[1:]   # Skip header

    for row in data:
        date = row[0]  # Get the date from the first column
        for hour in range(24):  # Iterate through each hour of the day
            date_hourly = convert_date(date, hour)  # Convert to 'dd/mm/yyyy hh:min'

            # Process the daily rainfall columns
            row_data = [date_hourly]  # Start with the converted date/time
            for col_idx in range(1, num_columns):
                daily_rainfall = float(row[col_idx])
                hourly_rainfall = daily_rainfall / 24.0  # Divide by 24 to get hourly rainfall
                row_data.append(hourly_rainfall)

            output_data.append(row_data)

    # Write the processed data to the output file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        
        # Write the header to the output file
        hourly_header = [f"{col}_hourly" for col in header]
        writer.writerow(hourly_header)

        writer.writerows(output_data)

    print(f'Output file "{output_file}" successfully generated.')

# Example usage
if __name__ == '__main__':
    input_file = 'input_data.csv'
    output_file = 'output_data.csv'
    process_csv(input_file, output_file)
