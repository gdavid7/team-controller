import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
from operator import itemgetter, attrgetter
import time
from datetime import date
import userinformation



myteam = userinformation.getTeam()


def generateList(team):
    teamMembers = []
    usernames = []
    userids = []
    races = []
    teamURL = requests.get("https://www.nitrotype.com/api/teams/" + team)
    parsed = teamURL.json()["data"]["members"]
    for x in parsed:
        usrn = x["username"]
        uid = str(x["userID"])
        usernames.append(usrn)
        userids.append(uid)
    for x in range(len(userids)):
        playerLink = "https://www.nitrotype.com/api/players/" + userids[x]
        playerGet = requests.get(url = playerLink)
        racingStats = playerGet.json()["data"]["racingStats"]
        if(len(racingStats) >= 2):
            races.append(str((racingStats[1]["played"])))
        else:
            races.append(str(0))
    for i in range (len(userids)):
        userList = []
        userList.append(usernames[i])
        userList.append(userids[i])
        userList.append(int(races[i]))
        teamMembers.append(userList)  
    teamMembers = sorted(teamMembers, key=itemgetter(2), reverse = True)
    dif = 50-len(teamMembers)
    for i in range(0,dif, 1):
        teamMembers.append([" ", str(123456), " "])
    return(teamMembers)

def updateUsernames(list, sheet, usrcol, racecol):
    for i in range (1, len(list) + 1, 1):
        if(sheet.cell(i + 2, usrcol).value != list[i-1][0]):
            username = list[i-1][0]
            #sheet.update_cell(i + 2, usrcol, list[i-1][0])
            sheet.update_cell(i + 2, usrcol, f'=HYPERLINK("https://www.nitrotype.com/racer/{username}", "{username}")')
            time.sleep(0.5)
        if(str(sheet.cell(i + 2, racecol).value) != str(list[i-1][2])):
            sheet.update_cell(i + 2, racecol, list[i-1][2])
            time.sleep(0.5)
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheetName = userinformation.getSheetName()
sheet = client.open(sheetName).sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
bigMin = 1440 #Change day here
#What we want:
#Updates sheet cells every 10 mins
#Updates single cell every 2 mins
#Updates day every 24 hours
#Updates week every 7 days
#1. Set the day in the code
day = 0
datecell = (day * 3) + 2
sheet.update_cell(1, datecell, str(date.today()))
updateGap = 10 #Minutes

#Mins, week can be left alone
min = 0
usercol = (day * 3) + 1
racecol = (day * 3) + 2
while True:
    if(min >= 1440):
        day += 1
        min = 0
        sheet.update_cell(54, usercol, "")
        usercol = (day * 3) + 1
        racecol = (day * 3) + 2
        datecell = (day * 3) + 2
        sheet.update_cell(1, datecell, str(date.today()))
    if(day >= 6):
        day = 0
        sheet.update_cell(54, usercol-3, " ")
        usercol = (day * 3) + 1
        racecol = (day * 3) + 2
    updateMin = 0
    list = generateList(myteam)
    updateUsernames(list, sheet, usercol, racecol)
    time.sleep(0.5)
    for i in range (0, updateGap, 1):
        sheet.update_cell(54, usercol, "Last Updated: " + str(updateMin) + " minutes ago")
        updateMin += 1
        time.sleep(60)
    #Now 10 mins have passed.
    min += updateMin





