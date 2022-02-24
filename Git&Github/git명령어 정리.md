# Git & Github 기본 사용법

## Git 기본 명령어

  ```bash
  # 디렉토리 생성
  mkdir
  # 디렉토리 이동
  cd
  # 파일을 생성
  touch
  # 디렉토리 안 리스트를 확인
  ls
  # 제거
  rm
  ## -r 옵션 : 재귀적 
  ## -rf 옵션 : 강제 삭제
  # 이동/이름변경
  mv
  # 현재의 경로를 보여줌
  pwd
  # 화면 깨끗이/스크롤 올리기
  clear
  ctrl + l 
  ```
---

## Github 사용을 위한 명령어 정리

### 1. basic

```bash
# 작성자 이름, 메일 등록 (최초 1번만 실행)
git config --global user.name "github username"
git config --global user.email "github email"

# config 정보 출력
git config --global --list

# 일반 폴더 -> 로컬 저장소
git init

# 버전 상태 출력
git status

# Working Directory -> Staging Area
git add [File]
git add .  # 모든 파일 add

# add한 파일 취소하고싶을 때
git rm --cached [File]

# Staging Area -> Commits
git commit -m "commit message"

# commits 목록 출력
git log
git log --oneline  # 한줄로 보기 옵션
git log -p  # 커밋마다 차이 보기 옵션
```

### 2. remote

```bash
# 로컬 저장소와 원격 저장소를 연결
git remote add origin [Github repository URL]

# 연결된 원격 저장소 목록 조회
git remote -v

# 원격 저장소 연결 삭제
git remote rm origin
git remote remove origin

# 로컬 저장소의 commits을 원격 저장소에 반영
git push origin master
git push -u origin master  # -u 옵션을 했다면 이후 push할 때는 git push만으로도 가능

# 원격 저장소를 로컬에 복제
git clone [Github repository URL]

# 원격 저장소의 변경 사항 로컬에 받아오기 (동기화)
git pull origin master
```

### 3. reset, revert

```bash
# 특정 커밋 상태로 되돌리기 (soft, mixed, hard 세 가지 옵션)
git reset --soft [commit ID]
git reset --mixed [commit ID]
git reset --hard [commit ID]

# 커밋을 취소하는 커밋을 새로 생성하여 특정 커밋을 되돌리기
git revert [commit ID]

# 이전 커밋 목록 모두 출력
git reflog
```

### 4. branch, merge

```bash
# 브랜치 목록 확인
git branch

# 새 브랜치 생성
git branch [branch name]

# 특정 브랜치 삭제
git branch -d [branch name]
git branch -D [branch name]  # 강제 삭제(병합되지 않은 브랜치도 삭제)

git switch [branch name]  # 다른 브랜치로 이동
git switch -c [branch name]  # 브랜치를 생성함과 동시에 이동

# 한 줄로, 모든 브랜치의, 그래프를 포함하여 커밋 목록 출력
git log --oneline --all --graph

# 브랜치 병합
git merge [branch name]
```

---



# Git 관련 팁

## .gitignore 파일

touch .gitignore 으로 만든 파일안에 깃으로 관리하고싶지 않은 파일명을 넣으면 제외된다.

### .gitignore 파일 사용을 편하게 해줄 사이트

https://www.toptal.com/developers/gitignore

- **설명 & 사용방법**

  -  .gitignore 파일안에 넣지않을 확장자들을 검색창에 이름(python, jupoyternotebook  등)들 넣어서 검색해서 나오는 내용들을 위부터 아래까지 전체복사해서 .gitignore 파일안에 넣으면 관련 푸쉬할 필요없는 파일들 알아서 제외해주는 사이트



## README.md 

README.md 파일을 만들어서 Github repository 에 보내면 Wiki로 만들 수 있다.



## 팁

깃허브에서는 파일들 수정하지말기



