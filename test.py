import requests, base64, random, argparse, os, playsound, time, re, textwrap, json


ENDPOINT = 'https://tiktok-tts.weilnet.workers.dev'

headers = {'Content-type': 'application/json'}



r = requests.post(ENDPOINT + "/api/generation", '{"text": "it works now", "voice": "en_us_ghostface"}', headers=headers).json()

vstr = r["data"]

b64d = base64.b64decode(vstr)

out = open("test.mp3", "wb")
out.write(b64d)
out.close()

playsound.playsound("test.mp3")