#!user/bin/python3

import records

def generate_db_connect_uri(username, password, db_addr):
    return "mysql://" + username + ":" + password + "@" + db_addr + "?charset=utf8"

def conn_to_mysql(username, password, db_addr):
    conn_uri = generate_db_connect_uri(username, password, db_addr)
    db = records.Database(conn_uri, encoding='utf-8')
    return db


def query(db, query_string):
    return db.query(query_string)


def test():
    username = "root"
    password = "texterrcollector"
    db_addr = "127.0.0.1:3306/cd_house_price"
    db = conn_to_mysql(username, password, db_addr)
    c = query(db, "select xiaoqu from tb_cd_house_price;")
    print(c)
test()

#docker run -d --name db_postgres -p 5432:5432 -e POSTGRES_USER=cdhouse -e POSTGRES_PASSWORD=cdhouseprice -e POSTGRES_DB=cd_house_price postgres  