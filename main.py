from time import sleep
from urllib.request import urlretrieve
import os

# Variables to use
amt_request_six_months = 0
amt_request_total = 0

def getSixMonths(file):
    global amt_request_six_months
    # Reading from file
    Content = file.read()
    line_list = Content.split("\n")
    # startMonAndDay: "24/Oct/1994"

    for line in line_list:
        if line:
            amt_request_six_months += 1
            if "24/May/1995" in line:
                return (amt_request_six_months - 1)


LOCAL_FILE = 'http_access_log.txt'

# Paula's Code: Calculating the requests from the past 6 months
file = open(LOCAL_FILE, "r")
amt_request_six_months = getSixMonths(file)

# Irish's Code: Calculating total amount of requests

# Roxanna's Code: Outputting the requested amounts
print("Total Amount of Data requested within six months:", amt_request_six_months)

print("Total Amount of Requests for the total amount of time period:", amt_request_total)
