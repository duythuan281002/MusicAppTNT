import mysql.connector
from src.DAO.database import Database

class BaiHatYeuThichDAO:
    def __init__(self):
        self.database = Database()

    def add_baihat_yeuthich(self, id_user, id_yeuthich):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO baihatyeuthich (id_user, id_baihat) VALUES (%s, %s)"
                val = (id_user, id_yeuthich)
                cursor.execute(sql, val)
                connection.commit()
                cursor.close()
                return True
            except mysql.connector.Error as e:
                print("Lỗi khi thêm bài hát yêu thích:", e)
                return False
            finally:
                connection.close()
        else:
            return False

    def delete_baihat_yeuthich(self, id_baihat, id_user):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "DELETE FROM baihatyeuthich WHERE id_baihat = %s AND id_user = %s"
                val = (id_baihat, id_user)
                cursor.execute(sql, val)
                connection.commit()
                cursor.close()
                return True
            except mysql.connector.Error as e:
                print("Lỗi khi xoá bài hát yêu thích:", e)
                return False
            finally:
                connection.close()
        else:
            return False

    def get_all_baihat_yeuthich(self):
        connection = self.database.connect_mysql()
        baihatyeuthich_list = []
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM baihatyeuthich"
                cursor.execute(query)
                baihatyeuthich_list = cursor.fetchall()
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
            finally:
                cursor.close()
                connection.close()
        return baihatyeuthich_list

    def get_all_baihat_yeuthich_byID_user(self, id_user):
        connection = self.database.connect_mysql()
        baihatyeuthich_list = []
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id_baihat FROM baihatyeuthich WHERE id_user = %s"
                cursor.execute(query, (id_user,))
                baihatyeuthich_list = cursor.fetchall()
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
            finally:
                cursor.close()
                connection.close()
        return baihatyeuthich_list

    def exists_baihatyeuthich(self, id_user, id_baihat):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT COUNT(*) FROM baihatyeuthich WHERE id_user = %s AND id_baihat = %s"
                cursor.execute(query, (id_user, id_baihat))
                count = cursor.fetchone()[0]
                cursor.close()
                return count > 0  # Return True if the combination exists, otherwise False
            except mysql.connector.Error as e:
                print("Lỗi khi truy vấn dữ liệu từ MySQL:", e)
                return False
            finally:
                connection.close()
        else:
            return False

# def main():
#     # Khởi tạo một đối tượng BaiHatYeuThichDAO
#     baihat_yeuthich_dao = BaiHatYeuThichDAO()
#
#
#
#     # # Lấy tất cả các bản ghi từ bảng baihatyeuthich
#     baihatyeuthich_list = baihat_yeuthich_dao.get_all_baihat_yeuthich_byID_user(1)
#     print("Danh sách bài hát yêu thích:")
#     for baihatyeuthich in baihatyeuthich_list:
#         print(baihatyeuthich['id_baihat'])
#
# if __name__ == "__main__":
#     main()