import tushare as ts
from sqlalchemy import create_engine
from config import mysql_engine as engine

pro = ts.pro_api()

data = pro.stock_basic()

# 这个方法将sql语句中的insert改为replace
def mysql_replace_into(table, conn, keys, data_iter):
    from sqlalchemy.dialects.mysql import insert
    from sqlalchemy.ext.compiler import compiles
    from sqlalchemy.sql.expression import Insert
    @compiles(Insert)
    def replace_string(insert, compiler, **kw):
        s = compiler.visit_insert(insert, **kw)
        s = s.replace("INSERT INTO", "REPLACE INTO")
        return s
    data = [dict(zip(keys, row)) for row in data_iter]
    conn.execute(table.table.insert(replace_string=""), data)
# 每次覆盖更新
data.to_sql('stock_basic', engine, if_exists ='append', index=False, method=mysql_replace_into)