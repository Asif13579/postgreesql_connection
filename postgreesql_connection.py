import psycopg2
import psycopg2.extras
conn=None
try:
    with psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Welcome@1") as conn:
        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('drop table if exists employee1')

            create_script="""create table if not exists employee1(id int primary key,name varchar(40) not null,salary int,dept_id varchar(30))"""
            cur.execute(create_script)

            insert_script='insert into employee1 (id,name,salary,dept_id) values (%s,%s,%s,%s)'
            insert_values=[(1,'James',12000,'D1'),(2,'Robin',15000,'D1'),(3,'Xavier',20000,'D1')]
            for record in insert_values:
                cur.execute(insert_script,record)

            update_script='update employee1 set salary=salary+(salary *0.5)'
            cur.execute(update_script)

            delete_script='delete from employee1 where name=%s'
            delete_record=('James',)
            cur.execute(delete_script,delete_record)

            cur.execute('select * from employee1')
            for record in cur.fetchall():
                #print(record[1],record[2])
                print(record['name'],record['salary'])





            #cur.execute(create_script)
            conn.commit()


except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
