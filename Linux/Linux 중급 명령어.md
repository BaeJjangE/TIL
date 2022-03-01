# Linux 중급 명령어

## 링크

```bash
링크
심볼릭 링크
- 파일명을 참조
- 원본 파일 삭제시 사용 불가(파일명을 참조하기 때문)
- 용도 : 명령어, 경로가 복잡한 디렉토리에 쉽게 접근하기 위해 사용
- 명령어 형식 : ln -s [원본 파일명] [만들 파일명]
# ln -s fileA soft_fileA

하드 링크
- inode 테이블을 참조
- 파일 삭제시 사용 가능(inode 테이블을 참조)
- 용도 : 프로그래밍(다수 사람들의 작업)
- 명령어 형식 : ln [원본 파일명] [만들 파일명]
# ln fileA hard_fileA

--------------------------------------------------------
링크 실습(확인 시 ls -il 로 확인해보는 것을 권장)
파일 분석
# ls -l
결과)
-rw-r--r--. 2 root root 0  1월 25 14:31 fileA
-rw-r--r--. 2 root root 0  1월 25 14:31 hard_fileA
lrwxrwxrwx. 1 root root 5  1월 25 14:33 soft_fileA
- 하드 링크는 root 앞에 갯수가 1에서 2로 증가

원본 파일에 내용 삽입
# echo "12345" > fileA

파일 내용 확인
# cat fileA
결과) 12345
# cat hard_fileA
결과) 12345
# cat soft_fileA
결과) 12345
- 원본 파일과 링크 파일의 내용이 동일함을 확인

원본 파일 지우기
# rm fileA

파일 확인(확인 시 ls -il 로 확인해보는 것을 권장)
# ls -l
결과)
-rw-r--r--. 1 root root 6  1월 25 14:39 hard_fileA
lrwxrwxrwx. 1 root root 5  1월 25 14:33 soft_fileA(빨간색) -> fileA(빨간색)
- 파일명을 참조하는 심볼릭 링크 파일은 쓰임이 사라짐

파일 내용 확인
# cat hard_fileA
결과) 12345
# cat soft_fileA
결과)
cat: soft_fileA: 그런 파일이나 디렉터리가 없습니다

fileA 생성
# touch fileA

파일 확인
# ls -l
결과)
-rw-r--r--. 1 root root 0  1월 25 14:42 fileA
-rw-r--r--. 1 root root 6  1월 25 14:39 hard_fileA
lrwxrwxrwx. 1 root root 5  1월 25 14:33 soft_fileA -> fileA
- 파일명을 참조하는 심볼릭 링크 파일은 다시 fileA를 참조

추가 내용 정리)
fileA를 재생성한 것은 기존 파일 fileA와 다른 파일이 생성된 것(확인은 cat 명령어 사용)
심볼릭 링크의 원본 파일의 이름을 바꿀 시 링크 동작 X

하드 링크 복사 차이점
- 하드 링크는 원본 데이터를 참조(바뀐 데이터가 계속 반영)
- 복사는 일시적인 데이터 복사(바뀐 데이터가 계속 반영 X)
```

## 검색

```bash
검색
locate
- 명령어 형식 : locate [파일명]
패키지 설치
# yum -y install mlocate

데이터베이스 업데이트
# updatedb

locate 명령어로 fileA 검색
# locate fileA
결과)
/root/fileA
/root/hard_fileA
/root/soft_fileA

find
- 명령어 형식 : find [경로] [조건]

find 명령어로 파일명이 file로 시작하는 모든 파일 검색(최상위 디렉토리부터)
# find / -name "file*"
- * 은 모든이라는 뜻을 가짐

find 명령어로 파일명이 file로 시작하는 모든 파일 검색(현재 디렉토리부터)
# find . -name "file*"

""(쌍따옴표) 사용 이유
- 하나로 묶여진 문자열을 표현하기 위해 사용
```

## vim 편집기

```bash
vim 편집기
설치
# yum -y install vim

4가지 동작모드 지원(21page ppt 글자 깨짐)
Command mode - 커서 이동 및 단순 편집 기능
Edit mode - 내용 추가 및 수정
Extended mode - 추가 기능 지원
Visual mode - 블록 처리 기능 제공

사용법(ppt 내용 참고)
i - edit mode 진입
esc - command mode 진입
:w - 저장하기(extended mode)
:q - 빠져나오기(extended mode)
! - 강제(extended mode)
```

## 파일 입출력

```bash
파일 입출력
echo : 인자를 그대로 출력
- >, >> 리다이렉션 기호는 echo와 많이 쓰임

echo와 리다이렉션을 사용하여 파일 쓰기
# echo 123456 > test.txt
- 파일 덮어쓰기(원본 파일 복귀 불가)
- 확인은 cat 명령어 사용

# echo 789 >> test.txt
- 파일 이어쓰기
- 중간에 파일 내용 추가 불가(무조건 끝 줄에 추가)
- 확인은 cat 명령어 사용

파이프
입력에 해당하는 출력값을 파이프 뒤에 나오는 명령어가 입력값으로 받아서 처리
# cat test.txt | grep 345
- test.txt 내용의 출력값을 grep이 받아서 345 문자열을 찾아 출력

tee
명령어의 출력 결과를 파일과 화면에 동시에 출력할 수 있도록 해주는 명령어
리다이렉션과 파이프를 혼용해서 사용
# ls -l | tee 파일명 | grep bbbbbb
- ls -l 명령어는 grep 명령어 도달까지 계속 동작
- 도중에 ls -l 결과를 파일명에 저장
- 옵션
-a: 덮어쓰기 말고 해당 파일에 추가해서 입력
-i: interrupt를 무시하는 옵션
ex) tee -a 파일명
```

## 아카이브

```bash
tar
아카이브 파일 관리 도구
- 현재 작업 위치에서 사용됨(경로를 지정해서 작업 불가)
- 현재 위치에 같은 파일이 있을 경우 물어보지 않고 파일을 덮어씀

아카이브 파일
단순한 의미로 파일의 묶음(압축 X)
- 용량을 감소시켜주지 않음

tar	[옵션]	[옵션]	[옵션]	파일명
	  c	f(필수) z
	  x		   j
	  t		   J

옵션
-c : 아카이브 파일을 만드는 옵션
-x : 원본 파일을 추출하는 옵션
-t : 묶여있는 파일의 목록을 확인하는 옵션
-f : 파일의 이름을 지정하는 옵션(필수)
-z : gzip 방식으로 파일을 압축하거나 추출할 때 사용
-j : bzip2 방식으로 파일을 압축하거나 추출할 때 사용
-J : xz 방식으로 파일을 압축하거나 추출할 때 사용

tar 실습을 위한 선행 작업
# rm -rf *
# touch fileA fileB fileC

아카이브 파일 생성
# tar cf file.tar fileA fileB fileC
- .tar 확장자를 빼고 만들 수 있으나 식별이 어려운 관계로 .tar 확장자를 붙여줌

아카이브 파일 추출
# tar xf file.tar

아카이브 파일 목록 확인
# tar tf file.tar

아카이브 파일 생성 및 gzip 압축
# tar cfz file.tar.gz fileA fileB fileC

gzip 파일을 추출
# tar xfz file.tar.gz

팁)
tar 옵션을 사용할 때 대시(-) 를 붙여서 사용해도 되고 붙이지 않고 사용해도 됨
- 대시(-) 사용시에는 옵션의 순서를 지켜줘야 함
- 대시(-) 미사용시에는 옵션의 순서를 지켜주지 않아도 됨
 - 대시 사용 유무에 큰 의미는 없음
```

