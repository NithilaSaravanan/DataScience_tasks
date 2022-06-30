"""

This piece of code does an intrinsic analysis of the transcripts of the dialogues in the show "My Little Pony". The transcripts have been downloaded from Kaggle. 

This code stiched together some functions to throw out the final analysis results in a JSON format, eithr printed or to a file.

AUTHOR: Nithilasaravanan Kuppan
MCGILL ID: 260905444
EMAIL: nithilasaravana.kuppan@mail.mcgill.ca

"""

from hw3.data_prep import prepareData
from hw3.verbosity import calc_verbosity
from hw3.mentions import calc_mentions
from hw3.follow import calc_follow
from hw3.nondict import calc_nondict
import argparse
import json
import sys
import os.path as osp

this_dir = osp.dirname(__file__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help = 'Enter the filename that will be used while creating the output file', default = 'nope')
    parser.add_argument('src_file', help = 'Enter the path to clean_dialog.csv - This is required for the program to run')
    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    src_file = args.src_file
    words_file = osp.join(this_dir,'..','data','words_alpha.txt')

    output_file = args.o
    
    #Call all functions and get the corresponding outputs
    data = prepareData(src_file, words_file)
    js_verbosity = calc_verbosity(data)
    js_mentions = calc_mentions(data)
    js_follow = calc_follow(data)
    js_nondict = calc_nondict(data)
    
    #Join all outputs in a dict together
    final_result = {"verbosity":js_verbosity,"mentions":js_mentions,"follow_on_comments":js_follow,"non_dictionary_words":js_nondict}
    
    #To determine whether print the result out or write it to a file
    if (output_file != 'nope'):
        with open(output_file,'w') as outfile:
            json.dump(final_result, outfile, indent = 4)
    else:
        print(json.dumps(final_result, indent = 4))

if __name__=='__main__':
    main()
