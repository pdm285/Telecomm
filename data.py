#!/usr/bin/env python3
import os
import sys
import requests
import csv
import datetime
import pandas as pd
import json

# Set the session ID from the provided parameter
SESSION_ID = sys.argv[1]

# Load JSON data from the config.json file
with open('resources/config.json', 'r') as file:
    config_data = json.load(file)
    HS_TOKEN = config_data['HS_TOKEN']
# Set your key
KEY = (HS_TOKEN or os.environ['HS_TOKEN'])

# Check if the session ID parameter is provided
if len(sys.argv) < 2:
    print("Please provide the session ID as a parameter.")
    sys.exit(1)
if (KEY==None):
    print("Please provide your HS_TOKEN in the resources/config.json file")
    sys.exit(1)

# Define the list of KPIs
KPI_LIST = [
    "video_quality_mos",
    "blurriness",
    "colorfulness",
    "downsampling_index",
    "impact",
    "impact_kde",
    "blockiness",
    "contrast",
    "brightness",
    "page_content",
    "screen_change",
    "screen_rotation",
    "network_in_bytes",
    "network_out_bytes",
    "network_in_packets",
    "network_out_packets",
    "network_in_bytes_total",
    "network_out_bytes_total",
    # Add more KPIs as needed
]

# Create a folder for the session
SESSION_FOLDER = f"session_{SESSION_ID}"
os.makedirs(SESSION_FOLDER, exist_ok=True)

# Retrieve start time of session
API_ENDPOINT = f"https://{config_data['API_BASE']}/v0/sessions/{SESSION_ID}/timestamps"

# API_ENDPOINT = f"https://teleworld-api.headspin.io/v0/sessions/{SESSION_ID}/timestamps"
headers = {
    "Authorization": f"Bearer {KEY}"
}

response = requests.get(API_ENDPOINT, headers=headers).json()
start_time = response["capture-started"]

# Loop through the KPI list and make API calls for each KPI
for KPI in KPI_LIST:
    # Construct the output file name
    OUTPUT_FILE = f"{SESSION_FOLDER}/{KPI}.csv"

    # Define the API endpoint and authentication token
    API_ENDPOINT = f"https://{KEY}@teleworld-api.headspin.io/v0/sessions/timeseries/{SESSION_ID}/download?key={KPI}"

    # Make the API call and save the response to the output file
    response = requests.get(API_ENDPOINT)
    with open(OUTPUT_FILE, 'wb') as output_file:
        output_file.write(response.content)

    # Display a success message
    print(f"Exported {KPI} to {OUTPUT_FILE}")

    # Process the CSV file, skip the first row, and replace the timestamp
    with open(OUTPUT_FILE, 'r') as csv_file, open(OUTPUT_FILE + '.tmp', 'w', newline='') as temp_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(temp_file)

        # Process the header row
        header_row = next(csv_reader)
        csv_writer.writerow(header_row[:2] + header_row[3:])  # Exclude the original timestamp column

        # Process each row in the CSV file
        for row in csv_reader:
            timestamp = float(row[1])/1000
            new_timestamp = datetime.datetime.fromtimestamp(start_time + timestamp).astimezone(datetime.timezone(datetime.timedelta(hours=-4))).strftime('%Y-%m-%d %H:%M:%S')
            csv_writer.writerow(row[:1] + [new_timestamp] + row[2:])  # Replace the timestamp column

    # Replace the original file with the modified file
    os.replace(OUTPUT_FILE + '.tmp', OUTPUT_FILE)

print(f"The CSV files in {SESSION_FOLDER} have been updated with the desired format")




API_ENDPOINT = f"https://teleworld-api.headspin.io/v0/sessions/analysis/issues/{SESSION_ID}"


DATA = requests.get(API_ENDPOINT, headers=headers).json()



def xls_title(string):
    return string[:25]


OUTPUT_FILE = f"{SESSION_FOLDER}/issues.xlsx"

# Create an ExcelWriter object
WRITER = pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl')

# Iterate over each key-value pair in the data dictionary
for sheet_name, sheet_data in DATA.items():
    # Create a DataFrame for the current sheet data
    df = pd.DataFrame(sheet_data)
    sheet_name = sheet_name.replace(':'," -")
    sheet_name = xls_title(sheet_name)
    # Write the DataFrame to the Excel file
    df.to_excel(WRITER, sheet_name=sheet_name, index=False)

# Save the Excel file
WRITER.close()