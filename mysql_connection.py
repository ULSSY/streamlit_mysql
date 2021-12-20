import mysql.connector


def get_connection():
    connection= mysql.connector.connect(
        host='yh-db.cahgiqgzpaou.ap-northeast-2.rds.amazonaws.com',
        database='streamlit_db',
        user='python_user',
        password='1234'
    )
    return connection

    