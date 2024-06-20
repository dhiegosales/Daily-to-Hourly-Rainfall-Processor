import csv
import os
import sys
from datetime import datetime
import time

# Function to print header information
def print_header():
    print_separator()
    print("Welcome to the Daily2HourRain: Daily to Hourly Rainfall Processor")
    print("Version: 1.0")
    print("Language: Python 3")
    print("Date: June 2024")
    print("Author: Dhiego da Silva Sales")
    print("Credentials: Geographer, MSc in Environmental Engineering")
    print("Affiliation: Instituto Federal Fluminense")
    print("Contact: dhiego.sales@outlook.com\n")
    print("Description: This Python program processes a CSV file containing daily rainfall data and converts it into hourly rainfall data.")
    print_separator()

# Function to print a separator line
def print_separator():
    print("=" * 80)
    
# Function to print a separator line
def print_separator_simple():
    print("-" * 80)

# Function to convert date from 'dd/mm/yyyy' to 'dd/mm/yyyy hh:min'
def convert_date(date_str, hour):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    date_obj = date_obj.replace(hour=hour)
    return date_obj.strftime('%d/%m/%Y %H:%M')

# Function to check if the date is in the correct format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Function to check for empty header cells
def check_empty_header_cells(header):
    if any(cell.strip() == '' for cell in header):
        print(f'File "{input_file}" has empty header cells. Please ensure all headers are filled.')
        print('The program will close in 30 seconds.')
        print_separator()
        for i in range(30, 0, -1):
            sys.stdout.write(f'\rClosing in {i} seconds...')
            sys.stdout.flush()
            time.sleep(1)
        sys.exit()
    else:
        print('All headers are present.')
        time.sleep(4)

# Function to process the CSV file
def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile, delimiter=';')
        data = list(reader)

    if not data:
        print(f'File "{input_file}" is empty.')
        return

    header = data[0]  # Extract header
    data = data[1:]   # Skip header

    # Inform user that the file was successfully loaded
    print(f'File "{input_file}" loaded successfully.')
    print_separator_simple()
    print("Processing file...")
    time.sleep(4)

    # Check for empty header cells
    check_empty_header_cells(header)

    # Number of columns in the input file
    num_columns = len(header)

    # Inform the user about the number of stations
    num_stations = num_columns - 1  # Excluding the date column
    print(f'Number of stations found: {num_stations}')
    time.sleep(4)

    # Check if the first column is a date and if dates are in the correct format
    for row in data:
        if not is_valid_date(row[0]):
            print(f'The first column in file "{input_file}" must contain dates in the format dd/mm/yyyy.')
            print('Please ensure the file is in the correct format for processing.')
            print('The program will close in 30 seconds.')
            print_separator()

            # Countdown timer
            for i in range(30, 0, -1):
                sys.stdout.write(f'\rClosing in {i} seconds...')
                sys.stdout.flush()
                time.sleep(1)
            
            sys.exit()
    
    print('The first column contains dates in the correct format (dd/mm/yyyy).')
    time.sleep(4)

    # Check for empty cells, negative values, and non-numeric values
    has_negative_values = False
    has_empty_cells = False
    has_non_numeric_values = False

    for row in data:
        for col in row[1:]:
            if col == '' or col is None:
                has_empty_cells = True
            try:
                value = float(col)
                if value < 0:
                    has_negative_values = True
            except ValueError:
                has_non_numeric_values = True

    if has_empty_cells:
        print(f'The file "{input_file}" contains empty cells. Please fill all gaps in precipitation data.')
        print('The program will close in 30 seconds.')
        print_separator()
        for i in range(30, 0, -1):
            sys.stdout.write(f'\rClosing in {i} seconds...')
            sys.stdout.flush()
            time.sleep(1)
        sys.exit()
    else:
        print('No empty cells found in the data.')
        time.sleep(4)

    if has_negative_values:
        print(f'The file "{input_file}" contains negative values. Please correct the data.')
        print('The program will close in 30 seconds.')
        print_separator()
        for i in range(30, 0, -1):
            sys.stdout.write(f'\rClosing in {i} seconds...')
            sys.stdout.flush()
            time.sleep(1)
        sys.exit()
    else:
        print('No negative values found in the data.')
        time.sleep(4)

    if has_non_numeric_values:
        print(f'The file "{input_file}" contains non-numeric values. Please correct the data.')
        print('The program will close in 30 seconds.')
        print_separator()
        for i in range(30, 0, -1):
            sys.stdout.write(f'\rClosing in {i} seconds...')
            sys.stdout.flush()
            time.sleep(1)
        sys.exit()
    else:
        print('All values are numeric (integers or floats).')
        time.sleep(4)

    output_data = []

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

    print_separator()
    print(f'Output file "{output_file}" successfully generated.')
    print(f'The file has been created in the directory: {os.path.abspath(output_file)}')
    print('The program will close in 30 seconds.')
    print_separator()

    # Countdown timer before closing
    for i in range(30, 0, -1):
        sys.stdout.write(f'\rClosing in {i} seconds...')
        sys.stdout.flush()
        time.sleep(1)

# Main execution
if __name__ == '__main__':
    # Print the header information
    print_header()
    
    # Identify current directory
    current_directory = os.getcwd()
    print(f'Current directory: {current_directory}')
    print_separator_simple()
    time.sleep(4)

    # Define file names
    input_file = 'daily_rainfall.csv'
    output_file = 'hourly_rainfall.csv'

    # Check if input file exists
    if not os.path.isfile(input_file):
        print(f'File "{input_file}" not found in the current directory.')
        print('Please make sure the following file is in the same directory as this executable:')
        print('1. daily_rainfall.csv')
        print('The program will close in 30 seconds.')
        print_separator()

        # Countdown timer
        for i in range(30, 0, -1):
            sys.stdout.write(f'\rClosing in {i} seconds...')
            sys.stdout.flush()
            time.sleep(1)
        
        sys.exit()

    # Process the CSV file
    process_csv(input_file, output_file)
