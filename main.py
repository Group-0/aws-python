from multiprocessing.resource_sharer import stop
from urllib.request import urlretrieve
import os
import re

# Variables to use
amt_request_six_months = 0
amt_request_total = 0

# Paula's Code: the function to calculate the requests made in 6 months
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


# Irish's Code: function to get the percent of requests for a particular request code starting with string/char num (i.e., 4xx, 3xx)
def getRequestsPercent(file, num):
    # Get amt_request_total 
    global amt_request_total
    # Append first digit of request code we're looking for (num) to the regex pattern
    pattern = '.*\[([0-9]+/[a-zA-Z]+/[0-9]{4}):(.*) \-[0-9]{4}\] \"(.*)\" ' + num + '\d\d'
    amt_requests = 0

    # Loop through each line of file
    for line in file:
        # Read line of file one by one and temporarily store as one_line
        one_line = file.readline()

        # Use regex function re.search() to check if current line matches with regex pattern
        if re.search(pattern, one_line):
            # If it matches, increment amt_requests by 1
            amt_requests += 1
    
    # Get percentage; divide amt_requests by amt_request_total
    requests_percent = (amt_requests / amt_request_total) * 100
    return round(requests_percent, 2)
    

# Claire's Code: Fetching the log file from the Apache server
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log.txt'

# I used urlretrieve() and fetched a remote copy to save into the local file path
# left this line for better user experience
print("Loading Log File...")
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

print("\nDone Loading.")
os.system('clear')

# Paula's Code: Calculating the requests from the first 6 months
file = open(local_file, "r")
amt_request_six_months = getSixMonths(file)


# Irish's Code: Calculating total amount of requests

# opens & reads LOCAL_FILE as filehead file
with open(LOCAL_FILE, "r") as file:
    # stores each line in list & counts list length
    amt_request_total= len(file.readlines())


# Roxanna's Code: Outputting the requested amounts
print("Total amount of data requested within six months:", amt_request_six_months)

print("Total amount of requests for the total amount of time period:", amt_request_total)

print("Done analyzing log files.")


# Irish's Code: Percentage of total amount of bad requests
with open(LOCAL_FILE, "r") as file:
    print("Percent of Unsuccessful Requests: ", getRequestsPercent(file, "4"), "%")




