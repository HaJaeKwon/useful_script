# 보안 서버접속 스크립트

> A Shell script to connect target server through kerberos gateway server

사내 서버 접속을 간편하게 하기위해 expect script를 활용

sauth.sh의 {{GATEWAY_DOMAIN}}, {{PATH}} 변수를 반드시 환경에 맡게 변경해야함

로컬(with vpn) -> connect Kerberos Server -> get Ticket -> connect Develop Server
```shell script
/bin/sh sauth.sh {{GatewayID}} {{GatewayPass}} {{TargetServerHost}} {{GoogleOTP}}
```

보통은 bash_profile에 아래와 같은 함수를 등록해두고 사용
```shell script
function ss { /bin/sh ~/sauth/sauth.sh ${ID} ${PASS} $*; }
```
