# temperature-in-my-house

내방의 온도를 측정하여 database 에 넣기 위한 프로젝트

1. __raspberry 4B__ 에서 DHT22 센서를 이용해 온습도 데이터를 수집합니다.
2. 수집된 데이터를 requests 를 통해 aws-lambda 로 전달합니다. ([ci-aws-lambda](https://github.com/noname2048/ci-aws-lambda))
3. aws-lambda 는 supabase postgresql 데이터 베이스에 넣습니다.

기타사항
- raspberry pi는 재부팅시에도 온도를 자동으로 수집할 수 있도록, systemctl 혹은 crontab 을 이용합니다.
- aws-lambda 는 필요한 파이썬 패키지를 포장하여 layer로 등록합니다.

## raspberry 4B 온도수집

1. `Adafruit_DHT`, `requests`, `python-dotenv` 패키지를 설치합니다.
2. `crontab -e` 를 치고 경로를 적절히 바꾸어 실행합니다.
