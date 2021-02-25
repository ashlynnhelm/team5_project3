# Group Project #3 for TCMG 412
# Project description: Program will be parsing and analyzing log files.
# It will then show how many total requests have been made in the last year, current year, and how many total requests were made.
# Data will then printed to the user

# Steps: Check for local copy, retrieve log files from url, save to local disk, parse log file, print needed information


# Imports needed
import urllib.request
import os

# Checks for file on local disk
file_path = './https_access_log.txt'
existence = os.path.exists(file_path)

if existence == False:
    print("File does not exist, please wait for file to download...")
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'    # url to log files, NOT WORKING
    urllib.request.urlretrieve(url, './http_access_log.txt')        # retrieves the file and saves to local disL, NOT WORKING
    print("File has been downloaded, please wait one more moment for analysis...")
    file = open("http_access_log.txt")      # opens file
    data = file.read()      # reads file
    count1 = data.count("1994")     # finds occurrences of the year 1994
    count2 = data.count("1995")     # finds occurrences of the year 1995
    print(f"Time accessed in 1994: {count1}")
    print(f"Time accessed in 1995: {count2}")
    total = count1 + count2     # total number of occurrences
    print(f"Total times accessed: {total}")
else:
    print("Hello! The file exists and can be analyzed.")
    option = input("Would you like to analyze? Type Y/N: ")     # user input
    if option == "Y" or option == "y":
        print("One moment please...")
        file = open("https_access_log.txt")        # opens file
        information = file.read()       # reads file
        count1 = information.count("1994")     # finds occurrences of the year 1994
        count2 = information.count("1995")      # finds occurrences of the year 1995
        print(f"Accessed in 1994: {count1} times")
        print(f"Accessed in 1995: {count2} times")
        total = count1 + count2     # total number of occurrences
        print(f"Total times accessed: {total}")
    else:
        print('Option of "no" selected.')


