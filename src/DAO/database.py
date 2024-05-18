import mysql.connector

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'appmusic'

    def connect_mysql(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                return connection
            else:
                return None
        except mysql.connector.Error as e:
            print("Lỗi khi kết nối đến MySQL:", e)
            return None


