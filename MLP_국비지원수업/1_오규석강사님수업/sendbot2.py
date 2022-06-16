from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SendBot:
    def __init__(self):
        self.query = "https://www.instagram.com/explore/tags/"
        self.options = Options()
        self.options.add_argument("--window-size=1920, 1080")
        self.driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe", chrome_options=self.options)
        
    def login(self, id, pw):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(6)
        user_input = self.driver.find_elements_by_tag_name("input")
        user_input[0].send_keys(id)        
        user_input[1].send_keys(pw)
        user_input[1].send_keys(Keys.RETURN)
        time.sleep(6)
    
    def search_tag(self, tag):
        self.driver.get(self.query+tag)
        time.sleep(6)
        
    def first_photo_click(self):
        first_xpath = '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]'
        el = self.driver.find_element_by_xpath(first_xpath)
        el.click()
        time.sleep(6)
        
    def comment(self, contents, num):
        count = num
        while count != 0:
            # 댓글 창 클릭(일단 보류)
            #comment_xpath = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea'
            #el = self.driver.find_element_by_xpath(comment_xpath)
            #el.click()
            #time.sleep(2)

            # 댓글달기
            tag_textarea = self.driver.find_element_by_tag_name("textarea")
            tag_textarea.send_keys(contents)

            button_path = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button'
            button = self.driver.find_element_by_xpath(button_path)
            button.click()

            time.sleep(5)           
            
            # 다음 게시물로 이동 버튼 클릭
            next_xpath = '/html/body/div[6]/div[2]/div/div[2]/button'
            next_el = self.driver.find_element_by_xpath(next_xpath)
            next_el.click()
            time.sleep(5)
            
            count -= 1
            
    def mix(self, tag, contents, num):
        self.search_tag(tag)
        self.first_photo_click()
        self.comment(contents, num)
        
    def kill():
        self.driver.quit()   