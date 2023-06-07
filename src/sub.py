import Adafruit_DHT as dht
import requests
from datetime import datetime, timedelta, timezone
from dotenv import dotenv_values

config =  dotenv_values("../.env")
url = config["URL"]

KST = timezone(offset=timedelta(hours=9))
humidity, temperature = dht.read_retry(dht.DHT22, 4, delay_seconds=5)

res = requests.post(
    url=url,
    json={
        "temperature": temperature,
        "humidity": humidity,
    },
)

if res.status_code != 200:
    print(f"temp={temperature:0.2f} humi={humidity:0.2f}")
    print(res.content)
else:
    print(f"temp={temperature:0.2f} humi={humidity:0.2f} | {datetime.now(tz=KST).strftime('%y%m%d %H:%M:%S')}")

