import streamlit as st
from mysql_connection import get_connection
from mysql.connector.errors import Error

def run_select_app():
    st.subheader('데이터 조회')
    try : 
        connection=get_connection()
       
        query='''select id,email,age,address
                 from test_user;'''
    
    #셀렉트 결과를 딕셔너리로 가져오느 경우
        cursor=connection.cursor()
        
        cursor.execute(query)

        #select문은 아래 내용이 필요하다
        record_list =cursor.fetchall()
        print(record_list)

        for row in record_list:
           st.write(row)

        #이메일 항목에서 검색하는 기능
        st.subheader('이메일 검색')
        search_word=st.text_input('검색어 입력')

        if st.button('검색하기!'):
            query='''select id,email,age.address 
                    from test_user
                    where email like '%%s%' '''

            record=(search_word,)
            cursor.execute(query,record)



         #2.아이디를 입력하면 해당 아이디의 데이터만 조회
        st.subheader('아이디로 조회')
        st.number_input('아이디를 입력하세요',min_value=1)

        query='''select id,email,age,address 
                from test_user 
                where email like '%'''+search_word+'''%';'''
        

        cursor.execute(query)

        
        # select문은 아래 내용이 필요하다
        record_list =cursor.fetchall()
        print(record_list)

        for row in record_list:
           st.write(row)
          

    #try와 except는 한쌍
    except Error as e:
        print('Error while connecting to MySQL',e)
    #finally는 try에서 에러가 나든 안나든 무조건 실행하라는 뜻
    finally:
        print('finally')
        cursor.close()
        if connection.is_connected():
            connection.close()
            print('MySQL connection is closed')
        else:
            print('connection does not exist')

