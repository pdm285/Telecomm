import requests
import json
import datetime  
import csv
from concurrent.futures import ThreadPoolExecutor




auth_token = ''
endpoint = 'https://teleworld-api.headspin.io'

session_count = 1


def appendData(masterData, newData, kpi):
    try:
        for data in masterData:
            for newPoint in newData:
                if data['time'] == newPoint['time']:
                    data[kpi] = newPoint[kpi]
        return masterData
    except Exception as e:
        print(f"Error in appendData function: {e}")
        return []

def getFirstData(session):
    try:
        api_endpoint = f'{endpoint}/v0/sessions/timeseries/' + session['session_id'] +'/download?key=blockiness'
        response = output = requests.get(api_endpoint, headers={'Authorization': 'Bearer {}'.format(auth_token)})
        if response.status_code != 200:
            print("Failed to retrieve first data.")
            return []
        else:
            response = (response.text)
            response_arrary = response.split('\n')
            size = len(response_arrary)
            response_arrary[0] = (response_arrary[0])[1:]
            # print(response_arrary[3])
            response_arrary.pop(size-1)
            holderArray = []

            for data in response_arrary:
                data = data.split(',')
                a={}
                a['time'] = data[1]
                a['blockiness'] = data[2]
                holderArray.append(a)
            return holderArray
    except Exception as e:
        print(f"Error in getFirstData function: {e}")
        return []

def collectData(session, kpi, masterData):
    try:
        api_endpoint = f'{endpoint}/v0/sessions/timeseries/' + session['session_id'] +'/download?key=' + kpi
        response = output = requests.get(api_endpoint, headers={'Authorization': 'Bearer {}'.format(auth_token)})
        if response.status_code != 200:
            print(f"Failed to retrieve {kpi} data.")
            return []
        else:
            response = (response.text)
            response_arrary = response.split('\n')
            size = len(response_arrary)
            response_arrary[0] = (response_arrary[0])[1:]
            response_arrary.pop(size-1)
            holderArray = []

            for data in response_arrary:
                data = data.split(',')
                a={}
                a['time'] = data[1]
                a[kpi] = data[2]
                holderArray.append(a)
            return appendData(masterData, holderArray, kpi)
    except Exception as e:
        print(f"Error in collectData function: {e}")
        return []

def collectSessions():
    try:
        api_endpoint = f"{endpoint}/v0/sessions?include_all=true&num_sessions={session_count}"
        response = requests.get(api_endpoint, headers={'Authorization': 'Bearer {}'.format(auth_token)})
        response = json.loads(response.text)
        for i in range(len(response['sessions'])):
            if(response['sessions'][i]['state'] != 'ended'):
                response['sessions'].pop(i)
        return response['sessions']
    except Exception as e:
        print(f"Error in collectSessions function: {e}")
        return []

def exportToCSV(session, masterData):
    try:
        #the first line was just titles
        masterData.pop(0)
        fieldnames = []
        for key in masterData[0]:
            fieldnames.append(key)
        name = session['session_id'] + '.csv'
       

        with open(name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            dataToBeWritten = {}
            for data in masterData:
                for key in fieldnames:
                    dataToBeWritten[key] = data[key]
                writer.writerow(dataToBeWritten)

        csvfile.close()
    except Exception as e:
        print(f"Error in exportToCSV function: {e}")



def convertToEpochTime(session, masterData):
    for data in masterData[1:]:
        data['time'] = str((float(data['time'])/1000) + session['start_time'])
    return masterData




# Define the list of KPIs
kpis = [
    'video_quality_mos',
    'blurriness',
    'colorfulness',
    'downsampling_index',
]

# Set the value of x based on the number of KPIs
x = len(kpis)



def process_kpi(session, kpi, data):
    return collectData(session, kpi, data)


def collect_data_concurrently(session, data):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_kpi, [session]*x, kpis, [data]*x))

    # Combine results
    for i in range(1, len(results)):
        data = appendData(data, results[i], kpis[i])

    return data


sessions = collectSessions()

for x in range(0, session_count):
    print(x)
    data = getFirstData(sessions[x])
    if data:
        data = collect_data_concurrently(sessions[x], data)
        data = convertToEpochTime(sessions[x], data)
    else:
        print(f"No data for session: {x}")
        data = []
    exportToCSV(sessions[x], data)
    print(f"Exported data for session {x}")