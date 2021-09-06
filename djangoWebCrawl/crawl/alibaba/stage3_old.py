from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Slide_Verify import slide_verify
import re
from sql import mysql


def webdriver_settings():
    chrome_debug_port = 9999
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{chrome_debug_port}")
    browser = webdriver.Chrome(options=chrome_options)

    browser.set_page_load_timeout(35)
    browser.set_script_timeout(35)
    return browser


def convert_percentToFloat(str_text):
    str_text = str_text[:-1]
    print(str_text)
    convert_float = float(str_text) / 100
    return convert_float


def decodeSpecialChar(str_text):
    if str_text[-1] == '+':
        str_text = str_text[:-1]
    elif str_text[-1] == '万':
        str_text = str_text + '0000'

    str_text = float(str_text)
    return str_text


def convertWeightToFloat(str_text):
    idx = str_text.find(' ')
    str_text = float(str_text[:idx])
    return str_text


conn = mysql.SQL("KIKUU", "KIKUU_DATA")
conn.enter_database()
conn.enter_table()
link_tuple = conn.query_data("1688_url")
browser = webdriver_settings()
sv = slide_verify()
for link in link_tuple:
    link = link[0]
    print(link)
    browser.get(link)
    flag = sv.test_slide(browser)

    while(True):
        print("The current page is at the status", flag)
        if flag == 1:
            sv.big_run(browser)
            flag = sv.test_slide(browser)
        elif flag == 2:
            sv.small_run(browser)
            flag = sv.test_slide(browser)
        elif flag == 3:
            sv.login_run(browser)
            flag = sv.test_slide(browser)
        else:
            break

    try:
        huitou = browser.find_element_by_xpath('//span[@class="description-show-ht description-value-ht"]').text
        huitou = convert_percentToFloat(huitou)
    except:
        huitou = 0

    # 获取供应商信息
    try:
        data = browser.find_element_by_xpath('//div[@class="app-topbar app-type-default  "]')
        offer_content = data.get_attribute("data-view-config")
        offer_result = re.findall(r'"score":(.*?),"serviceKey"', offer_content, re.S)
        try:
            caigou = float(offer_result[0][1:][:-1])
        except:
            caigou = 0
        try:
            wuliu = float(offer_result[1][1:][:-1])
        except:
            wuliu = 0
        try:
            tuihuan = float(offer_result[2][1:][:-1])
        except:
            tuihuan = 0
        try:
            jiufen = float(offer_result[3][1:][:-1])
        except:
            jiufen = 0
        try:
            pingzhi = float(offer_result[4][1:][:-1])
        except:
            pingzhi = 0

    except:
        caigou = 0
        wuliu = 0
        tuihuan = 0
        jiufen = 0
        pingzhi = 0

    # 30天内成交量
    try:
        chengjiao = browser.find_element_by_xpath('//p[@class="bargain-number"]/em').text
        chengjiao = decodeSpecialChar(chengjiao)
    except:
        chengjiao = 0

    try:
        weight = browser.find_element_by_xpath('//dd[@class="fd-clr"]//em').text
        weight = convertWeightToFloat(weight)
    except:
        weight = 0

    try:
        review = browser.find_element_by_xpath('//a[@trace="tabcomment"]//em').text
        review = review[1:][:-1]
        review = decodeSpecialChar(review)
    except:
        review = 0

    if review == 0:
        positive_rate = 0
        product_rate = 0
    else:
        try:
            browser.find_element_by_xpath('//a[@trace="tabcomment"]').click()
            positive_rate = browser.find_element_by_xpath('//span[@class="positive-rate"]').text
            positive_rate = convert_percentToFloat(positive_rate)
        except:
            positive_rate = 0
        try:
            product_rate = browser.find_element_by_xpath('//span[@class="star-score"]').text
            product_rate = float(product_rate)
        except:
            product_rate = 0

    col_name = ["回头率", "采购咨询", "物流时效", "退换体验", "纠纷解决", "品质体验", "30天内成交量", "跨境包裹重量", "评价数目", "好评率", "货品评分"]
    data = [huitou, caigou, wuliu, tuihuan, jiufen, pingzhi, chengjiao, weight, review, positive_rate, product_rate]
    conn.update_table(col_name,data,"1688_url",link)
