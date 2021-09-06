from stage_1 import kikuu,fix,lovelywholesale,wholesale7,jjshouse, kilimall, dealhub
from alibaba import stage2,stage3
import apscheduler
import time

def get_date():
    date=time.strftime('%Y-%m-%d')
    return date


def get_kikuu(cookies,access_token):
    table = "kikuu"
    img_path='../media/kikuu_img'
    offer = stage2.offer(access_token)
    print(f'kikuu的一阶段开始,当前日期为{get_date()}')
    kikuu.main(db, table)
    print(f'kikuu的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table,img_path)
    print(f'kikuu的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies,db,table)


def get_fix(cookies,access_token):
    table = "fix"
    img_path='../media/fix_img'
    offer = stage2.offer(access_token)
    print(f'fix的一阶段开始,当前日期为{get_date()}')
    fix.main(db, table)
    print(f'fix的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table,img_path)
    print(f'fix的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies,db,table)


def get_lovelywholesale(cookies,access_token):
    table = "lovelywholesale"
    img_path='../media/lovelywholesale_img'
    offer = stage2.offer(access_token)
    print(f'lovelywholesale的一阶段开始,当前日期为{get_date()}')
    lovelywholesale.main1(db, table)
    print(f'lovelywholesale的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table,img_path)
    print(f'lovelywholesale的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies,db,table)


def get_wholesale7(cookies,access_token):
    table = "wholesale7"
    img_path='../media/wholesale7_img'
    offer = stage2.offer(access_token)
    print(f'wholesale7的一阶段开始,当前日期为{get_date()}')
    wholesale7.main1(db, table)
    print(f'wholesale7的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table,img_path)
    print(f'wholesale7的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies,db,table)


def get_jjshouse(cookies,access_token):
    table = "jjshouse"
    img_path='../media/jjshouse_img'
    offer = stage2.offer(access_token)
    print(f'jjshouse的一阶段开始,当前日期为{get_date()}')
    jjshouse.main(db, table)
    print(f'jjshouse的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table,img_path)
    print(f'jjshouse的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies,db,table)

def get_dealhub(cookies,access_token):
    table = "dealhub"
    img_path='../media/dealhub_img'
    offer = stage2.offer(access_token)
    print(f'dealhub的一阶段开始,当前日期为{get_date()}')
    # dealhub.main(db, table)
    print(f'dealhub的二阶段开始,当前日期为{get_date()}')
    # stage2.main(offer, db, table,img_path)
    print(f'dealhub的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies,db,table)

def get_kilimall(cookies, access_token):
    table = "kilimall"
    img_path = '../media/kilimall_img'
    offer = stage2.offer(access_token)
    print(f'kilimall的一阶段开始,当前日期为{get_date()}')
    kilimall.main(db, table, 'kitchen_supply')
    kilimall.main(db, table, 'men_shoe')
    kilimall.main(db, table, 'women_bag')
    print(f'kilimall的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table, img_path)
    print(f'kilimall的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies, db, table)


if __name__=='__main__':
    db = "mysql02"
    cookies = {'_m_h5_tk': 'bb7d635aa926f208c8fbafa5fe1c5594_1630482427928',
               '_m_h5_tk_enc': '82c934be95355daa3892b2d7b395bf20'}
    access_token = "497c495a-dc77-4608-8cac-3def76e1b81d"

    # get_kikuu(cookies,access_token)
    # get_fix(cookies, access_token)
    # get_kilimall(cookies, access_token)
    get_dealhub(cookies, access_token)
    # get_lovelywholesale(cookies, access_token)