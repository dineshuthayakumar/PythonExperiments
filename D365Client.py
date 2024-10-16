import D365PyHelper

crm_connection = D365PyHelper.CrmConnection('Azure Tenant ID', 'https://xyz.crm8.dynamics.com', 'Azure App Registration Client ID', 'Azure App Regitration Client Secret')
crm_connection.get_authtoken()
contacts = crm_connection.get_records('contacts')
for contact in contacts.json()['value']:
    print(contact['fullname'])