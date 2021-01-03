import datetime
import constant
import fieldnames
import re
import math



coordinates_pattern = re.compile(r"^[.0-9-]+$")

def check_row(row, names):
    
    #location
    if re.match(coordinates_pattern, str(row["longitude"])) and re.match(coordinates_pattern, str(row["latitude"])):
        row["location"] = {"type": "Point", "coordinates": [float(row["longitude"]), float(row["latitude"])]}

    #remove latitude, longitude
    del row["latitude"]
    del row["longitude"]
    
    for k in list(set(names) & set(fieldnames.int_type)):
        if(row[k]!=""):
            try:
                row[k]=int(math.ceil(float(row[k])))
            except ValueError:
                return({'answer_list': "Sorry: Incorrect integer format for: "+str(row[k])} )    
        else:
            del row[k]
    for k in list(set(names) & set(fieldnames.float_type)):
        if(row[k]!=""):
            try:
                row[k]=float(row[k])
            except ValueError:
                return({'answer_list': "Sorry: Incorrect float format for: "+str(row[k])} )        
        else:
            del row[k]        
    
    for k in list(set(names) - set(fieldnames.checked_type)):
        if(row[k]==""):
            del row[k]

    return row



