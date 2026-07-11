import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
document = client.open('Music v4.5.2')
sheet = document.sheet1
result = sheet.cell(2, 1).value
print(result)
document.add_worksheet("apitest", 5, 5)