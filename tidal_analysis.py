# import the modules we need
import pandas as pd
import datetime
import os
import numpy as np
#uptide can calculate the tidal constuents, but any nan (i.e missing data) must be removed prior to working out tidal constiuents.ArithmeticError
#uptide doesnt work - to fix!!
import uptide
import pytz
import math
#The `scipy.stats' module can do the linear regression to work out sea-level rise. You may find it easier to work out the rise per day and multiply by 365 to get metres per year.
from scipy import stats
import matplotlib.dates as mdates
import argparse
import contextlib
from pathlib import Path

#Important to note:
    #If you alter any function names in the main code, 
        #you can alter the name in the test file to match; 
        #however the rest of the test must remain unchanged. 
        #This will be checked.
    #If you wish to add more tests, please do, 
        #but place them in a separate file in the test 
        #directory. Remember to name the file 
        #test_something.py. You must also make sure the 
        #class name(s) are different to those in 
        #test/test_tides.py.
    #You can also add extra functionality, but the 
        #command-line interface must pass the tests set

#%%
tidal_data_temp = {} # dict to store the various years
def read_tidal_data(filename):
    input_file = Path("./data/"+filename+"/")
    for input_file in input_file.glob("*.txt"):
        print(f"{input_file.name}")
        year_key = input_file.name[:4]
        with open (input_file, 'r'):
            output_file = Path("./data/datacleaned/")
            output_file.mkdir(parents=True, exist_ok=True)
            partial_data = pd.read_csv(input_file, sep='\s+', skiprows=11, names=['Cycle', 'Date', 'Time', 'Surface Elevation', 'Residual'])
            partial_data['Cycle'] = partial_data['Cycle'].str.replace(')', '', regex=False).astype(int)
            #Combining Date & Time collumns and setting it as a datetime
            #Better to store as a datetime
            partial_data['Timestamp'] = pd.to_datetime(partial_data['Date'] + ' ' + partial_data['Time'])
        tidal_data_temp[year_key] = partial_data
    return tidal_data_temp

#Could give the user more choice
    #change the loop so it looks for a file matching the file names available
    #Rather than looking for a file matching the given file names
    #Gives the user more flexibility to add more files of data ..
        #Additionally list the folders available tbh
filename = input("Please choose a file between Whitby, Dover or Aberdeen:") 
filename = filename.lower()
while filename != "whitby" and filename != "dover" and filename != "aberdeen":
    print ("Make sure you have typed your file of choice in correctly")
    filename = input("Please choose a file between Whitby, Dover or Aberdeen:")
    filename = filename.lower()
#Making sure the data is differentiated
if filename == "dover":
    tidal_data = read_tidal_data("dover")
elif filename == "aberdeen":
    tidal_data = read_tidal_data("aberdeen")
elif filename == "whitby":
    tidal_data = read_tidal_data("whitby")
else:
    print ("There was an error!! Please check your input was correct and restart the program!")
#%%
#%%
def extract_single_year_remove_mean(year, data):
    #Extract a single year
    #Remove the mean..?!
    year = np.empty(0)
    year[tidal_data[year_select]]
    return 
year_select = int(input("Select which year you would like to extract:"))
while year_select != tidal_data.loc[Timestamp[year_select]]:
    year_select = input("That's not a valid year, please try again:")
#%%

def extract_section_remove_mean(start, end, data):

    return year_data


def join_data(data1, data2):

    return 

def sea_level_rise(data):

    return

def tidal_analysis(data, constituents, start_datetime):

    return

def get_longest_contiguous_data(data):

    return 


def main(args_list=None):

    parser = argparse.ArgumentParser(
                     prog="UK Tidal analysis",
                     description="Calculate tidal constiuents and RSL from tide gauge data",
                     )

    parser.add_argument("directory",
                    help="the directory containing txt files with data")
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help="Print progress")

    args = parser.parse_args(args_list)
    dirname = args.directory
    verbose = args.verbose

    print("Add your code here to do things!")
    

if __name__ == '__main__':
    main()
