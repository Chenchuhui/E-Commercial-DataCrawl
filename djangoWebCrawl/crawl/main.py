from stage_1 import kikuu, kilimall, fix, jjshouse, lovelywholesale, valueco, wholesale7, \
    dealhub, snatcher, jumia
from alibaba import stage2,stage3
import time
import multiprocessing


tableList = ['kikuu', 'kilimall', 'fix', 'jjhouse', 'lovelywholesale', 'valueco', 'wholesale7', 'dealhub',
             'snatcher', 'jumia']


# 得到日期
def get_date():
    date = time.strftime('%Y-%m-%d')
    return date


def firstStage(pack, db, table, **kwargs):
    print(f'{table}的一阶段开始,当前日期为{get_date()}')
    pack.main(db, table, **kwargs)


def secondStage(offer, db, table,img_path):
    print(f'{table}的二阶段开始,当前日期为{get_date()}')
    stage2.main(offer, db, table, img_path)


def thirdStage(cookies, db, table):
    print(f'{table}的三阶段开始,当前日期为{get_date()}')
    stage3.main(cookies, db, table)


if __name__ == '__main__':
    db = 'mysql02'

    while True:
        try:
            stage = int(input('Please Enter the stage you want to process:'))
            if stage not in [1, 2 ,3]:
                raise ValueError
            break
        except:
            print("Please enter the integer.")

    while True:
        try:
            table = input('Please enter the website you want to process:')
            if table not in tableList:
                raise ValueError
            break
        except ValueError:
            print("Website in not valid!")

    if stage == 1:
        if table == 'kilimall':
            category = input("Please select from [kitchen_supply, men_shoe, women_bag]:")
            if category not in ['kitchen_supply', 'men_shoe', 'women_bag']:
                print("Invalid input, please retry")
            firstStage(kilimall, db, table, category=category)
        elif table == 'kikuu':
            firstStage(kikuu, db, table)
        elif table == 'valueco':
            firstStage(valueco, db, table)
        elif table == 'snatcher':
            firstStage(snatcher, db, table)
        elif table == 'jumia':
            firstStage(jumia, db, table)

    elif stage == 2:
        accessToken = input('Please enter the updated access token:')
        stage2.main(stage2.offer(accessToken), db, table, f'../media/{table}_img')

    elif stage == 3:
        _m_h5_tk = input("Please enter the updated _m_h5_tk cookie:")
        _m_h5_tk_enc = input("Please enter the updated _m_h5_tk_enc cookie:")
        cookies = {'_m_h5_tk': _m_h5_tk,
                   '_m_h5_tk_enc': _m_h5_tk_enc}
        stage3.main(cookies, db, table)