import json

   
def query1(db, date1, date2):
    q1=db.requests.aggregate([
        {"$match":{"$and":[
            {"creation_date":{"$gte":date1}},
            {"creation_date":{"$lte":date2}}]}},
        {"$group":{"_id":"$type_of_service_request","total":{"$sum":1}}},{"$sort":{"total":-1}}])
    q1=list(q1)
    return(json.dumps(q1))    
    
    
#q1=query1(db,datetime.datetime.strptime("2015-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'),
               #datetime.datetime.strptime("2016-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'))    



def query2(db, date1, date2, type_of_req):
    q2=db.requests.aggregate([
        {"$match":{"$and":[{"creation_date":{"$gte":date1}},
                       {"creation_date":{"$lte":date2}},
                       {"type_of_service_request":type_of_req}]}},
        {"$group":{"_id":"$creation_date","total":{"$sum":1}}},{"$sort":{"_id":1}}])
    q2=list(q2)
    for ret in q2:
        ret['_id']=(str(ret['_id']))
    return(json.dumps(q2)) 
    

#q2=query2(db,datetime.datetime.strptime("2015-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'),
               #datetime.datetime.strptime("2016-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'),
               #"Tree Trim")    



def query3(db, date):
    q3=db.requests.aggregate([
        {"$match": {"$and": [{"creation_date": date}, {"zip_code": {"$ne": ""}}]}}, 
        {"$group": {"_id": {"zip": "$zip_code", "type": "$type_of_service_request"}, "hits": {"$sum": 1}}}, 
        {"$sort": {"_id.zip": -1, "hits": -1}}, 
        {"$group": {"_id": "$_id.zip", "per_zip": {"$push": {"type": "$_id.type", "hits": "$hits"}}}}, 
        {"$project": {"_id": 0, "zip_code": "$_id", "topThreeTypes": {"$slice": ["$per_zip", 0, 3]}}} 
    ])
    q3=list(q3)
    return(json.dumps(q3)) 
    

#q3=query3(db,datetime.datetime.strptime("2015-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'))



def query4(db, type_of_req):
    q4=db.requests.aggregate([
        {"$match":{"type_of_service_request":type_of_req}},
        {"$group":{"_id":"$ward","total":{"$sum":1}}},
        {"$sort":{"total":-1}},{ "$limit" : 3 }])
    q4=list(q4)
    return(json.dumps(q4)) 

#q4=query4(db,"Tree Trim")



def query5(db, date1, date2):
    q5=db.requests.aggregate([
        {"$match":{"$and":[{"creation_date":{"$gte":date1}},
                       {"completion_date":{"$lte":date2}}]}}, 
        {"$group":{"_id":{"type":"$type_of_service_request"},
                 "avgComplDate": {"$avg": {"$divide":[{"$subtract":[ "$completion_date", "$creation_date" ]},1000*24*60*60]}}}}])
    q5=list(q5)
    return(json.dumps(q5)) 

#q5=query5(db,datetime.datetime.strptime("2015-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'),
               #datetime.datetime.strptime("2016-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'))  




def query6(db, date, x1, x2, y1, y2):
    q6=db.requests.aggregate([
        {"$match": {"$and": [{"location": {"$geoWithin": {"$box": [[x1, x2], [y1, y2]]}}}, 
                             {"creation_date": {"$eq": date}}]}}, 
        {"$group": {"_id": "$type_of_service_request", "count": {"$sum": 1}}}, 
        {"$sort": {"count": -1}}, 
        {"$limit": 1}
    ])
    q6=list(q6)
    return(json.dumps(q6)) 

#q6=query6(db,datetime.datetime.strptime("2015-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'),
             #-88.023555, 41.548756, -87.770997, 41.886956)  




def query7(db, date):
    q7=db.requests.aggregate([
        {"$match": {"creation_date": {"$eq": date}}}, 
        {"$match": {"upvoted_by": {"$exists": "true"}}}, 
        {"$project": {"_id": 1, "upvotes": {"$size": "$upvoted_by"}}}, 
        {"$sort": {"upvotes": -1}}, {"$limit": 50}
    ])
    q7=list(q7)
    for ret in q7:
        ret['_id']=(str(ret['_id']))
    return(json.dumps(q7)) 

#q7=query7(db,datetime.datetime.strptime("2015-01-01T00:00:00.000", '%Y-%m-%dT%H:%M:%S.%f'))



def query8(db):
    q8=db.citizens.aggregate([
        {"$match": {"upvotes": {"$exists": "true"}}}, 
        {"$project": {"name": 1, "num_of_upvotes": {"$size": "$upvotes"}}}, 
        {"$sort": {"num_of_upvotes": -1}}, 
        {"$limit": 50}
    ])
    q8=list(q8)
    for ret in q8:
        ret['_id']=(str(ret['_id']))
    return(json.dumps(q8)) 

#q8=query8(db)

    
    
     

def query9(db):
    q9=db.requests.aggregate([ 
        {"$project": {"_id": 1, "ward": 1, "upvoted_by": 1}},      
        {"$unwind": "$upvoted_by" },
        #{"$match": {"upvoted_by": {"$ne": None}}}, 
        {"$group":{"_id":{"up":"$upvoted_by","ward": "$ward"}}},
        {"$match": {"_id.ward": {"$ne": None}}}, 
        {"$group":{"_id":"$_id.up","total":{"$sum":1}}},
        {"$sort": {"total": -1}}, 
        {"$limit": 50}
    ])    
    q9=list(q9)
    for ret in q9:
        ret['_id']=(str(ret['_id']))
    return(json.dumps(q9))


#q9=query9(db)

    
    
    
    
def query10(db):
    q10=db.citizens.aggregate([
        {"$group": {"_id": "$telephone", "persons": {"$sum": 1}, "requests": {"$push": "$upvotes"}}}, 
        {"$match": {"persons": {"$gte": 2}}}, 
        {"$unwind": "$requests" },
        {"$unwind": "$requests" },
        {"$group": {"_id": {"tel":"$_id","requests":"$requests"}, "num_dup": {"$sum": 1}}},
        {"$project": {"_id": 0, "telephone": "$_id.tel", "request": "$_id.requests", "num_dup": "$num_dup"}},
        {"$match": {"num_dup": {"$gte": 2}}}, 
    ])
    q10=list(q10)
    for ret in q10:
        ret['request']=(str(ret['request']))
    return(json.dumps(q10))


#q10=query10(db)
 
    
    
    
    
def query11(db, name):
    q11=db.citizens.aggregate([
        {"$match": {"name": name}}, 
        {"$lookup": {"from": "requests", "localField": "upvotes", "foreignField": "_id", "as": "upvotes"}}, 
        {"$project": {"_id": 1, "name": 1, "wards": "$upvotes.ward"}}, 
        {"$project": {"_id": 1, "name": 1, "wards": {"$setIntersection": ["$wards"]}}} 
    ])
    q11=list(q11)
    for ret in q11:
        ret['_id']=(str(ret['_id']))
    return(json.dumps(q11))

#q11=query11(db, "Norma Fisher")
         
    
    
    



