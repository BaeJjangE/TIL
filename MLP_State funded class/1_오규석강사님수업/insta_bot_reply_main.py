# 인자를 받기 위해 sys 모듈 import
import sys

# 디렉토리를 만들기 위해 os 모듈 import
import os

# insta_bot_capture 모듈 import
import insta_bot_reply as ib

# 아이디를 입력
id = sys.argv[1]

# 패스워드를 입력
ps = sys.argv[2]

# 태그 입력
tag = sys.argv[3]

# 입력할 댓글이 저장된 파일을 입력
replyfile = sys.argv[4]

# 반복할 횟수 입력
NUMBER = int(sys.argv[5].strip())

# 크롤러 호출
BOT = ib.ReplyBot(replyfile)

# 인스타에 로그인
BOT.login(id, ps)

# 태그 검색
BOT.search_tag(tag)
        
# 사진 첫 장을 선택하고
BOT.select_picture()
        
# 좋아요를 하면서 댓글을 입력하고 한 장씩 넘기기
BOT.press_like_and_reply(NUMBER)

# 하나로 묶은 매크로 사용
# BOT.insta_jungbok(tag, NUMBER)

# 작업 완료 후 크롤러 종료
BOT.kill()