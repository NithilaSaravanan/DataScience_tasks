"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 5
To clean a given JSON file as per the conditions given in the assignment

"""
import json
from datetime import datetime as dt
from datetime import timezone
import argparse
import os.path as osp
import sys
from hw5.CleanJson import JsonCleaning


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help = 'Please enter the absolute path to the input file (the file to be cleansed)', default = 'nope')
    parser.add_argument('-o', help = 'Please enter the absolute path to the preferred output file (the cleaned file)', default = 'nope')
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit()
    
    input_path = args.i
    output_path = args.o
    if input_path == 'nope':
        print('No Input file path provided. Please try again \n')
        parser.print_help()
        sys.exit()
    if output_path == 'nope':
        print('No Output file path provided. Please try again \n')
        parser.print_help()
        sys.exit()


    #Reading the data and eliminating invlaid JSON before loading them up into a list
    data = []
    for line in open(input_path, 'r'):
        try:
            data.append(json.loads(line))
        except ValueError:
            pass

    clean_data = JsonCleaning(data)

    #Writing the clean data into a json file at the given location
    with open(output_path, 'w') as EndProduct:
        for x in clean_data:
            json.dump(x, EndProduct)
            EndProduct.write('\n')

    print(f'Successfully written {len(clean_data)} lines to {output_path}!')

if __name__ =='__main__':
    main()


