import mysql.connector

from src.DAO.database import Database


class UserDAO:
    def __init__(self):
        self.database = Database()

    def get_user_by_id(self, user_id):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM user WHERE id = %s"
                cursor.execute(query, (user_id,))
                user = cursor.fetchone()
                cursor.close()
                return user
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
                return None
            finally:
                connection.close()
        else:
            return None

    def create_user(self, username, password):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO user (username, password) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                connection.commit()
                cursor.close()
                return True
            except mysql.connector.Error as e:
                print("Lỗi khi tạo người dùng trong MySQL:", e)
                return False
            finally:
                connection.close()
        else:
            return False

    def get_all_users(self):
        connection = self.database.connect_mysql()
        users = []
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM user"
                cursor.execute(query)
                users = cursor.fetchall()
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
            finally:
                connection.close()
        return users

    def get_id(self, username, password):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id FROM user WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                cursor.close()
                if user:
                    return user['id']  # Trả về ID của người dùng nếu tìm thấy
                else:
                    return None  # Trả về None nếu không tìm thấy người dùng
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
                return None
            finally:
                connection.close()
        else:
            return None

    def get_username(self, username):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id FROM user WHERE username = %s"
                cursor.execute(query, (username,))
                user = cursor.fetchone()
                cursor.close()
                if user:
                    return user['id']  # Return the user ID if found
                else:
                    return None  # Return None if the user is not found
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
                return None
            finally:
                connection.close()
        else:
            return None

# def main():
#     # Khởi tạo một đối tượng UserDAO
#     user_dao = UserDAO()
#
#     result = user_dao.get_id("sgu1","2")
#     print(result)
#
# if __name__ == "__main__":
#     main()