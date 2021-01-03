import requests
import json

def request_query1(date1, date2):
    r = requests.get("http://127.0.0.1:5000/query1", params = {"date1": str(date1), "date2": str(date2)})
    return(r)

def request_query2(date1, date2, type_of_req):
    r = requests.get("http://127.0.0.1:5000/query2", params = {"date1": date1, "date2": date2, "type_of_req": type_of_req})
    return(r)

def request_query3(date):
    r = requests.get("http://127.0.0.1:5000/query3", params = {"date": date})
    return(r)    

def request_query4(type_of_req):
    r = requests.get("http://127.0.0.1:5000/query4", params = {"type_of_req": type_of_req})
    return(r)    

def request_query5(date1, date2):
    r = requests.get("http://127.0.0.1:5000/query5", params = {"date1": date1, "date2": date2})
    return(r)  

def request_query6(date, x1, x2, y1, y2):
    r = requests.get("http://127.0.0.1:5000/query6", params = {"date": date, "x1": x1, "x2": x2, "y1": y1, "y2": y2})
    return(r)  

def request_query7(date):
    r = requests.get("http://127.0.0.1:5000/query7", params = {"date": date})
    return(r)  

def request_query8():
    r = requests.get("http://127.0.0.1:5000/query8")
    return(r)  

def request_query9():
    r = requests.get("http://127.0.0.1:5000/query9")
    return(r)  

def request_query10():
    r = requests.get("http://127.0.0.1:5000/query10")
    return(r)  

def request_query11(name):
    r = requests.get("http://127.0.0.1:5000/query11", params = {"name": name})
    return(r)  

def insert_new_incident(new_inc):
    r = requests.post("http://localhost:5000/insert_new_incident", headers = {"Content-Type": "application/json"}, 
                      data = json.dumps(new_inc))
    return(r)

def upvote_request(citizen_id, request_id):
    #request_id = "5feefde8f884f9ccd91e3094"
    #citizen_id = "5ff082b06d74c9911f89577e"
    
    r = requests.post(f"http://localhost:5000/upvote/{request_id}", 
                      headers = {"Content-Type": "application/json"}, data = json.dumps({"citizen_id": citizen_id}))
    return(r)

def downvote_request(citizen_id, request_id):
    #request_id = "5feefe02f884f9ccd91ebfd5"
    #citizen_id = "5ff082b06d74c9911f89577e"
    
    r = requests.post(f"http://localhost:5000/downvote/{request_id}", 
                      headers = {"Content-Type": "application/json"}, data = json.dumps({"citizen_id": citizen_id}))

    return(r)



choice=0
while((int(choice)<1)|(int(choice)>14)):
    print("If you want to chose a query select a number from 1 to 11.")
    print("If you want to insert a new incident select 12.")
    print("If you want to upvote a request on a citizen select 13.")
    print("If you want to downvote a request on a citizen select 14.")
    print()
    choice = int(input("Your choice: "))

if(choice==1):
    print("Your chosen query: Find the total requests per type that were created within a specified time range and sort them in a descending order.")
    print()
    print("The date range is [date1, date2].")
    date1 = input("Choose date1:")
    date2 = input("Choose date2:")
    print()
    print("Running query 1 with date range ["+str(date1)+","+str(date2)+"].")
    print()
    r=request_query1(date1, date2)
    print()
    print(r.text)
    
elif(choice==2):
    print("Your chosen query: Find the number of total requests per day for a specific request type and time range.")
    print()
    print("The date range is [date1, date2] for the selected type_of_req")
    date1 = input("Choose date1:")
    date2 = input("Choose date2:")
    type_of_req = input("Choose type_of_req:")
    print()
    print("Running query 2 with date range ["+str(date1)+","+str(date2)+"] for the "+str(type_of_req)+" type of request.")
    print()
    r=request_query2(date1, date2, type_of_req)
    print()
    print(r.text)
    
elif(choice==3):
    print("Your chosen query: Find the three most common service requests per zipcode for a specific day.")
    print()
    date = input("Choose a date:")
    print()
    print("Running query 3 with date "+str(date)+".")
    print()
    r=request_query3(date)
    print()
    print(r.text)
    
elif(choice==4):
    print("Find the three least common wards with regards to a given service request type.")
    print()
    type_of_req = input("Choose type of service request:")
    print()
    print("Running query 4 with "+str(type_of_req)+" type of request.")
    print()
    r=request_query4(type_of_req)
    print()
    print(r.text)
    
elif(choice==5):
    print("Your chosen query: Find the average completion time per service request for a specific date range.")
    print()
    print("The date range is [date1, date2].")
    date1 = input("Choose date1:")
    date2 = input("Choose date2:")
    print()
    print("Running query 5 with date range ["+str(date1)+","+str(date2)+"].") 
    print()
    r=request_query5(date1,date2)
    print()
    print(r.text)
    
elif(choice==6):
    print("Your chosen query: Find the most common service request in a specified bounding box for a specific day.")
    print()
    print("The bounding box can be represented by 2 points:")
    print("---> The down left point of the box (x1,x2).")
    print("---> The up right point of the box (y1,y2).")
    print()
    date = input("Choose a date:")
    print()
    print("For the down left point:")
    x1 = input("Choose x1:")
    x2 = input("Choose x2:")
    print()
    print("For the up right point:")
    y1 = input("Choose y1:")
    y2 = input("Choose y2:")
    print()
    print("Running query 6 with bounding box represented by ("+str(x1)+","+str(x2)+") and ("+str(y1)+","+str(y2)+") for date "+str(date)+".")     
    print()
    r=request_query6(date, x1, x2, y1, y2)
    print()
    print(r.text)

elif(choice==7):
    print("Your chosen query: Find the fifty most upvoted service requests for a specific day.")
    print()
    date = input("Choose a date:")
    print()
    print("Running query 7 with date "+str(date)+".")   
    print()
    r=request_query7(date)
    print()
    print(r.text)
    
elif(choice==8):
    print("Your chosen query: Find the fifty most active citizens, with regard to the total number of upvotes.")
    print()
    print("Running query 8.")  
    print()
    r=request_query8()
    print()
    print(r.text)
    
elif(choice==9):
    print("Your chosen query: Find the top fifty citizens, with regard to the total number of wards for which they have upvoted an incidents.")
    print()
    print("Running query 9.")  
    print()
    r=request_query9()
    print()
    print(r.text)
    
elif(choice==10):
    print("Your chosen query: Find all incident ids for which the same telephone number has been used for more than one names.")
    print()
    print("Running query 10.")  
    print()
    r=request_query10()
    print()
    print(r.text)
    
elif(choice==11):
    print("Your chosen query: Find all the wards in which a given name has casted a vote for an incident taking place in it.")
    print()
    name = input("Choose a name:")
    print()
    print("Running query 11 for name"+str(name)+".") 
    print()
    r=request_query11(name)
    print()
    print(r.text)
    
elif(choice==12):
    print("You chose to insert a new incident")
    print()
    name = input("Write the name of the json file that contains the new incident: ")
    print()
    print("Inserting a new incident:") 
    
    name='new_incident.txt'
    with open(str(name), 'r') as f:
        new_inc = json.load(f)
        print()
        print(new_inc)
        print()
        r=insert_new_incident(new_inc)
        print()
        print(r.text)
        
elif(choice==13):
    #citizen_id = "5fedbc57d6a49f481606a1fa"    
    #request_id = "5fedb37ed6a49f4816c58fad"
    print("You chose to upvote an incident for a given citizen")
    print()
    citizen_id = input("Write the id of the citizen: ")
    request_id = input("Write the id of the incident: ")
    print()
    print("Upvoting incident "+str(request_id)+" for citizen "+str(citizen_id))
    print()
    r=upvote_request(str(citizen_id), str(request_id))
    print()
    print(r.text)
    
else:
    #citizen_id = "5fedbc57d6a49f481606a1fa" 
    #request_id = "5fedb37ed6a49f4816c58fad"       
    print("You chose to downvote an incident for a given citizen")
    print()
    citizen_id = input("Write the id of the citizen: ")
    request_id = input("Write the id of the incident: ")
    print()
    print("Downvoting incident "+str(request_id)+" for citizen "+str(citizen_id))
    print()
    r=downvote_request(citizen_id, request_id)
    print()
    print(r.text)    
    
    
    
    
    
    
    