import requests
import pandas as pd
import threading

class checkexist(object):
    def __init__(self):
        df=pd.read_excel(r'C:\Users\claude\Desktop\独立站.xlsx',header=[0])
        col_name=df.columns.tolist()
        col_name.insert(1, 'is_exist')
        df=df.reindex(columns=col_name)
        self.df=df
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

    def main(self,start_index,end_index):
        for i in range(start_index,end_index):
            try:
                response=requests.get('https://'+self.df['url'][i],headers=self.headers,timeout=25)
                self.df['is_exist'][i]=response.status_code
                print(response.status_code)
            except:
                self.df['is_exist'][i]=404

if __name__=='__main__':
    cx=checkexist()
    df=cx.df
    threads = []
    threadNum = 4
    start_idx = []
    end_idx = []
    increment = int(len(df)/ threadNum)

    for i in range(threadNum):
        start_idx.append(increment * i)
        if i == threadNum - 1:
            end_idx.append(len(df))
        else:
            end_idx.append(increment * (i + 1))

    for i in range(1, threadNum + 1):
        threads.append(
            threading.Thread(target=cx.main, args=(start_idx[i - 1], end_idx[i - 1],)))
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    df.to_excel(r'C:\Users\claude\Desktop\独立站1.xlsx')