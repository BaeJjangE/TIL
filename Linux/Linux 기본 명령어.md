# Linux 기본 명령어

```bash
현재 위치 디렉토리 확인
# pwd

작업 디렉토리를 바꿀 때
# cd 절대경로, 상대경로
절대경로: 최상위 디렉토리 (/)부터 시작해서 목표 디렉토리까지 가는 경로를 전부 기술하는 방식 ex) cd /a/b/c/d/
상대경로: '현재 자신이 있는 위치를 기준으로' ex) cd ./c/d/
사용자의 홈 디렉토리로 이동: # cd 
현재 디렉토리: cd .
상위 디렉토리로 이동: cd ..

디렉토리
- 디렉토리를 확인할 시 ls -l 명령어를 사용
# ls -l
- 결과: 맨 앞에 나오는 알파벳이 "d" 이면 디렉토리

자동완성 : tab 키 사용
- 디렉토리 부분에서 자동완성 시 디렉토리명 뒤에 /(슬래시)가 자동으로 붙음

파일 내용 확인
cat - 파일 내용 전체 확인
# cat 파일명
- 가상 머신에서는 상위 내용을 확인 X
- putty에서는 상위 내용을 확인 O

head - 파일 내용의 전반부 10줄 확인
# head 파일명
# head -n 12 파일명
- anaconda-ks.cfg 파일의 전반부 12줄 확인

tail - 파일 내용의 후반부 10줄 확인
# tail 파일명

more - 파일 내용 전체 확인
# more 파일명
- 화살표 위아래 키 사용 불가
- space바로 페이지 이동
- enter로 한 줄 이동

less - 파일 내용 전체 확인
# less 파일명
- 화살표 위아래 키 사용 가능
- space바로 페이지 이동
- enter로 한 줄 이동
- page up/down 사용 가능
- 빠져나올 경우 q 버튼 누르기

grep - 파일 내용에서 문자열 검색
# cat anaconda-ks.cfg | grep System
- anaconda-ks.cfg 라는 파일을 확인하여 결과물을 출력하여 System 이라는 단어에 해당하는 줄 내용을 출력

파일 관리 명령어
		파일					디렉토리
생성		touch, vim			mkdir

이동		mv 파일명 이동할위치	mv 디렉토리명 이동할위치

복사		cp 파일명 복사할위치	cp -r 디렉토리명 이동할위치

삭제		rm 파일명				rm -r 디렉토리명

파일 생성
# touch test.py
- 빈 파일 생성

# touch fileA fileB fileC
- fileA fileB fileC 생성
- 파일 여러개 생성 가능

디렉토리 생성
# mkdir dirA
- 빈 디렉토리 생성

파일 이동
# mv test.py dirA/

# mv fileA fileB fileC dirA
- fileA fileB fileC 파일을 dirA 이동
- 여러 파일 이동 가능
- 옮길 위치에 똑같은 이름의 파일이 있을 경우 덮어 쓸 것인지 질문함
 - 질문에 no 라고 답하면 이동자체가 되지 않음

파일 이름 변경
# touch fileD
# mv fileD fileE
- mv를 사용하여 파일의 이름 변경 가능

디렉토리 이동
# mkdir dirB
# mv dirB dirA

디렉토리 이름 변경
# mkdir dirD
# mv dirD dirE
- mv를 사용하여 디렉토리의 이름 변경 가능

파일 복사
# cp 파일명 /tmp

여러 파일을 디렉토리에 복사 가능
# cp anaconda-ks.cfg python.py dirA
- anaconda-ks.cfg, python.py 파일을 dirA에 복사


디렉토리 복사
# mkdir dirC
# cp -r dirC dirA

파일 삭제
# rm 파일명
- 일반 파일 삭제 시에 삭제할 것인지 질문함

# touch fileA fileB fileC
# rm fileA fileB fileC
- fileA, fileB, fileC 제거
- 파일 한 번에 삭제 가능

디렉토리 삭제
# rm -r dirA/
- rmdir 로 디렉토리를 지울 경우 내부에 파일이 있으면 디렉토리 삭제 불가

번외)
파일 강제로 덮어쓰기
# touch fileA fileB fileC
# cp fileA fileB fileC dirC/
# mv -f fileA fileB fileC dirC/
- f 옵션 사용시 강제로 덮어씀
 - cp 명령어도 마찬가지로 -f 옵션 사용 시 강제로 덮어씀
 - rm 명령어도 마찬가지로 -f 옵션 사용 시 강제로 삭제
```

