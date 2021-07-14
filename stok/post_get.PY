
from dataclasses import dataclass
from django.http import JsonResponse
from requests.structures import CaseInsensitiveDict
from requests.exceptions import HTTPError
from art import text2art
import requests



#### http://<IIS sunucu ip >/api/Auth/Login --> Login URL
#### http://10.240.173/api/Stock/GetStok/{stok kod}
####






print (text2art("OLCAYTO  \n MIKRO-DJANGO INTERFACE \n")  )

global default_json_template    ### Standart MIKRO'ya gönderilen şablonu gösterir.
global headersAPI
global response_token ## tokenin her yerde kullanılmasını sağlar. 
global cookies
cookies = {'.AspNetCore.Identity.Application' : 'CfDJ8HcURbtv17VNmrVBiZiBEKMNNeGMErVwzTCnI0bModBTHRbgMVjo4cQeMVf5uJxRwP62W607U6wRHyIMYfWT9XWBf71j703pkKLhd_Bptj6C1XGAg2MkVomwsPRCVmIr2IftgGK4_ESuAvpvEMSF53i55xqzrsd-9rROtt2iDArXrimMKsbooweuNqvDA6U-lzqWy0cT1eKSrF-3lW9JGSflRqtu8aJhryX3MDGPe1skhGkHvxJdc-NTHpTGlIeMvDQZtuQPwdheB0frnF4BJKeWdpXfAF3TFEwTmD8bGpgD37Bp-osUJRYk1z3_mJXpfjzr9OreA4krwIR0OTQFHWD08G2sSZtX4YFeNqqDWCamGv1WFDlHr_00FwlB0_SFSqechJ-2C4QO1o2fixXSmgj-gQaOZEIRaAuxubXxLKEp3U3-CbaJAN7VEK-nxXqo92VMtcHwjzf5xYN7VoTfXhtRWlUsttMAWkwt-0TvhGRdVLf-2Cot0xPF8csDgTUwkYD8rpjFymRHQN_HQ0BJ0YqBsZfsp3cOF2oP6Atp2tOKKahtWZJqtAwJ_IildY9Mic65CHUkxrBhO_zRyURKG5Icl9A4o6crrWqWTSiDzYiZyXW9O5yaISq7ASjUENge10yZBdSDzefH4huLG_uuGLT-qpW9l8aAeSUcBYv4mxyp'}

data ={
   
    "userName" : 'admin',
    "password" : 'Adminuser_1234',
    
    }

params = (
    ('offset', '0'),
    ('limit', '20'),
)

default_json_template = {
    "sto_lastup_user": 0,
    "sto_special1": "string",
    "sto_special2": "string",
    "sto_special3": "string",
    "sto_kod": "stok kodudenemesi",
    "sto_isim": "string",
    "sto_kisa_ismi": "string",
    "sto_yabanci_isim": "string",
    "sto_sat_cari_kod": "string",
    "sto_cins": 0,
    "sto_doviz_cinsi": 0,
    "sto_detay_takip": 0,
    "sto_birim1_ad": "string",
    "sto_birim1_katsayi": 0,
    "sto_birim1_agirlik": 0,
    "sto_birim1_en": 0,
    "sto_birim1_boy": 0,
    "sto_birim1_yukseklik": 0,
    "sto_birim1_dara": 0,
    "sto_birim2_ad": "string",
    "sto_birim2_katsayi": 0,
    "sto_birim2_agirlik": 0,
    "sto_birim2_en": 0,
    "sto_birim2_boy": 0,
    "sto_birim2_yukseklik": 0,
    "sto_birim2_dara": 0,
    "sto_birim3_ad": "string",
    "sto_birim3_katsayi": 0,
    "sto_birim3_agirlik": 0,
    "sto_birim3_en": 0,
    "sto_birim3_boy": 0,
    "sto_birim3_yukseklik": 0,
    "sto_birim3_dara": 0,
    "sto_birim4_ad": "string",
    "sto_birim4_katsayi": 0,
    "sto_birim4_agirlik": 0,
    "sto_birim4_en": 0,
    "sto_birim4_boy": 0,
    "sto_birim4_yukseklik": 0,
    "sto_birim4_dara": 0,
    "sto_muh_kod": "string",
    "sto_muh_Iade_kod": "string",
    "sto_muh_sat_muh_kod": "string",
    "sto_muh_satIadmuhkod": "string",
    "sto_muh_sat_isk_kod": "string",
    "sto_muh_aIiskmuhkod": "string",
    "sto_muh_satmalmuhkod": "string",
    "sto_yurtdisi_satmuhk": "string",
    "sto_ilavemasmuhkod": "string",
    "sto_yatirimtesmuhkod": "string",
    "sto_depsatmuhkod": "string",
    "sto_depsatmalmuhkod": "string",
    "sto_bagortsatmuhkod": "string",
    "sto_bagortsatIadmuhkod": "string",
    "sto_bagortsatIskmuhkod": "string",
    "sto_satfiyfarkmuhkod": "string",
    "sto_yurtdisisatmalmuhkod": "string",
    "sto_bagortsatmalmuhkod": "string",
    "sto_sifirbedsatmalmuhkod": "string",
    "sto_ihrackayitlisatismuhkod": "string",
    "sto_ihrackayitlisatismaliyetimuhkod": "string",
    "sto_karorani": 0,
    "sto_min_stok": 0,
    "sto_siparis_stok": 0,
    "sto_max_stok": 0,
    "sto_perakende_vergi": 0,
    "sto_toptan_vergi": 0,
    "sto_yer_kod": "string",
    "sto_satis_dursun": 0,
    "sto_siparis_dursun": 0,
    "sto_malkabul_dursun": 0,
    "sto_iskon_yapilamaz": True,
    "sto_kategori_kodu": "string",
    "sto_urun_sorkod": "string",
    "sto_altgrup_kod": "string",
    "sto_anagrup_kod": "string",
    "sto_uretici_kodu": "string",
    "sto_sektor_kodu": "string",
    "sto_reyon_kodu": "string",
    "sto_muhgrup_kodu": "string",
    "sto_ambalaj_kodu": "string",
    "sto_marka_kodu": "string",
    "sto_beden_kodu": "string",
    "sto_renk_kodu": "string",
    "sto_model_kodu": "string",
    "sto_sezon_kodu": "string",
    "sto_hammadde_kodu": "string",
    "sto_prim_kodu": "string",
    "sto_kalkon_kodu": "string",
    "sto_paket_kodu": "string",
    "sto_mkod_artik": "string",
    "sto_bedenli_takip": True,
    "sto_renkDetayli": True,
    "sto_pasif_fl": True,
    "sto_eksiyedusebilir_fl": True,
    "sto_tamamlayici_kodu": "string",
    "sto_yerli_yabanci": 0,
    "sto_mensei": "string"

        }

    ### Connection of the MIKRO API FUNCTION"

def LoginAPIMikro():
        ##Parameters##
            print("API connection has initilazed")
            url = "http://10.240.1.73/api/Auth/Login"
            response = requests.request("POST", url, json = data, verify=True)
            success_login = (response != True)
            if (success_login):
                print("\n\nBaşarılı şekilde bearer token verisi alınmıştır.\n\n\n")
                response_token = response
            else:  print("Houston we have problem Call 911")
            print("Dönen Durum Kodu  {}\n\n\n" .format(response.status_code) )
            response_token =response_token.json()
            print(response_token) 
           


def stock_create():
    print("#Stok Kodu oluşturma talebi# \n \n \n ")
    url = "http://10.240.1.73/api/Stock/AddStok" # Related URL
# Header inf


    headers = CaseInsensitiveDict() 
    headers["Content-Type"] = "applicaton/json"

    send_data= """
    
   {"sto_Guid":"cca3df4c-5266-4bfe-9c18-e6af697d09af","sto_create_user":60,"sto_create_date":"2020-07-16T10:52:39.483","sto_lastup_user":60,"sto_lastup_date":"2020-07-16T10:52:39.483","sto_special1":"ANK","sto_special2":"PLN","sto_special3":"","sto_kod":"AG.YM50001","sto_isim":"ELEKTRONIK KART SDIL_V1","sto_kisa_ismi":"","sto_yabanci_isim":"","sto_sat_cari_kod":"","sto_cins":4,"sto_doviz_cinsi":0,"sto_detay_takip":0,"sto_birim1_ad":"ADET","sto_birim1_katsayi":1.0,"sto_birim1_agirlik":0.0,"sto_birim1_en":0.0,"sto_birim1_boy":0.0,"sto_birim1_yukseklik":0.0,"sto_birim1_dara":0.0,"sto_birim2_ad":"","sto_birim2_katsayi":0.0,"sto_birim2_agirlik":0.0,"sto_birim2_en":0.0,"sto_birim2_boy":0.0,"sto_birim2_yukseklik":0.0,"sto_birim2_dara":0.0,"sto_birim3_ad":"","sto_birim3_katsayi":0.0,"sto_birim3_agirlik":0.0,"sto_birim3_en":0.0,"sto_birim3_boy":0.0,"sto_birim3_yukseklik":0.0,"sto_birim3_dara":0.0,"sto_birim4_ad":"","sto_birim4_katsayi":0.0,"sto_birim4_agirlik":0.0,"sto_birim4_en":0.0,"sto_birim4_boy":0.0,"sto_birim4_yukseklik":0.0,"sto_birim4_dara":0.0,"sto_muh_kod":"150.01.01.001","sto_muh_Iade_kod":"150.01.01.001","sto_muh_sat_muh_kod":"600.01.01.001","sto_muh_satIadmuhkod":"610.01.01.001","sto_muh_sat_isk_kod":"611.01.01.001","sto_muh_aIiskmuhkod":"150.01.01.001","sto_muh_satmalmuhkod":"621.01.01.001","sto_yurtdisi_satmuhk":"601.01.01.001","sto_ilavemasmuhkod":"150.01.01.001","sto_yatirimtesmuhkod":"258","sto_depsatmuhkod":"600.01.01.001","sto_depsatmalmuhkod":"621.01.01.001","sto_bagortsatmuhkod":"600.01.01.001","sto_bagortsatIadmuhkod":"610.01.01.001","sto_bagortsatIskmuhkod":"611.01.01.001","sto_satfiyfarkmuhkod":"600","sto_yurtdisisatmalmuhkod":"621.01.01.001","sto_bagortsatmalmuhkod":"621.01.01.001","sto_sifirbedsatmalmuhkod":"760","sto_ihrackayitlisatismuhkod":"601","sto_ihrackayitlisatismaliyetimuhkod":"621","sto_karorani":0.0,"sto_min_stok":0.0,"sto_siparis_stok":0.0,"sto_max_stok":0.0,"sto_perakende_vergi":4,"sto_toptan_vergi":4,"sto_yer_kod":"","sto_satis_dursun":0,"sto_siparis_dursun":0,"sto_malkabul_dursun":0,"sto_iskon_yapilamaz":false,"sto_kategori_kodu":"","sto_urun_sorkod":"","sto_altgrup_kod":"YM","sto_anagrup_kod":"SAVUNMA","sto_uretici_kodu":"","sto_sektor_kodu":"","sto_reyon_kodu":"","sto_muhgrup_kodu":"","sto_ambalaj_kodu":"","sto_marka_kodu":"","sto_beden_kodu":"","sto_renk_kodu":"","sto_model_kodu":"","sto_sezon_kodu":"","sto_hammadde_kodu":"","sto_prim_kodu":"","sto_kalkon_kodu":"","sto_paket_kodu":"","sto_mkod_artik":"","sto_bedenli_takip":false,"sto_renkDetayli":false,"sto_pasif_fl":false,"sto_eksiyedusebilir_fl":false,"sto_tamamlayici_kodu":"","sto_yerli_yabanci":0,"sto_mensei":""}
    
    """
    try:
        r = requests.post(url,json=send_data, headers=headers  ,cookies=cookies)
        print(headers)
        r.raise_for_status()
        jsonResponse=r.json()
        

        print("Client JSON respond is below \n")
        print(jsonResponse.raw)
    

    except HTTPError as http_err:
        print("Code Creation failed.\n Response Header infos\n {} \n{} \n {} " .format(r.text,r.headers, r.raise_for_status, r.raw))
        print(f'HTTP Error occurred : {http_err}')
       

    
    except Exception as err:
    
        print(f'Other Error occured : {err}')
    
def stock_update():

    headers = CaseInsensitiveDict() 
 
    headers["Content-Type"] = "application/json"


    url = "http://10.240.1.73/api/Stock/UpdateStok" # Related URL

    send_data= {
        "test " : "11"


    }

    try:
        r = requests.post(url,json=send_data, headers=headers ,cookies=cookies)
        print(headers)
        r.raise_for_status()
        jsonResponse=r.json()
        print("Client JSON respond is below \n")
        print(jsonResponse)
    except HTTPError as http_err:
        print("Code Creation failed.\n Response Header infos\n {} " .format(r.json))
        print(f'HTTP Error occurred : {http_err}')        
    except Exception as err:
    
        print(f'Other Error occured : {err}')


def stock_get():
    kod = "1"
    url= "http://10.240.1.73/api/Stock/GetStok/{}".format(kod)

    
    r=requests.get(url, cookies=cookies)
    print(r.json())
    

LoginAPIMikro()
#stock_update()
#stock_create()
stock_get()
            