#This is the client side code.
#The client here uses the RESTful APIs that are implemented in app3.py


import requests, json
from subprocess import call
import io

def printheaders(object):
    for elem in object.headers:
        print(elem, ":  ", object.headers[elem])

def printdir(object):
    for elem in dir(object):
        print(elem)

def content_type(object):
    return object.headers["Content-Type"]

def add_task(url, title):
    requests.post(url, json={"title":title})


#How do we open a connection tothe local server without explicitly turning it on thru the terminal
def main():
    #requests.post("http://localhost:5000/todo/api/v1.0/tasks", json={"title":"Eat dinner"})
    #requests.put("http://localhost:5000/todo/api/v1.0/tasks/3", json={"description":"Cook some food and eat at 8pm"})
    #requests.delete("http://localhost:5000/todo/api/v1.0/tasks/5")
    url = "http://www.cnn.com"
    #requests.post(url, json={"title":"Finish HW"})
    #requests.put(url + "/3", json={"done":True})
    
    #add_task(url, "Get food")
    r = requests.get(url)
    print(r.text)


    #running the text file from the server as a python application
    if(content_type(r)[0:9] == "text/html"):    
        myfile = open("newfile.txt", "w")
        myfile.write(r.text)
        myfile.close()

        with open("newfile.txt", "r") as f:
            call(["python", "newfile.txt"])

    
    
# The main script begins here:
main()
