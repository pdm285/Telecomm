import requests
import os
import json

# Set your token from https://ui.headspin.io/mysettings
TOKEN = ""

# Enter the number of sessions to download
NUM=10

# Enter the API Base URL.  The default is https://api-dev.headspin.io but can change in AIR GAP or self hosted models
BASE_URL = 'https://api-dev.headspin.io'

# Function to dynamically fetch keys for the Time Series Session Data
def fetchKeys(SESSION):
    KEY_API = f"{BASE_URL}/v0/sessions/timeseries/{SESSION}/info"
    response = requests.get(KEY_API, headers={'Authorization': 'Bearer {}'.format(TOKEN)})
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch session info.")
        return "DOWNLOAD FAILED"
    
# Function to use the keys to dynamically gather all the Time Series Data.
def fetchInfo(KEY,SESSION):
    INFO_API = f"{BASE_URL}/v0/sessions/timeseries/{SESSION}/download?key="
    response = requests.get(INFO_API + KEY, headers={'Authorization': 'Bearer {}'.format(TOKEN)})

    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch session info.")
        return "DOWNLOAD FAILED"
    
# Function to fetch and then export to JSON format all issues
def fetchIssues(SESSION):
    ISSUE_API = f"{BASE_URL}/v0/sessions/analysis/issues/{SESSION}"
    response = requests.get(ISSUE_API, headers={'Authorization': 'Bearer {}'.format(TOKEN)})
    if response.status_code == 200:
            DATA = json.loads(response.text)
            exportJSON(DATA)
            return
    else:
        print("Failed to fetch session info.")
        return "DOWNLOAD FAILED"

# Function to fetch & export HAR File
# WIP NOT FINISHED
def fetchHAR(SESSION):
    DATA_API = f"{BASE_URL}/v0/sessions/{SESSION}."
    response = requests.get(DATA_API + "har?enhanced=True", headers={'Authorization': 'Bearer {}'.format(TOKEN)})
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch session info.")
        return "DOWNLOAD FAILED"

# Function to fetch & export PCAP File
# WIP NOT FINISHED
def fetchPCAP(SESSION):
    DATA_API = f"{BASE_URL}/v0/sessions/{SESSION}."
    response = requests.get(DATA_API + "pcap", headers={'Authorization': 'Bearer {}'.format(TOKEN)})
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch session info.")
        return "DOWNLOAD FAILED"

def exportToCSV(DATA,FILE):
    PATH = os.path.join(os.getcwd(), SESSION['session_id'])
    if not os.path.exists(PATH):
        os.makedirs(SESSION['session_id'])
    try:
        with open(os.path.join(SESSION['session_id'],FILE), 'w', newline='') as csvfile:
            for line in DATA:
                csvfile.write(line + "\n")
        print(f'Data has been successfully exported to {FILE}')
    except Exception as e:
        print(f'Error exporting data to {FILE}: {str(e)}')

def fetchTimeSeriesData(SESSION):
    KEYS = fetchKeys(SESSION)
    for KEY in KEYS:
        DATA = fetchInfo(KEY,SESSION)
        DATA = DATA.split("\n")
        exportToCSV(DATA,KEY + ".csv")
    return

def exportJSON(DATA):
    PATH = os.path.join(os.getcwd(), SESSION['session_id'])
    with open(PATH+"/Issues.json", "w") as jsonfile:
        json.dump(DATA,jsonfile)


# Function to collect NUM ammount of sessions (defined at the top)
def collectSessions(NUM):
    SESSIONS_API = f'{BASE_URL}/v0/sessions?include_all=true&num_sessions={NUM}'
    try:
        response = requests.get(SESSIONS_API, headers={'Authorization': 'Bearer {}'.format(TOKEN)})
        response = json.loads(response.text)
        for i in range(len(response['sessions'])):
            if(response['sessions'][i]['state'] != 'ended'):
                response['sessions'].pop(i)
        return response['sessions']
    except Exception as e:
        print(f"Error in collectSessions function: {e}")
        return []


# PROGRAM MAIN
if __name__:
    SESSIONS = collectSessions(NUM)
    for SESSION in SESSIONS:
        try:
            print(f"Downloading data for {SESSION['session_id']}")
            fetchTimeSeriesData(SESSION['session_id'])
            fetchIssues(SESSION['session_id'])
        except:
            print(f"Error with Session: {SESSION['session_id']}")

