from multiprocessing.resource_sharer import stop
from urllib.request import urlretrieve
import os

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

# Make amt_bad_requests variable to keep track of total amount of 4xx status codes
amt_bad_requests = 0
# Open file
with open(LOCAL_FILE, "r") as file:
    
    # Get index where status code is
    for line in file:
        # Reads line
        one_line = file.readline()
        # Stores each value in list and splits it by space
        one_line_list = one_line.split(" ")
        # print(one_line_list)

        # Skips any lines in log file that are not the same length 
        if len(one_line_list) == 10:
            # Request code from second to last index of list
            code = one_line_list[len(one_line_list) - 2]

            # If code at first index is equal to 4; which indicates a bad request
            if code[0] == "4":
                # Increment amt_bad_requests + 1
                amt_bad_requests += 1

# Get percentage; divide amt_bad_requests by total amount of requests found in previous lab #3
bad_requests_percent = (amt_bad_requests / amt_request_total) * 100
print("Total amount of bad requests: ", amt_bad_requests)
print("Percent of bad requests: ", round(bad_requests_percent, 2), "%")



#Code for least Requested File: 
amt_least_requested = 0

with open(local_file,"r") as file:
    amt_least_requested= len(file.readlines())

line = ""
list = line.split(',')
fileInfo = list[1].split(' ')

fileName = fileInfo[1]

filesCount = { }

#if (fileName exists within filesCount):
  #find file + add count
#else:
 # add file to filesCount and default to 1
