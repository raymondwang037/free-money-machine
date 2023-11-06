import requests, base64, random, argparse, os, playsound, time, re, textwrap, json, time


ENDPOINT = 'https://tiktok-tts.weilnet.workers.dev'

headers = {'Content-type': 'application/json'}
def mp3(txt_path):
    f = open(txt_path, "r")

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

        out = open("{txtfile}.mp3".format(txtfile=txt_path), "ab+")
        out.write(b64d)
        out.close()

    # playsound.playsound("{num}.mp3".format(num=inc))