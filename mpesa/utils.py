import base64
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

def get_access_token():
    consumer_key = ""
    consumer_secret = ""
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    access_token = response.json().get("access_token")
    return access_token

def stk_push(phone_number, amount):
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    business_short_code = "174379"   # e.g. Till Number
    lipa_na_mpesa_online_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        (business_short_code + lipa_na_mpesa_online_passkey + timestamp).encode()
    ).decode('utf-8')

    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": business_short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": business_short_code, 
        "PhoneNumber": phone_number,
        "CallBackURL": "https://yourdomain.com/api/mpesa/callback/",
        "AccountReference": "RentPayment",
        "TransactionDesc": "Rental Payment"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
