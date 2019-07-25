import urllib.request
import json
import time
import datetime
import os


directory = "./url.json"

url = ""

with open(directory) as data_file:    
    data = json.load(data_file)


now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
for url_data in data:
    with open("./craw.log", "a") as myfile:
        start_time = time.time()
        file_link = url_data
        file_name = file_link.split("/")[4]
        urllib.request.urlretrieve(url+file_name, './key/'+file_name)
        myfile.write("URL : "+url+file_name+"\n")

        time.sleep(1)
        myfile.write("seconds : ")
        myfile.write(str(time.time() - start_time))
        myfile.write("\n")
        myfile.close()

with open("./craw.log", "a") as myfile:
    now = datetime.datetime.now()
    myfile.write("End : "+nowDatetime+"\n")
    myfile.write(len(data))

