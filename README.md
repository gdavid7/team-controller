# spreadsheet

This is a spreadsheet to track team races in [Nitro Type](https://www.nitrotype.com).

This was programmed fully in Python, using the libraries [Requests](https://github.com/psf/requests) and [gspread](https://github.com/burnash/gspread).

The program will update a google sheets spreadsheet every 10 minutes showing the top racers, from best to worst. It also stores information from the past 7 days.

![alt text](https://github.com/Limitized/spreadsheet/blob/master/Images/Image%201.PNG?raw=true)

Additionally, it also has a feature that shows graphs that can track a teams progress throughout the week.

![alt text](https://github.com/Limitized/spreadsheet/blob/master/Images/Image%202.PNG?raw=true)

### Installation

1. Upload the [Spreadsheet Template](https://github.com/Limitized/spreadsheet/tree/master/Template%20For%20Spreadsheet) to your google sheets by importing it.

3. Essentially just follow this [tutorial](https://medium.com/@CROSP/manage-google-spreadsheets-with-python-and-gspread-6530cc9f15d1) until you download the client_secret.json.

3. Put your client secret stuff in [client_secret.json](https://github.com/Limitized/spreadsheet/blob/master/client_secret.json). (Open it in notepad and copy and paste into into that one)

4. Change the userinformation.py to fit your settings.

5. Run secpro.py

Hopefully, this will help you get your team to #1!
