from email import header
import json
from lib2to3.pgen2 import token
from wsgiref import headers
import requests
import urllib.parse
from requests.structures import CaseInsensitiveDict
data ={
    "userName" : 'admin',
    "password" : 'Adminuser_1234',
    
    }



def LoginAPIMikro():
    ##Parameters##
        print("API connection has initilazed")
        url = "http://10.240.1.73/api/Auth/Login"
        response = requests.request("POST", url, json = data, verify=True)
        success_login = (response != True)
        if (success_login):
            print("\n\nBaşarılı şekilde bearer token verisi alınmıştır.\n\n\n")
            global response_token
            response_token = response
        else:  print("Houston we have problem Call 911")
        print("Dönen Durum Kodu  {}\n\n\n" .format(response.status_code) )
        response_token =response_token.json()
        print(response_token)


def StockUpdate():
    print("Stock Update has been initialized")
    url= "http://10.240.1.73/api/Stock/GetStok/1"
    headers = CaseInsensitiveDict() 
    headers["Authorization"]=response_token["token"]
    cookies = {'.AspNetCore.Identity.Application' : 'CfDJ8HcURbtv17VNmrVBiZiBEKMNNeGMErVwzTCnI0bModBTHRbgMVjo4cQeMVf5uJxRwP62W607U6wRHyIMYfWT9XWBf71j703pkKLhd_Bptj6C1XGAg2MkVomwsPRCVmIr2IftgGK4_ESuAvpvEMSF53i55xqzrsd-9rROtt2iDArXrimMKsbooweuNqvDA6U-lzqWy0cT1eKSrF-3lW9JGSflRqtu8aJhryX3MDGPe1skhGkHvxJdc-NTHpTGlIeMvDQZtuQPwdheB0frnF4BJKeWdpXfAF3TFEwTmD8bGpgD37Bp-osUJRYk1z3_mJXpfjzr9OreA4krwIR0OTQFHWD08G2sSZtX4YFeNqqDWCamGv1WFDlHr_00FwlB0_SFSqechJ-2C4QO1o2fixXSmgj-gQaOZEIRaAuxubXxLKEp3U3-CbaJAN7VEK-nxXqo92VMtcHwjzf5xYN7VoTfXhtRWlUsttMAWkwt-0TvhGRdVLf-2Cot0xPF8csDgTUwkYD8rpjFymRHQN_HQ0BJ0YqBsZfsp3cOF2oP6Atp2tOKKahtWZJqtAwJ_IildY9Mic65CHUkxrBhO_zRyURKG5Icl9A4o6crrWqWTSiDzYiZyXW9O5yaISq7ASjUENge10yZBdSDzefH4huLG_uuGLT-qpW9l8aAeSUcBYv4mxyp'}
    response = requests.request("GET", url,json=data ,headers=headers, cookies=cookies)
    

    r=response.json()
    print(r)    




   

 


    





LoginAPIMikro()
StockUpdate()