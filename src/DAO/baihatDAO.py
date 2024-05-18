import os

import mysql.connector
from src.DTO.baihatDTO import BaiHatDTO
from src.DAO.database import Database
class BaiHatDAO:
    def __init__(self):
        self.database = Database()

    def load_data_bai_hat(self):
        connection = self.database.connect_mysql()
        danh_sach_bai_hat = []
        if connection:
            try:
                cursor = connection.cursor()
                # Thực hiện truy vấn SQL để lấy dữ liệu từ bảng 'baihat'
                cursor.execute("SELECT * FROM baihat")
                # Lấy tất cả các dòng kết quả
                rows = cursor.fetchall()
                # Lặp qua từng dòng kết quả và tạo đối tượng BaiHat tương ứng
                for row in rows:
                    id_bh, ten_bh, hinh_anh, link_nhac, loai_nhac = row
                    # Tạo đối tượng BaiHat và thêm vào danh sách
                    bai_hat = BaiHatDTO(id_bh, ten_bh, hinh_anh, link_nhac, loai_nhac)
                    danh_sach_bai_hat.append(bai_hat)
            except mysql.connector.Error as e:
                print("Lỗi khi lấy dữ liệu từ bảng baihat:", e)
            finally:
                connection.close()
        return danh_sach_bai_hat

    def get_linkBH(self, id):
        connection = self.database.connect_mysql()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM baihat WHERE id = %s"
                cursor.execute(query, (id,))
                latest_song = cursor.fetchone()
                if latest_song:
                    id, ten, hinh_anh, the_loai, link = latest_song
                    bai_hat_moi_nhat = BaiHatDTO(id, ten, hinh_anh, the_loai, link)

                    # Xác định thư mục chứa tệp âm nhạc trong dự án của bạn
                    music_directory = os.path.join(r"D:\App_Music_python\src\sound")
                    # Tạo đường dẫn tuyệt đối đến tệp âm nhạc
                    music_file_path = os.path.join(music_directory, bai_hat_moi_nhat.get_link())
                    if os.path.exists(music_file_path):
                        return music_file_path
                else:
                    print(f"Không tìm thấy bài hát với id {id} trong cơ sở dữ liệu.")
                    return None
            except Exception as e:
                print("Lỗi khi truy vấn cơ sở dữ liệu:", e)
                return None
            finally:
                connection.close()

    def add(self, tenBH, loaiBH, hinhAnh, link):
        connection = self.database.connect_mysql()
        if not connection:
            print("Không có kết nối đến cơ sở dữ liệu.")
            return False
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO baihat (tenBH, loaiNhac, hinhAnh, linkBH) VALUES (%s, %s, %s, %s)"
            val = (tenBH, loaiBH, hinhAnh, link)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print("Lỗi khi thêm bài hát:", e)
            return False

    def update(self, id_bai_hat, tenBH, loaiBH, hinhAnh, link):
        connection = self.database.connect_mysql()
        if not connection:
            print("Không có kết nối đến cơ sở dữ liệu.")
            return False
        try:
            cursor = connection.cursor()

            sql = "UPDATE baihat SET tenBH = %s, loaiNhac = %s, hinhAnh = %s, linkBH = %s WHERE id = %s"
            val = (tenBH, loaiBH, hinhAnh, link, id_bai_hat)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print("Lỗi khi cập nhật bài hát:", e)
            return False

    def delete(self, id_bai_hat):
        connection = self.database.connect_mysql()
        if not connection:
            print("Không có kết nối đến cơ sở dữ liệu.")
            return False
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM baihat WHERE id = %s"
            val = (id_bai_hat,)
            cursor.execute(sql, val)
            connection.commit()  # Lưu các thay đổi vào cơ sở dữ liệu
            cursor.close()
            return True
        except mysql.connector.Error as e:
            print("Lỗi khi xoá bài hát:", e)
            return False
        finally:
            connection.close()

    def get_latest_song(self, id):
        connection = self.database.connect_mysql()
        if not connection:
            print("Không có kết nối đến cơ sở dữ liệu.")
            return None
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM baihat WHERE id = %s"
            cursor.execute(query, (id,))
            latest_song = cursor.fetchone()
            if latest_song:
                id, ten, hinh_anh, the_loai, link = latest_song
                bai_hat_moi_nhat = BaiHatDTO(id, ten, hinh_anh, the_loai, link)
                return bai_hat_moi_nhat
            else:
                print(f"Không tìm thấy bài hát với id {id} trong cơ sở dữ liệu.")
                return None
        except Exception as e:
            print("Lỗi khi truy vấn cơ sở dữ liệu:", e)
            return None
        finally:
            connection.close()

    def get_Maxid(self):
        connection = self.database.connect_mysql()
        if not connection:
            print("Không có kết nối đến cơ sở dữ liệu.")
            return None
        try:
            cursor = connection.cursor()
            query = "SELECT MAX(id) FROM baihat"
            cursor.execute(query)
            result = cursor.fetchone()
            if result and result[0] is not None:
                latest_id = result[0]
                return latest_id
        except Exception as e:
            print("Lỗi khi truy vấn cơ sở dữ liệu:", e)
            return None

    def getByTheLoai(self, chuoi):
        connection = self.database.connect_mysql()
        if not connection:
            print("Không có kết nối đến cơ sở dữ liệu.")
            return []

        try:
            cursor = connection.cursor()
            # Sử dụng placeholder %s để truyền tham số chuỗi vào câu truy vấn
            query = "SELECT * FROM baihat WHERE loaiNhac = %s"
            cursor.execute(query, (chuoi,))
            rows = cursor.fetchall()  # Lấy tất cả các bản ghi từ kết quả truy vấn

            danh_sach_bai_hat = []
            # Lặp qua từng dòng kết quả và tạo đối tượng BaiHat tương ứng
            for row in rows:
                id_bh, ten_bh, hinh_anh, link_nhac, loai_nhac = row
                # Tạo đối tượng BaiHat và thêm vào danh sách
                bai_hat = BaiHatDTO(id_bh, ten_bh, hinh_anh, link_nhac, loai_nhac)
                danh_sach_bai_hat.append(bai_hat)

            cursor.close()
            return danh_sach_bai_hat

        except Exception as e:
            print("Lỗi khi truy vấn cơ sở dữ liệu:", e)
            return []
# def main():
#     # Khởi tạo một đối tượng UserDAO
#     user_dao = BaiHatDAO()
#
#     result = user_dao.load_data_bai_hat()
#     print(result)
#
# if __name__ == "__main__":
#     main()