# 음력 달력 생성기

한국천문연구원(https://astro.kasi.re.kr/index) 으로부터 음력 날짜를 조회하여 file로 생성해주는 스크립트

날짜 하나당 한번 API 조회하는 형태여서 file 생성에 시간이 어느정도 소요된다.

file은 json 형태의 key(양력날짜), value(음력날짜)로 생성된다.

```shell script
./makeLunarCalendar.py {start_date:20200513} {end_date:20200515} {output_file}

output
{
 { "20200513": "20200421" },
 { "20200514": "20200422" },
 { "20200515": "20200423" }
}
```
