import sqlite3



def insert_query(name ,weight, rank):
     conn = sqlite3.connect("Pokedata_hisotry.db")
     cursor=conn.cursor()


     cursor.execute('create table if not exists poke_history('
               'name varchar(100),'
               'weight float,'
               'rank int);')

     cursor.execute("insert into poke_history(name,weight,rank)"
                   "values(?,?,?)",(name,weight,rank))
     conn.commit()  # to save the changes
     conn.close()
def select_query():
    conn = sqlite3.connect("Pokedata_hisotry.db")
    cursor = conn.cursor()

    cursor.execute("select * from poke_history")
    data=cursor.fetchall()
    print("printing all the searched pokemon data below data :")
    print(f"--------------------------------------------------")
    i=0 # for index showing in the table below
    for d in data:
        i=i+1
        print(f"{i}--- name:{d[0]}--- weight:{d[1]}--- rank:{d[2]}---")
    print(f"--------------------------------------------------")
    print(f"Total : {i} rows.")
    conn.commit()  # to save the changes
    conn.close()

if __name__=="__main__":
    select_query()