'''
Ip calculator to convert number to binary
'''
from fastapi import FastAPI
from utils import number_to_binary, ip_to_binary, number_to_ip_mask

app = FastAPI()

@app.post('/to_binary')
def to_binary(a_number):
    number_as_int = int(a_number)
    result = number_to_binary(number_as_int)
    return {'value': result}

@app.post('/ip_to_binary')
def post_ip_to_binary(ip,mask):
    ip = ip_to_binary(ip)
    mask = number_to_ip_mask(mask)
    return {'ip': ip, 'mask': mask}
