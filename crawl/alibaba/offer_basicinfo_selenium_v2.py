import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Slide_Verify import slide_verify
import pandas as pd
import csv
import re
from queue import Queue



# from selenium.webdriver.common.action_chains import ActionChains



class seleniumbasicinfo(object):

    def __init__(self):
        self.urlQueue = Queue()

    def webdriver_settings(self):

        #os.system(r'chrome.exe --remote-debugging-port=9999 --user-data-dir="C:\selenium\AutomationProfile"')
        chrome_debug_port = 9999
        chrome_options = Options()
        # chrome_options.add_argument('--user-data-dir="C:\selenum\AutomationProfile"')

        #chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{chrome_debug_port}")
        #,executable_path="C:\\selenium\\AutomationProfile\\chromedriver.exe"
        browser = webdriver.Chrome(chrome_options=chrome_options)
        #browser.maximize_window()

        browser.set_page_load_timeout(35)
        browser.set_script_timeout(35)

        current_handle = browser.current_window_handle


        # 所有句柄
        all_handle = browser.window_handles
        second_handle = all_handle[-1]

        # 切回first
        browser.switch_to.window(current_handle)
        return browser

    def get_offers_url_from_csv(self,csv_path):
        offers_url = []
        df=pd.read_csv(csv_path,header=0)
        data=pd.DataFrame(df)
        for i in range(len(data)):
            offers_url.append(df["offer_url"][i])
        return offers_url


    #本函数用于获取商品页中所需的商品信息
    def get_target_data_from_goodurl(self,offer_url):
        driver = self.webdriver_settings()
        sv=slide_verify()
        try:
            driver.get(offer_url)
            result=sv.test_slide(driver)
            if result!=0:
                print(f"出现验证，为第{result}类")
            if result==1:
                sv.big_run(driver)
            elif result==2:
                sv.small_run(driver)
            elif result==3:
                sv.login_run(driver)
            else:
                pass

        except Exception as e:
            print(str(e))
            driver.execute_script('window.stop()')

            # temp={}
            # temp["回头率"] = None
            # temp["采购咨询"] = None
            # temp["物流时效"] = None
            # temp["退换体验"] = None
            # temp["纠纷解决"] = None
            # temp["品质体验"] = None
            # temp["30天内成交量"] = None
            # temp["跨境包裹重量"] = None
            # temp["评价数目"] = None
            # temp["好评率"] = None
            # temp["货品评分"] = None
            # driver.quit()
            # return temp

        temp={}
        try:
            huitou=driver.find_element_by_xpath('//span[@class="description-show-ht description-value-ht"]')
            temp["回头率"]=huitou.text
        except:
            temp["回头率"] = None
        try:
            data = driver.find_element_by_xpath('//div[@class="app-topbar app-type-default  "]')
            content=data.get_attribute("data-view-config")

            result = re.findall(r'"score":(.*?),"serviceKey"', content, re.S)
            temp["采购咨询"] = float(result[0][1])
            temp["物流时效"] = float(result[1][1])
            temp["退换体验"] = float(result[2][1])
            temp["纠纷解决"] = float(result[3][1])
            temp["品质体验"] = float(result[4][1])
        except:
            temp["采购咨询"] = None #设置成0
            temp["物流时效"] = None
            temp["退换体验"] = None
            temp["纠纷解决"] = None
            temp["品质体验"] = None

        try:
            bargain_num =driver.find_element_by_xpath('//p[@class="bargain-number"]/em')
            temp["30天内成交量"]=bargain_num .text
        except:
            temp["30天内成交量"]=None


        try:
            weight= driver.find_element_by_xpath('//dd[@class="fd-clr"]//em')
            temp["跨境包裹重量"]=weight.text
        except:
            temp["跨境包裹重量"]=None

        try:
            Review = driver.find_element_by_xpath('//a[@trace="tabcomment"]//em')
            temp["评价数目"]=Review.text #转换成int
        except:
            temp["评价数目"]=None

        try:
            driver.find_element_by_xpath('//a[@trace="tabcomment"]').click()
        except:
            print("没有评价页面")

        try:
            postive_rate = driver.find_element_by_xpath('//span[@class="positive-rate"]')
            temp["好评率"]=postive_rate.text #转换成int
        except:
            temp["好评率"] =None #0
        try:
            star=driver.find_element_by_xpath('//span[@class="star-score"]')
            temp["货品评分"]=star.text
        except Exception as e:
            temp["货品评分"] = None

        driver.quit()
        return temp

    def main(self,offer_path,temp2_path):

        tempcsv = open(temp2_path, 'w+',encoding='utf-8', newline='')
        head = ["回头率", "采购咨询", "物流时效", "退换体验", "纠纷解决", "品质体验", "货品评分", "30天内成交量", "好评率", "评价数目", "跨境包裹重量"]
        writer = csv.DictWriter(tempcsv, head)
        writer.writeheader()

        offer_urls=self.get_offers_url_from_csv(offer_path)

        for offer_url in offer_urls:

            try:

                temp = self.get_target_data_from_goodurl(offer_url)
                writer.writerow(temp)
                print(f"已成功写入{offer_url}")
                print(temp)

            except Exception as e:
                temp={"回头率":None,"采购咨询":None,"物流时效":None,"退换体验":None,"纠纷解决":None,"品质体验":None,"30天内成交量":None,"好评率":None,"货品评分":None,"评价数目":None, "跨境包裹重量":None}
                writer.writerow(temp)
                print(str(e))
                print(f"写入失败{offer_url}")
        tempcsv.close()



# if __name__ == '__main__':
#     ss=seleniumbasicinfo()
#     offer_path="C:\\Users\\claude\\Desktop\\test.csv"
#     temp_path="C:\\Users\\claude\\Desktop\\test_final.csv"
#     ss.main(offer_path,temp_path)