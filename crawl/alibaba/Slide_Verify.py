from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import random
import numpy as np
from pynput.keyboard import Key, Controller as c2
from pynput.mouse import Button, Controller as c1

import time
import ssl
import json


class slide_verify(object):
    # def __init__(self):
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option("excludeSwitches", ["enable-automation"])
    #     options.add_experimental_option('useAutomationExtension', False)
    #
    #     options.add_argument("--disable-blink-features=AutomationControlled")
    #     options.add_argument(
    #         "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")
    #     driver = webdriver.Chrome(options=options)
    #     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    #     driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    #         "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    #     driver.maximize_window()
    #     self.driver=driver
    def webdriver_settngs(self):
        # os.system(r'C:\Users\claude/chrome.exe --remote-debugging-port=9999 --user-data-dir="C:\selenum\AutomationProfile"')
        chrome_debug_port = 9999
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{chrome_debug_port}")

        browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser.set_page_load_timeout(10)
        current_handle = browser.current_window_handle
        all_handle = browser.window_handles
        second_handle = all_handle[-1]
        # 切回first
        browser.switch_to.window(current_handle)
        return  browser

    def ease_out_quad(self,x):

        return 1 - (1 - x) * (1 - x)

    def ease_out_quart(self,x):

        return 1 - pow(1 - x, 4)

    def ease_out_expo(self,x):

        if x == 1:

            return 1

        else:

            return 1 - pow(2, -10 * x)

    def get_track(self,distance, seconds, ease_func):

        tracks = [0]

        offsets = [0]

        for t in np.arange(0.0, seconds, 0.05):
            ease =ease_func

            offset = round(ease(t / seconds) * distance)

            tracks.append(offset - offsets[-1])

            offsets.append(offset)
        if offsets[-1] != 258:
            offsets.append(258)
            tracks.append(258-offsets[-1])


        return offsets, tracks



    # def get_track(self, distance, t):  # distance为传入的总距离，a为加速度
    #     track = []
    #     current = 0
    #     mid = distance * 3/5
    #     v = 0
    #     while current < distance:
    #         if current < mid:
    #             a = 2
    #         else:
    #             a = -3
    #         v0 = v
    #         v = v0 + a * t
    #         move = v0 * t + 1 / 2 * a * t * t
    #         rest=distance-current
    #         if move<rest:
    #             current += move
    #         else:
    #             move=rest
    #             current += move
    #         track.append(round(move))
    #     return track


    def move_to_gap(self, driver,slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹
        ActionChains(driver).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
        ActionChains(driver).pause(1).release().perform()

    #
    # def pynput_small_slide(self,driver):
    #     mouse=c1()
    #
    #     time.sleep(3)
    #     mouse.position = (52, 203)
    #     mouse.press(Button.left)
    #     mouse.move(310, 203)
    #     mouse.release(Button.left)
    #     time.sleep(1)
    #
    #     try:
    #         driver.find_element_by_xpath("//span[contains(@data-nc-lang,'_error300')]")
    #         return False
    #     except:
    #         try:
    #             driver.find_element_by_xpath("//span[contains(@id, 'nc_1_n1z')]")
    #             return False
    #         except:
    #             return True

    def test_slide(self,driver):

        try:
            driver.find_element_by_xpath("//div[contains(@id, 'nc_1__bg')]")
            return 1
        except:
            try:
                iframe = driver.find_element_by_xpath('//iframe[@id="sufei-dialog-content"]')
                driver.switch_to.frame((iframe))
                try:
                    driver.find_element_by_xpath("//form[contains(@id, 'login-form')]")
                    return 3
                except:
                    driver.find_element_by_xpath("//div[contains(@id, 'nc_1__bg')]")
                    return 2
            except:
                return 0



    def operation_small_slide(self, driver):


        time1 = [0.5, 0.15, 0.45, 1.25, 1.15, 0.75,0.3,0.5,0.35,0.25,0.15,0.7]
        #quad更适合偶数时间
        #time1 = []
        #quart更适合奇数时间
        #time1 = [0.5,0.45,1.25,1.15,1.35,0.75,0.25,0.35,0.3,0.65,0.7,0.85,0.75,0.45]
        # time1=[2,3,4,4.5,5,3.5,2.5]
        t1 = random.choice(time1)
        print(f"本次挑选的时间是{t1}")
        try:

            try:
                iframe = driver.find_element_by_xpath('//iframe[@id="sufei-dialog-content"]')
                driver.switch_to.frame(iframe)
            except:
                pass
            slider = driver.find_element_by_xpath("//span[contains(@id, 'nc_1_n1z')]")
            offsets, tracks=self.get_track(258, t1,self.ease_out_expo)
            print(f"offsets是{offsets}")
            print(f"tracks是{tracks}")
            tracks=[258]
            self.move_to_gap(driver,slider,tracks)
        except Exception as e:
            print(str(e))
            print("本次滑动失败，将再次尝试")


        try:
            driver.find_element_by_xpath("//span[contains(@data-nc-lang,'_error300')]")
            driver.refresh()
            return False
        except:
            try:
                driver.find_element_by_xpath("//span[contains(@id, 'nc_1_n1z')]")
                driver.refresh()
                return False
            except:
                # with open('right_t1.txt','a+',encoding='utf-8') as f:
                #     f.write(str(t1))
                #     f.write('\n')
                return True

    def operation_big_slide(self, driver):
        time1=[1,1.1,1.2,0.9,1.3,1,0.8,0.6,0.7]
        t1 = random.choice(time1)
        print(f"本次挑选的时间是{t1}")

        try:

            slider = driver.find_element_by_xpath("//div[contains(@id,'nc_1__bg')]")
            offsets, tracks=self.get_track(258, t1,self.ease_out_quart)
            print(f"offsets是{offsets}")
            print(f"tracks是{tracks}")
            #tracks=self.get_track(258,t1)
            tracks = [258]
            self.move_to_gap(driver,slider,tracks)
        except Exception as e:
            print(str(e))
            print("本次滑动失败，将再次尝试")

        try:
            driver.find_element_by_xpath("//span[contains(@data-nc-lang,'_error300')]")
            driver.refresh()
            return False
        except:
            try:
                driver.find_element_by_xpath("//span[contains(@id, 'nc_1_n1z')]")
                driver.refresh()
                return False
            except:
                return True


    def big_run(self, driver):
        result=False
        while not result:
            try:
                result = self.operation_big_slide(driver)
                print(result)
            except Exception as e:
                print(str(e))
    def small_run(self,driver):
        result=False
        while not result:
            try:
                #result = self.operation_small_slide(driver)
                result = self.operation_small_slide(driver)
                print(result)
            except Exception as e:
                print(str(e))
    def login_run(self,driver):
        driver.find_element_by_xpath('//input[@name="fm-login-id"]').send_keys('18918902959')
        driver.find_element_by_xpath('//input[@name="fm-login-password"]').send_keys('fudan0206')
        driver.find_element_by_xpath('//button[@type="submit"]').click()
