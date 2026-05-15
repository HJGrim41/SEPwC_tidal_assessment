# import the modules we need
import pandas as pd
import datetime
import os
import numpy as np
import uptide
import pytz
import math
from scipy import stats
import matplotlib.dates as mdates
import argparse
import contextlib
from pathlib import Path


#perform the analysis by the user suppying the folder
def read_tidal_data(filename):
    input_file = Path("./data/"+filename+"/")
    for input_file in input_file.glob("*.txt"):
        print(f"{input_file.name}")
        with open (input_file, 'r'):
            output_file = Path("./data/datacleaned/")
            output_file.mkdir(parents=True, exist_ok=True)
            tidaldata = pd.read_csv(input_file, sep='\s+', skiprows=11, names=['Cycle', 'Date', 'Time', 'Surface Elevation', 'Residual'])
            #Removing the ')' in the cycle column
            tidaldata['Cycle'] = tidaldata['Cycle'].str.replace(')', '', regex=False).astype(int)
            #Combining Date & Time collumns and setting it as a datetime
            tidaldata['Timestamp'] = pd.to_datetime(tidaldata['Date'] + ' ' + tidaldata['Time'])
    return tidaldata

filename = input("Please choose a file between Whitby, Dover or Aberdeen:")
filename = filename.lower()
while filename != "whitby" and filename != "dover" and filename != "aberdeen":
    print ("Make sure you have typed your file of choice in correctly")
    filename = input("Please choose a file between Whitby, Dover or Aberdeen:")
    filename = filename.lower()

def extract_single_year_remove_mean(year, data):

    return 


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
