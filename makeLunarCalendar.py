#!/usr/bin/python3

# 조회할 날짜 데이터 리스트를 만든다
# 파일을 연다
# get 조회를 한다
# https://astro.kasi.re.kr/life/solc?yyyy=2020&mm=04&dd=15
# json 파싱을 한다
# {
#     "LUNC_AGE": 22.1,
#     "LUNC_DD": "23",
#     "LUNC_EN_DD": "30",
#     "LUNC_ILJIN": "무자(戊子)",
#     "LUNC_LEAP_MM": "평",
#     "LUNC_MM": "03",
#     "LUNC_PRCN": "경자(庚子)",
#     "LUNC_WLGN": "경진(庚辰)",
#     "LUNC_YYYY": "2020",
#     "SOLC_DD": "15",
#     "SOLC_JD": "2458955",
#     "SOLC_LEAP_YYYY": "윤",
#     "SOLC_MM": "04",
#     "SOLC_WEEK": "수",
#     "SOLC_YYYY": "2020"
# }
# LUNC_YYYY + LUNC_MM + LUNC_DD
# 필요한 데이터를 필요한 string 으로 변환한다
#   { "Hello", "World" },
#   { "John", "Doe" },
# 파일에 쓴다
# 500건당 1초 쉰다

import requests
import json
import time
import datetime

filename = 'lunarCalendar'

solarCalendar = []
start_date = datetime.date(2020, 5, 12)
end_date = datetime.date(2050, 12, 31)
delta = datetime.timedelta(days=1)

url = "https://astro.kasi.re.kr/life/solc?yyyy={}&mm={}&dd={}"

with open(filename, "w", encoding="utf-8") as write:
    index = 0
    while start_date <= end_date:
        date = start_date.strftime("20%y%m%d")
        r = requests.get(url.format(date[0:4], date[4:6], date[6:]))
        result = ''

        try:
            result = json.loads(r.text)
        except:
            print("error: " + date)

        lunarDate = result["LUNC_YYYY"] + result["LUNC_MM"] + result["LUNC_DD"]
        output = ' { "' + date + '", "' + lunarDate + '" },'
        print(output)
        write.writelines(output + "\n")
        index += 1
        # if index % 1000 == 0:
        #     time.sleep(1)

        start_date += delta

