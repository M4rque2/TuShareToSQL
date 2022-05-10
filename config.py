from sqlalchemy import create_engine

# MySQL on local machine
# 将下面的数据库地址换成自己的地址，理论上支持sqlalchemy的各种方言，实际上仅在MySQL测试过，其他SQL数据库因为数据类型的支持差异，一定会有小毛病，需要自己解决。
mysql_engine = create_engine('mysql+pymysql://username:password@localhost:3306/tushare?charset=utf8mb4')