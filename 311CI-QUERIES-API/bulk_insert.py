import datetime
import constant
import fieldnames
import re
import math



coordinates_pattern = re.compile(r"^[.0-9-]+$")

def fix_row(row, type, names):
    
    #location ...TODO
    if re.match(coordinates_pattern, str(row["longitude"])) and re.match(coordinates_pattern, str(row["latitude"])):
        row["location"] = {"type": "Point", "coordinates": [float(row["longitude"]), float(row["latitude"])]}
    
    #remove latitude, longitude
    del row["latitude"]
    del row["longitude"]
    
    for k in list(set(names) & set(fieldnames.int_type)):
        if(row[k]!=""):
            row[k]=int(math.ceil(float(row[k])))
        else:
            del row[k]
    for k in list(set(names) & set(fieldnames.float_type)):
        if(row[k]!=""):
            row[k]=float(row[k])
        else:
            del row[k]        
    
    for k in list(set(names) - set(fieldnames.checked_type)):
        if(row[k]==""):
            del row[k]
    
    return row



