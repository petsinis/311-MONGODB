from flask import Flask
from flask import jsonify
from flask import request

from pymongo import MongoClient
from bson.objectid import ObjectId

from queries import *

import datetime
from dateutil.parser import parse

import json
import constant
from check_insert import check_row

client = MongoClient()
db = client.chicago_incidents



app = Flask(__name__)


def not_date_given(date):
    context = {'error': "Sorry: Incorrect date format for: "+str(date)}  
    return(context)

def floaturn(num):
    if((str(num)=='None')|(str(num)=='')):
        return None
    num=str(num)
    try:
        float(num)
        return float(num)
    except ValueError:
        return False

def not_float_given(num):
    context = {'answer_list': "Sorry: Incorrect numeric format for: "+str(num)} 
    return(context)


@app.route("/query1", methods=["GET"])
def _query1():
    date1 = request.args.get("date1")
    date2 = request.args.get("date2")
    
    #Check date format
    try:
        d1=datetime.datetime.strptime(date1, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date1)))
    try:
        d2=datetime.datetime.strptime(date2, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date2)))

    d1=datetime.datetime.strptime(str(d1), '%Y-%m-%dT%H:%M:%S.%f')
    d2=datetime.datetime.strptime(str(d2), '%Y-%m-%dT%H:%M:%S.%f')
    
    q1=query1(db, d1, d2)

    return(q1)
    
@app.route("/query2", methods=["GET"])
def _query2():
    date1 = request.args.get("date1")
    date2 = request.args.get("date2")
    type_of_req = request.args.get("type_of_req")
    
    #Check date format
    try:
        d1=datetime.datetime.strptime(date1, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date1)))
    try:
        d2=datetime.datetime.strptime(date2, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date2)))

    d1=datetime.datetime.strptime(str(d1), '%Y-%m-%dT%H:%M:%S.%f')
    d2=datetime.datetime.strptime(str(d2), '%Y-%m-%dT%H:%M:%S.%f')
    
    q2=query2(db, d1, d2, type_of_req)

    return(q2)    

@app.route("/query3", methods=["GET"])
def _query3():
    date = request.args.get("date")
    
    #Check date format
    try:
        d=datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date)))

    d=datetime.datetime.strptime(str(d), '%Y-%m-%dT%H:%M:%S.%f')

    q3=query3(db, d)

    return(q3)   

@app.route("/query4", methods=["GET"])
def _query4():
    type_of_req = request.args.get("type_of_req")
    
    q4=query4(db, type_of_req)

    return(q4)

@app.route("/query5", methods=["GET"])
def _query5():
    date1 = request.args.get("date1")
    date2 = request.args.get("date2")
    
    #Check date format
    try:
        d1=datetime.datetime.strptime(date1, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date1)))
    try:
        d2=datetime.datetime.strptime(date2, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date2)))

    d1=datetime.datetime.strptime(str(d1), '%Y-%m-%dT%H:%M:%S.%f')
    d2=datetime.datetime.strptime(str(d2), '%Y-%m-%dT%H:%M:%S.%f')
    
    q5=query5(db, d1, d2)

    return(q5) 

@app.route("/query6", methods=["GET"])
def _query6():
    date = request.args.get("date")
    x1 = floaturn(request.args.get("x1"))
    x2 = floaturn(request.args.get("x2"))
    y1 = floaturn(request.args.get("y1"))
    y2 = floaturn(request.args.get("y2"))
    
    #Check float format
    count=1
    for x in list([x1, x2, y1, y2]):
        if(x==False):
            return(not_float_given(request.args.get("x"+str(count))))
        count=count+1
        
    #Check date format    
    try:
        d=datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date)))

    d=datetime.datetime.strptime(str(d), '%Y-%m-%dT%H:%M:%S.%f')
    
    q6=query6(db, d, x1, x2, y1, y2)

    return(q6)  

@app.route("/query7", methods=["GET"])
def _query7():
    date = request.args.get("date")
    
    #Check date format
    try:
        d=datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        return(json.dumps(not_date_given(date)))

    d=datetime.datetime.strptime(str(d), '%Y-%m-%dT%H:%M:%S.%f')

    q7=query7(db, d)

    return(q7)  

@app.route("/query8", methods=["GET"])
def _query8():
    q8=query8(db)
    return(q8)  

@app.route("/query9", methods=["GET"])
def _query9():
    q9=query9(db)
    return(q9)  

@app.route("/query10", methods=["GET"])
def _query10():
    q10=query10(db)
    return(q10)  


@app.route("/query11", methods=["GET"])
def _query11():
    name = request.args.get("name")
    q11=query11(db, name)
    return(q11)  


@app.route("/insert_new_incident", methods=["POST"])
def _insert_new_incident():
    row=request.json
    
    #Name of fields
    names=(list(row.keys()))
    
    #Check type of request
    type_of_req = row.get("type_of_service_request")
    if((type_of_req==None)|(str(type_of_req) not in constant.types_of_incidents)):
        return({'You must choose a type_of_service_request from: ': str(constant.types_of_incidents)} ) 
    
    date1 = str(row.get("creation_date"))
    date2 = str(row.get("completion_date"))

    #Check date format of creation and completion date
    try:
        d1=datetime.datetime.strptime(date1, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
        row['creation_date']=datetime.datetime.strptime(str(d1), '%Y-%m-%dT%H:%M:%S.%f')
    except ValueError:
        try:
            d1=datetime.datetime.strptime(date1, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            row['creation_date']=datetime.datetime.strptime(str(d1), '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            return(json.dumps(not_date_given(date1)))
    if(date2!=None):
        try:
            d2=datetime.datetime.strptime(date2, '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%f')
            row['completion_date']=datetime.datetime.strptime(str(d2), '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            try:
                d2=datetime.datetime.strptime(date2, '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                row['completion_date']=datetime.datetime.strptime(str(d2), '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                return(json.dumps(not_date_given(date2)))
    
    #Convert fields to date/int/floats/string
    row=check_row(row, names)
    
    #Insert the new incident
    if("_id" not in names):
        res=db.requests.insert_one(row)
    else:
        if not (ObjectId.is_valid(row["_id"])):
            return({"error": "Not valid ObjectId "+str(row["_id"])})
            
        row["_id"] = ObjectId(row["_id"])
        res=db.requests.replace_one({"_id":row["_id"]}, row, upsert=True)

    
    return({"Insertion finished":" "+str(res)})  


@app.route("/upvote/<request_id>", methods = ["POST"])
def upvote_request(request_id):
    
    # take citizen id from json payload
    # do upvote logic  <= 1000, 2ble upvoting
    citizen_id = request.json.get("citizen_id")
    
    if not (ObjectId.is_valid(request_id)) or not (ObjectId.is_valid(citizen_id)):
        return jsonify({"error": "Not valid ObjectIds"})
    

    req_id = ObjectId(request_id)
    cit_id = ObjectId(citizen_id)

    result1 = db.requests.find_one({"_id": req_id})
    result2 = db.citizens.find_one({"_id": cit_id})

    if not result1:
        return jsonify({"error": "Request not found"})
    if not result2:
        return jsonify({"error": "Citizen not found"})
    

    # check if request already upvoted by citizen
    result = db.requests.aggregate([
        {"$match": {"_id": req_id}}, 
        {"$match": {"$expr": {"$in": [cit_id, {"$cond": {"if": {"$ifNull": ["$upvoted_by", False]}, "then": "$upvoted_by", "else": []}}]}}}, 
    ])
    
    already_upvoted = len(list(result))
    
    if already_upvoted:
        return jsonify({"error": "Request already upvoted by this citizen"})

    # check if citizen's number of upvotes hit threshold
    result = db.citizens.aggregate([
        {"$match": {"_id": cit_id}}, 
        {"$project": {"_id": 0, "num_of_upvotes": {"$cond": {"if": {"$ifNull": ["$upvotes", False]}, "then": {"$size": "$upvotes"}, "else": 0}}}}
    ])

    num_of_upvotes = list(result)[0].get("num_of_upvotes")

    if num_of_upvotes > 999:
        return jsonify({"error": "Citizen has reached the maximum number of upvotes"})
    
    
    result1 = db.citizens.update_one({"_id": cit_id}, {"$addToSet": {"upvotes": req_id}})
    result2 = db.requests.update_one({"_id": req_id}, {"$addToSet": {"upvoted_by": cit_id}})
    
    return jsonify({"sucess": "Upvoting successful"})


@app.route("/downvote/<request_id>", methods = ["POST"])
def downvote_request(request_id):
    citizen_id = request.json.get("citizen_id")
    
    if not (ObjectId.is_valid(request_id)) or not (ObjectId.is_valid(citizen_id)):
        return jsonify({"error": "Not valid ObjectIds"})
    

    req_id = ObjectId(request_id)
    cit_id = ObjectId(citizen_id)

    result1 = db.requests.find_one({"_id": req_id})
    result2 = db.citizens.find_one({"_id": cit_id})

    if not result1:
        return jsonify({"error": "Request not found"})
    if not result2:
        return jsonify({"error": "Citizen not found"})
    

    
    result1 = db.citizens.update_one({"_id": cit_id}, {"$pullAll": {"upvotes": [req_id]}})
    result2 = db.requests.update_one({"_id": req_id}, {"$pullAll": {"upvoted_by": [cit_id]}})

    db.citizens.update_one({"_id": cit_id, "upvotes": []}, {"$unset": {"upvotes": ""}})
    db.requests.update_one({"_id": req_id, "upvoted_by": []}, {"$unset": {"upvoted_by": ""}})
    
    return jsonify({"sucess": "Downvoting successful"})

