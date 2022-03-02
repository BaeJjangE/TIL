# Linux 고급 명령어

## 프로세스

```bash
프로세스
- 디스크에 저장된 프로그램 파일을 실행하면 메모리에 올라가서 동작중인 상태

exec : 내가 직접 동작
- 기존 프로세스가 그대로 동작

fork : 프로세스를 복사하여 동작
- 부모프로세스는 프로세스의 동작과 상태를 저장
- 자식프로세스는 업무를 처리하여 효율적인 작업이 이루어지도록 하기 위함

포어그라운드
- 육안으로 식별 가능한 작업 공간

포어 그라운드에서 명령어 실행
# sleep 10000

백그라운드
- 육안으로 식별 불가능한 작업 공간

백그라운드에서 명령어 실행
# sleep 10000 &
- 명령어 뒤에 & 기호 사용
- [1] 뒤에 숫자는 다르게 출력

jobs
- 작업 목록 확인 명령어

백그라운드 프로세스 추가 실행
# sleep 10000 &
# sleep 10000 &
# sleep 10000 &

# jobs
결과)
[1]   Running                 sleep 10000 &
[2]   Running                 sleep 10000 &
[3]-  Running                 sleep 10000 &
[4]+  Running                 sleep 10000 &

백그라운드에서 동작중인 프로세스를 포어그라운드로 전환
# fg %1
sleep 10000

포어그라운드에서 동작중인 프로세스를 백그라운드로 전환
^Z
[1]+  Stopped                 sleep 10000
- 포어그라운드에서 하고 있던 작업을 ctrl + z 입력하여 일시중지

# bg %1
[1]+ sleep 10000 &

프로세스 확인 명령어(ps, top)
ps
- 최근 프로세스의 실행하는 순간의 현재 상태를 찍어서 보여주는 명령어
# ps aux
- a : 모든 프로세스
- u : user
- x : 종료 되지 않은 동작중인 프로세스
- ps 명령어 옵션은 대시(-)를 사용해도 되고 사용하지 않아도 됨

top
- 현재 동작중인 모든 프로세스를 "실시간"으로 확인할 수 있는 명령어
# top
- PID : 프로세스 아이디
- 종료는 q 버튼

uptime
- 부하율을 출력하는 명령어
# uptime
 10:30:13 up  1:23,  2 users,  load average: 0.00, 0.01, 0.03
- 0.00, 0.01, 0.03 은 각각 1분, 5분, 15분에 대한 부하율을 나타냄
- 부하율이 1을 넘어가지 않으면 만족스러운 리소스 사용량 및 최소 대기 시간

w
- 현재 작업중인 사용자와 작업 목록을 확인
# w
 10:35:08 up  1:28,  2 users,  load average: 0.00, 0.01, 0.03
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      10:03   31:24   0.00s  0.00s -bash
root     pts/0    gateway          09:19    4.00s  0.02s  0.00s w

프로세스 강제 종료
# ps aux
- 강제 종료 전 프로세스 번호(PID) 확인

# kill -9 1363
# ps aux
...
[1]   죽었음               sleep 10000
- 1363번에 해당하는 프로세스 종료를 확인

pgrep
- 프로세스를 작업 내용을 가지고 검색
# pgrep sl
1041
1364
1365
1366
- PID만 출력

[root@localhost ~]# pgrep -l sl
1041 rsyslogd
1364 sleep
1365 sleep
1366 sleep
- l 옵션하여 리스트로 출력

pkill
- 프로세스를 작업 내용을 가지고 종료
# pkill sleep
[2]   종료됨               sleep 10000
[3]-  종료됨               sleep 10000
[4]+  종료됨               sleep 10000

nice
- 우선 순위
- 프로세스 실행 시 기본값 0
- 값이 감소하면 우선 순위가 높아짐
- 값이 증가하면 우선 순위가 떨어짐
- root 사용자는 우선 순위를 -20 ~ 19 설정(초기 설정)
- root 사용자는 우선 순위를 -20 ~ 19 마음대로 조정 가능
- 일반 사용자는 우선 순위를 1 ~ 19 설정(초기 설정)
- 일반 사용자는 우선 순위를 초기 설정보다 높은 값으로만 조정 가능

nice로 우선 순위 지정
- 형식 : nice -n [순위] [명령어]
# nice -n 10 sleep 5000 &
[5] 3754

renice로 우선 순위 재지정
- 형식 : renice -n [순위] [PID]
# renice -n 5 3754
```



## 권한

```bash
권한
- 소유자는 파일을 소유하고 있는 사용자(단일)
- 소유그룹은 파일을 소유하고 있는 그룹(사용자의 집합)
- 권한을 바꿀 수 있는 사용자 : root, 소유자

퍼미션 종류
r: 파일 내용 읽기(cat, more, head, ~), 디렉토리 내 파일 정보 확인(ls)
w: 파일 내용 편집(vim, redirect, ~), 파일 생성 및 삭제(cp, mv, rm, ~)
x: 실행파일 경우에만 실행, 디렉토리 접근(cd)
-rwx------	<-- 소유자는 모든 권한, 소유 그룹 권한 X, 기타 사용자 권한 X
-rwxrw----	<-- 소유자는 모든 권한, 소유 그룹은 읽기, 쓰기, 기타 사용자는 권한 X

퍼미션 설정
chmod [option] 파일명

권한 확인
# ls -l fileA
-rw-r--r--. 1 root root 0  1월 26 13:12 fileA
# ls -l fileB
-rw-r--r--. 1 root root 0  1월 26 13:29 fileB

알파벳을 이용하여 권한 바꾸기
조건)
소유자 권한 실행 권한 추가
# chmod u+x fileA
소유그룹 권한 쓰기 권한 추가
# chmod g+w fileA
기타사용자는 아무 권한 없게 설정
# chmod o-r fileA
- # chmod o= fileA 설정 가능
파일의 소유자 권한 확인
# ls -l fileA
-rwxrw----. 1 root root 0  1월 26 13:12 fileA

숫자를 이용하여 권한 바꾸기
r: 4
w: 2
x: 1
# chmod 760 fileB
# ls -l fileB
-rwxrw----. 1 root root 0  1월 26 13:29 fileB

소유권 변경 전 선행 작업: user1 추가
# useradd user1

소유자 변경(user1)
# chown user1 fileA
# ls -l fileA
-rwxrw----. 1 user1 root 0  1월 26 13:12 fileA

소유 그룹 변경(user1)
# chown :user1 fileA
# ls -l fileA
-rwxrw----. 1 user1 user1 0  1월 26 13:12 fileA

소유자, 소유 그룹 변경(root, root)
# chown root:root fileA
# ls -l fileA
-rwxrw----. 1 root root 0  1월 26 13:12 fileA

특수 권한 부여 전 사전 작업
# mkdir dirA

권한 확인(디렉토리)
# ls -ld dirA
drwxr-xr-x. 2 root root 6  1월 26 14:06 dirA

특수 권한 부여(디렉토리) - 필요시 따로 구글 검색
# chmod g+s dirA
# ls -ld dirA
drwxr-sr-x. 2 root root 6  1월 26 14:06 dirA

번외) 특수 권한이 부여된 디렉토리에서 실행 제거
# chmod g-x dirA
# ls -ld dirA
drwxr-Sr-x. 2 root root 6  1월 26 14:06 dirA

- 특수 권한이 대문자로 설정되어 있으면 특수 권한 적용 X
- 실행 권한을 부여해야 특수 권한이 적용됨

리눅스에서는 보통
확인할 때 get ~
설정할 때 set ~

POSIX ACL 설정 확인
# getfacl fileA
결과
# file: fileA
# owner: root
# group: root
# flags: s--	<-- 특수 권한
user::rwx
group::rw-
other::---

setfacl
- 형식 : setfacl [option] ENTRY:NAME:PERMS file-name
- 많이 사용하는 옵션
 - m : 추가 / 수정할 때 사용하는 옵션
  - 소유자 권한을 바꾸고 싶을 때 u::<perm> 파일명
  - 소유 그룹의 권한을 바꾸고 싶을 때 g::<perm> 파일명
  - 특정 사용자의 권한을 설정할 때 u:<user_name>:<perm> 파일명
  - 특정 그룹의 권한을 설정할 때 u:<group_name>:<perm> 파일명
  - mask의 권한 m::<perm> 파일명

ACL 설정(user1)
# setfacl -m u:user1:rwx fileA
# setfacl -m g:user1:rwx fileA
# getfacl fileA
결과)
# file: fileA
# owner: root
# group: root
# flags: s--
user::rwx
user:user1:rwx	<--
group::rw-
group:user1:rwx	<--
mask::rwx		<--
other::---

mask 값
- 특정 사용자, 소유 그룹, 특정 그룹에 부여할 수 있는 최대 권한을 정의

mask 값 변경
# setfacl -m m::r-- fileA
# getfacl fileA
결과)
# file: fileA
# owner: root
# group: root
# flags: s--
user::rwx
user:user1:rwx                  #effective:r--
group::rw-                      #effective:r--
group:user1:rwx                 #effective:r--
mask::r--		<-- 변경 확인
other::---
- mask 값은 파일 소유자나 기타 사용자의 권한을 제한하지 않음
- user:user1:rwx 는 사용자가 직접 부여한 권한       
- #effective:r-- 는 실제 부여되는 권한(mask 값보다 높을 경우 표시)

ACL 설정 제거(x 옵션 사용)
# setfacl -x u:user1,g:user1 fileA
# getfacl fileA
결과)
# file: fileA
# owner: root
# group: root
# flags: s--
user::rwx
group::rw-
mask::rw-
other::---
```

