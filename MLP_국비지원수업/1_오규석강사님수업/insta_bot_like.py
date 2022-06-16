# 브라우저를 제어하기 위해 selenium 모듈의 webdriver를 import
from selenium import webdriver

# 브라우저를 옵션을 이용해서 활성화시키기 위해 Options를 import
from selenium.webdriver.chrome.options import Options

# 클릭과 캡쳐를 위해 keys를 import
from selenium.webdriver.common.keys import Keys

# 작업과 작업 사이에 딜레이를 주기 위해 time 모듈을 import
import time

class LikeBot:
    def __init__(self):
        
        # 홈페이지를 변수에 저장
        self.querry = "https://www.instagram.com/explore/tags/"
        
        # 셀레늄 웹드라이버에 입력할 옵션을 지정
        self.options = Options()
        
        # 옵션에 해상도를 입력
        self.options.add_argument("--window-size=1920, 1080")
        
        # 화면이 존재하지 않는 서버에서 사용한다면 해상도 입력 옵션 사용 X
        # ex) 리눅스 cli 서버, 우분투 서버
        # 아래 headless 옵션을 사용
        # self.options.add_argument("headless")
        
        # 크롬 드라이버 실행
        self.driver = webdriver.Chrome(
            executable_path="chromedriver_win32/chromedriver.exe",
            chrome_options=self.options)
        
    # 크롤러 종료 메서드
    def kill(self):
        self.driver.quit()
        
    # 스크린샷 메서드
    # html 요소를 가지고 스크린샷을 하는 것이 아닌 전체를 스크린샷
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        
    # 인스타그램 로그인 메서드
    def login(self, id, ps):
        
        # 로그인 페이지로 이동
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(5)
        
        # 아이디와 패스워드 입력을 위해 <input> 태그 찾기
        input_field = self.driver.find_elements_by_tag_name("input")
        
        # 첫 번째 요소 아이디를 입력
        input_field[0].send_keys(id)
        
        # 두 번째 요소 패스워드를 입력
        input_field[1].send_keys(ps)
        
        # 엔터키를 눌러 로그인 마무리
        input_field[1].send_keys(Keys.RETURN)
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(5)
        
    # 인스타그램 태그 검색 메서드
    def search_tag(self, tag):
        
        # 위에서 지정한 URL 주소와 태그를 결합해서 브라우저를 열어줌
        self.driver.get(self.querry + tag)
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(5)
        
    # 최근 게시물 첫 번째 사진을 선택하여 클릭하는 메서드
    def select_picture(self):
        
        # 최근 게시물의 위치를 recent_picture_xpath에 지정
        recent_picture_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]'
        
        # recent_picture_xpath의 요소를 가져와서 저장
        recent_picture = self.driver.find_element_by_xpath(recent_picture_xpath)
        
        # 최근 게시물 클릭
        recent_picture.click()
        
        # 다음 동작을 위해 딜레이 시간 부여
        time.sleep(5)
    
    # 게시물들을 돌아다니면서 '좋아요' 버튼을 누르는 메서드
    # num 변수에 몇 번 반복할 것인지를 저장
    # -1 을 입력하면 직접 종료하기 전까지 무한정으로 계속 '좋아요' 버튼 클릭
    def press_like(self, num):
        
        # 반복할 횟수를 count에 저장
        count = num
        
        # count가 0이 될때까지 계속 반복
        # num에 -1이 들어오게 되면 무한 반복
        while count != 0:
            
            # "좋아요"가 포함된 태그를 기반으로 찾기
            # <svg> 태그를 가진 모든 요소를 저장
            like_button = self.driver.find_elements_by_tag_name("svg")
            
            # <svg> 태그 내부에 aria-label이라는 어트리뷰트(속성)를 가지고 "좋아요"를 가진 경우에만 클릭
            # "좋아요 취소" 일 경우에는 클릭 X

            list_like = []
            for ele in like_button:
                if ele.get_attribute("aria-label") == "좋아요":
                    list_like.append(ele)

            list_like[1].click()
        
            # 다음 게시물로 넘어감
            next_button = '/html/body/div[6]/div[2]/div/div[2]/button/div/span'            
            next_button_element = self.driver.find_element_by_xpath(next_button)
            next_button_element.click()

            count -= 1
            
            # 다음 동작을 위해 딜레이 시간 부여
            time.sleep(5)   
                
    # 검색, 좋아요를 하나로 묶은 매크로 만들기
    # tag, num 변수 필요 <---- 위에 메서드에서 찾기
    # 10장 캡쳐
    def insta_jungbok(self, tag, num):
        
        # 태그 검색도 하고
        self.search_tag(tag)
        
        # 사진 첫 장을 선택하고
        self.select_picture()
        
        # 좋아요를 하면서 한 장씩 넘기기
        self.press_like(num)