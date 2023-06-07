import time
import os
import sys
import json
import subprocess
import argparse

# Load JSON data from the config.json file
with open('resources/config.json', 'r') as file:
    config_data = json.load(file)

if(config_data['HS_TOKEN'] is None):
    print("You must configure your api key in the resources/config.json file")
    exit(-1)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Execute a Python file.')
parser.add_argument('filename', metavar='F', type=str, help='the Python file to execute')
args = parser.parse_args()

# Append '.py' to the filename
file = 'tests/test_' + args.filename + '.py'


# Call the Python file
subprocess.call([sys.executable, file, json.dumps(config_data)])
