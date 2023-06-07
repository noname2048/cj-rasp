import Adafruit_DHT as dht
import time
import requests
from dotenv import dotenv_values

config =  dotenv_values("../.env")
url = config["URL"]

while True:
    humidity, temperature = dht.read_retry(dht.DHT22, 4, delay_seconds=5)
    print(f"temp={temperature:0.2f} humi={humidity:0.2f}")

    res = requests.post(
        url=url,
        json={
            "temperature": temperature,
            "humidity": humidity,
        },
    )

    if res.status_code != 200:
        print(res.content)
        break;

    time.sleep(60)
