import json
import base64
import sqlite3
import logging
import requests
import mcuuid as mc

def run():
    with open('data/CONF', 'r') as config_file:
        data = json.load(config_file)
    version = data.get('version')
    config_version = data.get('config_version')
    print(f"Running HyLogger Version: '{version}'")
    url = "https://api.github.com/repos/itzilly/HyLogger/contents/VERSION"
    response = requests.get(url).json()
    response_content = response.get('content')
    content_bytes = response_content.encode('ascii')
    latest_release_bytes = base64.b64decode(content_bytes)
    content = latest_release_bytes.decode('ascii')
    latest_release = content.split('=')[1]
    if version != latest_release:
        print(f"New release avalible! '{latest_release}'")

if __name__ == "__main__":
    run()
