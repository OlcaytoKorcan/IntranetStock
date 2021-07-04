import base64
import requests
import os
import json
from art import text2art 


splash=text2art("OLCAYTO   POST-GET MANAGER \n")  

print (splash)

#the api endpoint for the job application. Send resumes and personal information to this URL via a POST request!
url = "http://10.240.1.73/api/Auth/Login"



#define what type of content this script is sending
headers = {
        'Content-Type': 'application/json',
    }


#the dictionary that will be serialized to JSON format and sent to Perka's server using their api endpoint
payload = {
        'userName' : 'admin',
        'password' : 'Adminuser_1234',
        
    }
#the final api request, which stores the response (hopefully a 200!)



response = requests.request("POST", url, json = payload, headers=headers)

response_token= ""


success_login = (response != True)


if (success_login):
    print("\n\n Başarılı şekilde bearer token verisi alınmıştır.\n\n\n")
    response_token = response.text

else:  print("Houston we have problem Call 911")




print("Geri dönen mesaj \n  {}\n\n\n " .format(response.text) )
print("Dönen Durum Kodu  {}\n\n\n" .format(response.status_code) )


