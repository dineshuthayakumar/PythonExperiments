import requests
import json

class CrmConnection:

    def __init__(self, azure_directory_id, resource, client_id, client_secret):
        self.azure_directory_id = azure_directory_id
        self.resource = resource
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_token = None

    def get_authtoken(self):
        URL = "https://login.microsoftonline.com/" + self.azure_directory_id + "/oauth2/token"
        payload = {'client_id':self.client_id, 'resource':self.resource, 'client_secret':self.client_secret, 'grant_type':'client_credentials'}        
        response = requests.post(url=URL, data=payload)
        self.auth_token = response.json()['access_token']
        

    def get_records(self, entity_plural_name):
        URL = self.resource.replace('.',".api.",1) + "/api/data/v9.2/" + entity_plural_name
        authtokenString = "Bearer " + self.auth_token
        HEADERS = {"Authorization":authtokenString}
        response = requests.get(url = URL, params = None, headers=HEADERS)
        return response

    def create_record(self, entity_plural_name, column_values):
        URL = self.resource.replace('.',".api.",1) + "/api/data/v9.2/" + entity_plural_name
        authtokenString = "Bearer " + self.auth_token
        HEADERS = {"Authorization":authtokenString, "Content-Type":"application/json; charset=utf-8", "OData-MaxVersion":"4.0", "OData-Version":"4.0", "Accept":"application/json"}
        response = requests.post(url = URL, data = json.dumps(column_values), headers=HEADERS)
        print(json.dumps(column_values))
        return response
