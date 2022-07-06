#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:27:27 2020

@author: nithila
"""

from bs4 import BeautifulSoup as bs
import requests as r
import json
import hashlib
import os.path as osp
import time

def getCache(url, cache_dir):
    hash_name = hashlib.sha1(url.encode('utf-8')).hexdigest()
    filename = osp.join(cache_dir, hash_name)
    contents = None
    if osp.exists(filename):
        return filename
    else:
        #print('from source')
        time.sleep(1) #Make sure to not hit the server too often too soon
        date_data = r.get(url)
        contents = date_data.text
        try:
            with open(filename, 'w') as f:
                f.write(contents)
        finally:
            f.close()
        return filename
        

def extractEntanglements(candidates,target_celeb_name):
    relationships = []
    
    for cand in candidates:
        if 'href' not in cand.attrs:
            
            continue
        
        href = cand['href']
        
        if href.startswith('/dating') and href!=target_celeb_name:
            name = href.replace('/dating/','')
            relationships.append(name)
    
    return relationships

def extractCelebs(target_celeb_file, target_celeb_name, file_name, celebrity):
    relationships = []
    try:    
        file = open(file_name, 'r')
        soup = bs(file, 'html.parser')
    except:
        print(f'Cannot open file for {celebrity}. Please delete file {file_name} and try again')
        
    finally:
        file.close()
        
    #Finding current relationship
    try:
        current_level_high = soup.find('h4','ff-auto-status')
        current_level_same = current_level_high.next_sibling
        current_candidates = current_level_same.find_all('a')
        relationships.extend(extractEntanglements(current_candidates, target_celeb_name))
        
        #Finding previous relationships
        prior_level_high = soup.find('h4', 'ff-auto-relationships')
        prior_level_same = prior_level_high.next_sibling
        
        while prior_level_same is not None and prior_level_same.name == 'p':
            prior_candidates = prior_level_same.find_all('a')
            prior_level_same = prior_level_same.next_sibling
            
            relationships.extend(extractEntanglements(prior_candidates, target_celeb_name))
    
    except:
        print(f'\n {celebrity} not found on WDW \n')
            
    return relationships
    
    
def main():
    outfile = "output.json"
    try:
        file = open('config-file.json','r')
        config = json.load(file)
    finally:
        file.close()
    
    cache_dir = config['cache_dir']
    celeb_list = config['target_people']
    
    final_dict = {}
    
    #print(config, cache_dir, celeb_list)
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
    

