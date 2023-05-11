import requests

class UserFlowAPI:
    def __init__(self, api_token):
        self.api_token = api_token
        self.url = "https://api-dev.headspin.io/v0/userflows"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def Create_Userflow(self, name, description):
        payload = {"name": name, "description": description}
        response = requests.put(self.url, headers=self.headers, json=payload)
        response_json = response.json()
        user_flow_id = response_json.get("user_flow_id")
        return user_flow_id,response
    
    def Add_Userflow(self, user_flow_id, session_id):
            url = f"{self.url}/{user_flow_id}/sessions"
            data = {"session_id": session_id}
            response = requests.post(url, headers=self.headers, json=data)
            return response
    
    def Update_Session(self, user_flow_id, session_id, status, status_message):
        url = f"{self.url}/{user_flow_id}/sessions/{session_id}"
        headers = self.headers
        data = {"status": status, "status_message": status_message}
        response = requests.patch(url, headers=headers, json=data)
        print("User flow session updated")
        return response