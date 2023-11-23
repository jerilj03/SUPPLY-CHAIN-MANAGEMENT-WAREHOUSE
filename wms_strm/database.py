import mysql.connector 
mydb = mysql.connector.connect(host="localhost", user="root", password="1915",database="warehouse_management")
cur = mydb.cursor()

def validate(username,password,privilege):
    cur.execute(f"SELECT * FROM users;")
    sel=[cur.column_names,cur.fetchall()]
    if (username,password,privilege) in sel[1]:
        return True
    return False

def signup(username,password,privilege):
    query = "INSERT INTO users (username, password, privilege) VALUES (%s, %s, %s)"
    values = (username, password,privilege)
    cur.execute(query, values)
    mydb.commit()

def tables():
    cur.execute('SHOW TABLES')
    data = cur.fetchall()
    return [i[0] for i in data if i[0]!='users']
def view_all(table_name): 
    cur.execute(f"SELECT * FROM {table_name}") 
    data = cur.fetchall()
    return data

def view_id(table_name):
    cur.execute(f"SELECT * FROM {table_name}")
    data = cur.fetchall()
    return [i[0] for i in data]

def columns(table_name):
    cur.execute(f"SHOW COLUMNS FROM {table_name}")
    data = cur.fetchall()
    return [i[0] for i in data]

def add_data(table_name, data): 
    col_names = ",".join(data.keys())
    vals = ",".join(data.values())
    cur.execute(f"INSERT INTO {table_name} ({col_names}) VALUES ({vals})")
    mydb.commit()

def add_request(data):
    col_names = ",".join(data.keys())
    vals = ",".join(data.values())
    cur.execute(f"INSERT INTO shipments ({col_names}) VALUES ({vals})")
    mydb.commit()
    
    
def update_items(id,quant):
    sel=view_all("items")
    for i in sel:
        if i[1]==id:
           quant=int(quant)+int(i[2])
           query=f"UPDATE items SET Quantity={quant} WHERE 'Item_Id'='{id};'"
           print(query)
           cur.execute(f"UPDATE items SET Quantity={quant} WHERE Item_Id={int(id)}")
           mydb.commit()

def check_thresh():
    sel=view_all("items")
    list1=[]
    for i in sel:
        if int(i[2])<=int(i[5]):
            list1.append([i[0],i[1],i[5]])
    return list1

def check_qty(vals):
    sel=view_all("items")
    # vals = ",".join(data.values())
    # vals = data.values()
    print(vals)
    print(sel)
    
    for i in sel: 
        if  int(vals[0]) == i[1]:
            # if vals[1]<i[2]:
            return int(i[2])

    # return False

def deduct(id, quant):
    sel=view_all("items")
    for i in sel:
        if i[1]==id:
           quant = int(i[2]) - int(quant)
        #    query=f"UPDATE items SET Quantity={quant} WHERE 'Item_Id'='{id};'"
        #    print(query)
           cur.execute(f"UPDATE items SET Quantity={quant} WHERE Item_Id={int(id)}")
           mydb.commit()

# def receipt():
#     data1
