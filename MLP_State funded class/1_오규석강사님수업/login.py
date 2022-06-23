import sys
import login_macro as lm

# 로그인 할 사이트를 입력받기
site = sys.argv[1]

# 아이디 입력받기
id = sys.argv[2]

# 패스워드 입력받기
ps = sys.argv[3]

# lm 모듈에 있는 클래스를 객체화
crawler = lm.LoginBot(site)

# 로그인
crawler.login(id, ps)