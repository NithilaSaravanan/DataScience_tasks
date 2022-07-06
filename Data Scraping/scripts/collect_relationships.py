"""
NAME: Nithilasaravanan Kuppan
ID: 260905444
EMAIL: nithilasaravana.kuppan@mail.mcgill.ca

COMP 598 - HOMEWORK 7 - Task 1
"""

from bs4 import BeautifulSoup as bs
import requests as r
import json
import hashlib
import os.path as osp
import time
import argparse
import sys
import os

#Check if directory exists, else create it in script
def checkDir(cache_dir):
    try:
        os.makedirs(cache_dir)
        print(f'\n Created {cache_dir}')
    except FileExistsError:
        pass

#Function to ensure files are cached and if cache exists, program uses local file
def getCache(url, cache_dir):
    hash_name = hashlib.sha1(url.encode('utf-8')).hexdigest()
    filename = osp.join(cache_dir, hash_name)
    contents = None

    if osp.exists(filename):
        return filename
    else:
        time.sleep(1) #Not to overburden server by continuous requests
        date_data = r.get(url)
        contents = date_data.text
        with open(filename,'w') as f:
            f.write(contents)
        return filename


#Function to extract the exact people from a set of possible people (with whom target was in a relationship with)
def extractEntanglements(candidates, target_celeb_name):
    relationships = []

    for cand in candidates:
        if 'href' not in cand.attrs:
            continue
        
        href = cand['href']

        if href.startswith('/dating') and href!=target_celeb_name:
            name = href.replace('/dating/','')
            relationships.append(name)

    return relationships

#Function to extract all possible relationships associated with the target celebrity
def extractCelebs(target_celeb_file, target_celeb_name, file_name, celebrity):
    relationships = []
    try:
        file_n = open(file_name,'r')
        soup = bs(file_n, 'html.parser')
    except:
        print(f'Cannot open file for {celebrity}. Please delete file {file_name} and try again')
    finally:
        file_n.close()
    #Figuring out current relationship
    try:
        current_level_high = soup.find('h4','ff-auto-status')
        current_level_same = current_level_high.next_sibling
        current_candidates = current_level_same.find_all('a')
        relationships.extend(extractEntanglements(current_candidates, target_celeb_name))

    #Figuring out previous relationship(s)
        prior_level_high = soup.find('h4', 'ff-auto-relationships')
        prior_level_same = prior_level_high.next_sibling
        while prior_level_same is not None and prior_level_same.name == 'p':
            prior_candidates = prior_level_same.find_all('a')
            prior_level_same = prior_level_same.next_sibling
            relationships.extend(extractEntanglements(prior_candidates, target_celeb_name))

    except:
        print(f'\n {celebrity} not found on WDW')

    return relationships

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help = 'Path to the configuration file to be used by this script', default = 'nope')
    parser.add_argument('-o',help = 'Path to the output file to store the JSON results in', default = 'nope')
    
    try:
        args = parser.parse_args()
    except:
        print('\n Please try again \n')
        parser.print_help()
        sys.exit()

    outfile = args.o
    conf = args.c

    if (outfile == 'nope' or  conf =='nope'):
        print('\n Missing parameters. Please try again \n')
        parser.print_help()
        sys.exit()

    try:
        file_c = open(conf,'r')
        config = json.load(file_c)
    finally:
        file_c.close()

    cache_dir = config['cache_dir']
    checkDir(cache_dir) #Check if directory exists
    celeb_list = config['target_people']
    final_dict = {}

    for i in range(len(celeb_list)):
        target_celeb_name = "/dating/"+celeb_list[i]
        url = "https://www.whosdatedwho.com/dating/"+celeb_list[i]
        file_name = getCache(url, cache_dir)
        celeb = extractCelebs(celeb_list[i], target_celeb_name, file_name, celeb_list[i])

        if celeb_list[i] not in final_dict:
            final_dict.update({celeb_list[i]: celeb})

    try:
        with open(outfile, 'w') as out:
            json.dump(final_dict, out, indent = 4)
    finally:
        out.close()

    print(f'\n Output written to {outfile}')


if __name__ == '__main__':
    main()


