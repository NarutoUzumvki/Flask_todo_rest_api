from connection import connection

cursor = connection.cursor()

def insert(data):
    query = """
    insert into `Todo`(`TITLE`, `DESCRIPTION`)
    VALUES(%s, %s)
    """
    cursor.execute(query, data)
    

def retrieve(sno):
    query="""
    select*from `Todo` where `S.NO`=%s
    """
    cursor.execute(query, sno)
    data = cursor.fetchone()
    if data:
        column_names = [column[0] for column in cursor.description]
        data = dict(zip(column_names, data))
    return data


def update_title(data):
    query = """
    UPDATE Todo SET `TITLE`=%s where `S.NO`=%s
    """
    cursor.execute(query, data)


def update_desc(data):
    query = """
    UPDATE Todo SET `DESCRIPTION`=%s where `S.NO`=%s
    """
    cursor.execute(query, data)


def update(data):
    query = """
    UPDATE Todo SET `TITLE`=%s, `DESCRIPTION`=%s where `S.NO`=%s
    """
    cursor.execute(query, data)


def remove(sno):
    query="""
    delete from Todo where `S.NO`=%s
    """
    cursor.execute(query, sno)
