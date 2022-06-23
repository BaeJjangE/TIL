from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time

# 사이트의 로그인 주소를 미리 저장
LOGIN_URLS = {
    "daum" : "https://logins.daum.net/accounts/signinform.do",
    "naver" : "https://nid.naver.com/nidlogin.login?"
}

class LoginBot:
    def __init__(self, site):
        # 셀레늄 웹드라이버에 입력할 옵션을 지정
        self.options = Options()
        # 옵션에 해상도를 입력
        self.options.add_argument("--window-size=1920, 1080")
        # 옵션을 이용하여 크롬 웹드라이버를 불러옴
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe",
                                 chrome_options=self.options)
        # 로그인하려는 사이트로 이동해 로그인창을 켬
        try:
            self.driver.get(LOGIN_URLS[site.lower()])   # TWITTER  -> twitter
            # 로딩이 오래 걸릴 것을 대비하여 잠시 대기
            time.sleep(7)
        except KeyError:
            # 세팅되지 않은 주소가 나올 경우 주소창에 입력하게 함
            self.driver.get(site)
            # 로딩이 오래 걸릴 것을 대비하여 잠시 대기
            time.sleep(7)
        
    # 로그인 메서드
    def login(self, id, ps):
        # 아이디 입력
        pw.typing(id)
        # 비밀번호 입력을 위해 탭 키 사용
        pw.key_press_once("tab")
        # 비밀번호 입력
        pw.typing(ps)
        # 로그인을 위한 엔터키 사용
        pw.key_press_once("enter")
        # 로딩이 오래 걸릴 것을 대비하여 잠시 대기
        time.sleep(7)
        
    # 크롤러 종료 메서드
    def kill(self):
        self.driver.quit()