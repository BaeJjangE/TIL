# 인자를 받기 위해 sys 모듈 import
import sys

# 디렉토리를 만들기 위해 os 모듈 import
import os

# insta_bot_like 모듈 import
import insta_bot_like as ib

# 아이디를 입력
id = sys.argv[1]

# 패스워드를 입력
ps = sys.argv[2]

# 태그 입력
tag = sys.argv[3]
  
# 반복할 횟수 입력
NUMBER = int(sys.argv[4].strip())

# 크롤러 호출
BOT = ib.LikeBot()

# 인스타에 로그인
BOT.login(id, ps)

# 태그 검색
BOT.search_tag(tag)
        
# 사진 첫 장을 선택하고
BOT.select_picture()
        
# 캡쳐를 하면서 한 장씩 넘기기
BOT.press_like(NUMBER)

# 하나로 묶은 매크로 사용
# BOT.insta_jungbok(tag, NUMBER)

# 작업 완료 후 크롤러 종료
BOT.kill()