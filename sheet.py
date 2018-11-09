import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1JtJr-f0HVB8hLfAELZSJSp2UqI4djMo8ol3CtsMTwlk/edit").sheet1

GANG_MEMBERS = wks.cell(8, 13).value
GANG_UPGRADES = wks.cell(8, 15).value
GANG_RANK = wks.cell(8, 16).value

print(GANG_MEMBERS, GANG_UPGRADES, GANG_RANK)