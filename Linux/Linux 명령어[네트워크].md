# Linux 명령어[네트워크]

```bash
Centos 로그인
localhost login: root	<-- 입력
Password: 		<-- 입력
[root@localhost ~] #	<-- 로그인 완료

화면 지우기(2가지)
ctrl + L
# clear

네트워크 확인
# nmcli con show
# nmcli con show [네트워크명]
ex) nmcli con show ens1
- q로 빠져나오기

네트워크 설정
NAT-Network 설정
# nmcli con add con-name ens1 type ethernet ifname enp0s3 ipv4.method manual ipv4.addresses 10.0.2.10/24 ipv4.gateway 10.0.2.1 ipv4.dns 8.8.8.8

Host-Only 설정
# nmcli con add con-name ens2 type ethernet ifname enp0s8 ipv4.method manual ipv4.addresses 192.168.56.10/24 ipv4.gateway 192.168.56.1 ipv4.dns 8.8.8.8
- con-name : 네트워크 이름
- type : 연결 방식
- ifname : 랜카드 이름
- ipv4.method : ip 설정 방식(자동 / 수동)
- ipv4.addresses : ip 주소
- ipv4.gateway : 패킷 관문
- ipv4.dns : 도메인 서버 주소

네트워크 활성화
# nmcli con up ens1
# nmcli con up ens2

네트워크 통신 확인
# ping 8.8.8.8
- 중지 시 ctrl + c 입력

네트워크 설정을 잘못 했을 경우(2가지)
첫 번째 방법(지우고 다시 생성)
# nmcli con del ens1	<-- 네트워크 제거
# nmcli con add ...		<-- 위에 설정 참고
# nmcli con up ens1	<-- 활성화

두 번째 방법(설정을 바꿔주기)
# nmcli con mod ens1 ipv4.addresses 192.168.56.11/24
# nmcli con reload
# nmcli con down ens1
# nmcli con up ens1

ip 주소 확인
# ip addr show
```
