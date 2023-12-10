import pymysql



conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = 'password', 
        
        )



cur = conn.cursor() 
cur.execute("CREATE database elderco")
output = cur.fetchall() 
print(output) 



print("All Done")