import pymysql

db_config = {
    "host":"localhost",
    "user":"root",
    "database":"todo_data",
    "password":"SQLP@ssw0rd",
    "autocommit":"True"
}

connection = pymysql.connect(**db_config)