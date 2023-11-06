import requests, base64, random, argparse, os, playsound, time, re, textwrap, json, time


ENDPOINT = 'https://tiktok-tts.weilnet.workers.dev'

headers = {'Content-type': 'application/json'}

f = open("./posts/I messed up the tire on my parents van while running errands", "r")

inc = 0
for line in f.readlines():
    time.sleep(1.5)
    line = line.strip()
    rest_array = [text.encode("utf8") for text in line]
    line = b''.join(rest_array)
    url = "{endpoint}/api/generation".format(endpoint=ENDPOINT)
    json = b'{"text": "' + line + b'", "voice": "en_us_001"}'
    r = requests.post(url, json, headers=headers).json()

    vstr = r["data"]

    b64d = base64.b64decode(vstr)

    os.system("touch {num}.mp3".format(num=inc))

    out = open("{num}.mp3".format(num=inc), "wb")
    out.write(b64d)
    out.close()

    # playsound.playsound("{num}.mp3".format(num=inc))



