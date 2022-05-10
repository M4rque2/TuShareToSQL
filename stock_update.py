import tushare as ts
import pandas as pd

from time import sleep
from datetime import datetime
from config import mysql_engine as engine

pro = ts.pro_api()
start_date = '2009-01-01'
today = datetime.today().strftime('%Y-%m-%d')
trade_day = pd.read_sql("select distinct cal_date FROM trade_cal WHERE cal_date BETWEEN '{}' AND '{}' AND is_open = 1 AND cal_date not in (SELECT DISTINCT trade_date from stock_daily)".format(start_date, today), engine)

while not trade_day.empty:
    for day in trade_day['cal_date']:
        try:
            df = pro.daily(trade_date = day.strftime('%Y%m%d'))
        except Exception as e:
            print(e)
            sleep(60)
            continue
        df.to_sql('stock_daily', engine, index=False, if_exists='append')
        print(day, ' finished')
        sleep(1)
    trade_day = pd.read_sql("select distinct cal_date FROM trade_cal WHERE cal_date BETWEEN '{}' AND '{}' AND is_open = 1 AND cal_date not in (SELECT DISTINCT trade_date from stock_daily)".format(start_date, today), engine)
