import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="0",
                              host="localhost",
                              port="5432",
                              database="bank")

cursor = connection.cursor()

class Bank:
    __smen_id = 0
    __status_smen = False

    # Smena ochish
    @classmethod
    def start_smen(cls):
        if not cls.__status_smen:
            cls.__smen_id += 1
            cls.__status_smen = True
            return cls.__smen_id
        else:
            return "Ochiq smen mavjud"
        
    # Smena tugatish 
    @classmethod
    def end_smen(cls):
        if cls.__status_smen:
            cls.__smen_id -= 1
            cls.__status_smen = False
            cursor.execute(f"DELETE FROM users;")
            connection.commit
            return "Complate !"
        else:
            return "Yopib bo`lmaydi. Hali smen boshlanmagan"
        
    # Foydalanuvcchilarga navbat berish
    @classmethod
    def queue(cls):
        if cls.__status_smen:
            cursor.execute(f"INSERT INTO users (status, smen) VALUES (true, {cls.__smen_id});")
            connection.commit
        else:
            return "Smen hali boshlanmagan"
    
    # Hozirda xizmat ko`rsatilayotgan foydalanuvchi
    @classmethod
    def the_person_being_served(cls):
        if cls.__status_smen:
            cursor.execute("SELECT id FROM users WHERE status = true;")
            record = cursor.fetchall()
            return record[0][0]
        else:
            return "Smen hali boshlanmagan"
        
    # Foydalanuvchiga xizmat korsatish   
    @classmethod
    def service(cls):
        if cls.__status_smen:
            cursor.execute("SELECT id FROM users WHERE status = true;")
            record = cursor.fetchall()
            if len(record) > 0:
                cursor.execute(f"UPDATE users SET status = false WHERE id = {record[0][0]};")
                connection.commit
                return "Complate !"
            else:
                return "Hali foydalanuvchi yo`q"                
        else:
            return "Smen hali boshlanmagan"

    # Baholash
    @classmethod
    def evaluation(cls, rating=None, comment=None):
        if cls.__status_smen:
            cursor.execute("SELECT * FROM users;")
            record = cursor.fetchall()
            if len(record) > 0:
                cursor.execute(f"INSERT INTO evaluation (rating, comment) VALUES ('{rating}', '{comment}');")
                connection.commit
                return "Complate !"
            else:
                return "Hali foydalanuvchi yo`q"                
        else:
            return "Smen hali boshlanmagan"    

    # Barcha commentarialarni ko`rish 
    @classmethod
    def show_comments(cls):
        if cls.__status_smen:
            cursor.execute("SELECT comment FROM evaluation;")
            record = cursor.fetchall()
            if len(record) > 0:
                cursor.execute("SELECT comment FROM evaluation WHERE comment != 'None';")
                record = cursor.fetchall()
                return record
            else:
                return "Hali commentlar yo`q"                
        else:
            return "Smen hali boshlanmagan"   
        
    # O`rtacha reytingni ko`rish 
    @classmethod
    def show_rating(cls):
        if cls.__status_smen:
            cursor.execute("SELECT rating FROM evaluation;")
            record = cursor.fetchall()
            if len(record) > 0:
                cursor.execute("SELECT commratingent FROM evaluation WHERE rating != 'None';")
                record = len(cursor.fetchall())
                cursor.execute("SELECT SUM(rating) FROM evaluation;")
                record1 = cursor.fetchone()
                return record1 / record
            else:
                return "Hali commentlar yo`q"                
        else:
            return "Smen hali boshlanmagan"

