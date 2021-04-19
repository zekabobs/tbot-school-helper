import sqlite3


class Sqlliter():
    def __init__(self, db_file='school_db.db'):
        self.tables = ('user', 'scholar', 'teacher', 'parent', 'descriptions')
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        statement = "SELECT name FROM sqlite_master WHERE type='table';"
        if not self.tables in self.cursor.execute(statement).fetchall():
            self.create_table(self.cursor, self.tables)

        self.conn.commit()


    def is_exists(self, id):
        return self.cursor.execute(f'select * from user where id={id}').fetchall()


    def get_user_info(self, id):
        return self.cursor.execute(f'select * from user where id={id}').fetchall()


    def get_scholar(self, id):
        return self.cursor.execute(f"select class_ from scholar where id={id}").fetchall()


    def get_category(self, id):
        result = self.is_exists(id)
        if not result:
            return None

        return result[-1][-2]


    def get_scholars(self):
        return self.cursor.execute("select id, fio, username from user where category='scholar'").fetchall()


    def update_user_fio(self, id, fio):
        if self.is_exists(id):
            self.cursor.execute(f"update user set fio='{fio}' where id={id}")
            self.conn.commit()
            return True

        return False


    def insert_data(self, table_name, username, *args):
        if not self.is_exists(id=args[0]):
            self.insert_into_user(args[0], username, table_name, 'Anonim')
            self.cursor.execute(f'insert into {table_name} values {args}')
            self.conn.commit()
            return True

        return False


    def insert_into_user(self, *args):
        self.cursor.execute(f'insert into user values {args}')


    def delete_data(self, id):
        table_name =  self.is_exists(id)
        if table_name:
            self.cursor.execute(f'delete from user where id={id}')
            self.cursor.execute(f'delete from {table_name[-1][-2]} where id={id}')
            self.conn.commit()
            return True

        return False


    def show_table(self, table_name):
        self.cursor.execute(f'select * from {table_name};')
        result = self.cursor.fetchall()

        for row in result:
            print(row)


    def create_table(self, cur, *args):
        cur.execute("""
            Create table if not exists user(
            id int primary key,
            username text,
            category text not null,
            fio text(6,60));
        """)

        cur.execute("""
            Create table if not exists scholar(
            id int primary key,
            id_parent int,
            class_ int not null);
        """)

        cur.execute("""
            Create table if not exists teacher(
            id int primary key,
            subject text(30));
        """)

        cur.execute("""
            Create table if not exists parent(
            id int primary key,
            id_scholar int,
            foreign key (id_scholar) references scholar(id));
        """)

        cur.execute("""
            Create table if not exists subscriptions(
            id int primary key,
            id_user int ,
            status boolean not null,
            foreign key (id_user) references user(id));
        """)