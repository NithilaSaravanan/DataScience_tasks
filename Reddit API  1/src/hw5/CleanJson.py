"""
NAME: Nithilasaravanan Kuppan
ID: 260905444

COMP 598 HOMEWORK 5
Source code associated with clean.py script

"""
import json
from datetime import datetime as dt
from datetime import timezone

def JsonCleaning(data):
    inp_data = data
    for x in inp_data:
        x_cpy = {**x}#Creating a shallow copy to avoid issues in Python 3.8
        for key in x_cpy:
            if key=='title_text':
                x['title'] = x.pop('title_text')

    for x in inp_data:
        if 'title' not in x.keys():
            inp_data.remove(x)

    for x in inp_data:
        try:
            dt.strptime(x['createdAt'],"%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            inp_data.remove(x)

    for x in inp_data:
        temp_dt = dt.strptime(x['createdAt'], "%Y-%m-%dT%H:%M:%S%z")
        dttime = temp_dt.astimezone(timezone.utc)
        x['createdAt'] = dttime.isoformat()

    return(inp_data)





