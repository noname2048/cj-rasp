import Adafruit_DHT as dht
import requests
from dotenv import dotenv_values
import asyncio

config =  dotenv_values("../.env")
url = config["URL"]
uuid = config["UUID"]

async def main():
    print("starting...")
    while True:
        humidity, temperature = dht.read_retry(dht.DHT22, 4, delay_seconds=5)
        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        print(f"temp={temperature:0.2f} humi={humidity:0.2f}")

        res = requests.post(
            url=url,
            json={
                "uuid": uuid,
                "temperature": temperature,
                "humidity": humidity,
            },
        )

        if res.status_code != 200:
            print(res.status_code)
            print(res.text)
        
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
