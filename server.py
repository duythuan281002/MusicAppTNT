import json
import socket
import threading
import pickle
from src.BUS.userBUS import UserBUS
from src.BUS.baihatBUS import BaiHatBUS
from src.BUS.baihatyeuthichBUS import BaiHatYeuThichBUS
# Khởi tạo server
HOST = '192.168.138.48'
PORT = 1236

# Khởi tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(6)

print(f"Server đang lắng nghe trên {HOST}:{PORT}...")
user_bus = UserBUS()
haihat_BUS = BaiHatBUS()
baihatyeuthich_bus = BaiHatYeuThichBUS()
global id_user
def handle_client_connection(client_socket, address):
    global id_user
    print(f"Đã kết nối với client {address}")
    try:
        while True:
            # Nhận thông tin đăng nhập từ client
            request = client_socket.recv(1024).decode('utf-8')
            if not request:
                print(f"Kết thúc kết nối với client {address}.")
                client_socket.close()
                return

            if request == 'GET_MUSIC_LIST':
                    danh_sach_bai_hat = haihat_BUS.load_data_bai_hat()
                    if danh_sach_bai_hat:
                        data_to_send = [bai_hat.__dict__ for bai_hat in danh_sach_bai_hat]
                        # Mã hóa dữ liệu và gửi về cho máy khách
                        serialized_data = pickle.dumps(data_to_send)
                        client_socket.sendall(serialized_data)
                    else:
                        # Gửi thông báo nếu không có dữ liệu từ cơ sở dữ liệu
                        client_socket.sendall(b'NO_DATA')
            elif request.startswith("GET_MUSIC_DATA"):
                try:
                    parts = request.split("_")
                    username = parts[3]
                    password = parts[4]

                    # Giả sử ta có một hàm kiểm tra đăng nhập
                    user_id = user_bus.get_id(username, password)
                    id_user = user_id
                    if user_id:
                        id_user = user_id
                        # Gửi ID của người dùng qua client
                        client_socket.sendall(str(user_id).encode())
                    else:
                        # Gửi thông báo nếu thông tin đăng nhập không hợp lệ
                        client_socket.sendall(b'fail')
                except json.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e}")
                    client_socket.sendall(b'INVALID_JSON')

            elif request == 'GET_MUSIC_LIST_YEU_THICH':
                    # Lọc danh sách bài hát yêu thích
                    filtered_bai_hat = []
                    danh_sach_bai_hat = haihat_BUS.load_data_bai_hat()
                    if danh_sach_bai_hat:
                        arr_list = [bai_hat.__dict__ for bai_hat in danh_sach_bai_hat]
                        danh_sach_bai_hat_yeu_thich = baihatyeuthich_bus.get_all_baihat_yeuthich_byID_user(id_user)
                        if danh_sach_bai_hat_yeu_thich:
                            for bai_hat in arr_list:
                                for item in danh_sach_bai_hat_yeu_thich:
                                    id_bai_hat = item['id_baihat']
                                    if bai_hat['id'] == id_bai_hat:
                                        filtered_bai_hat.append(bai_hat)
                    # Mã hóa dữ liệu bằng pickle
                    serialized_data = pickle.dumps(filtered_bai_hat)
                    # Gửi dữ liệu đã mã hóa qua socket
                    client_socket.sendall(serialized_data)
            elif request.startswith("GET_MUSIC_ID"):
                parts = request.split("_")
                song_id = int(parts[3])
                music_file_path = haihat_BUS.get_linkBH(song_id)
                if music_file_path:
                    print("in music")
                    try:
                        with open(music_file_path, 'rb') as f:
                            while True:
                                data = f.read(1024)
                                if not data:
                                    break
                                # print(data)
                                client_socket.sendall(data)
                            client_socket.sendall(b'')
                    except Exception as e:
                        print(f"Error sending music data: {e}")
                    finally:
                        break
                else:
                    client_socket.sendall(b'Song not found')
            elif request.startswith("ADD_MUSIC_ID"):
                parts = request.split("_")
                song_id = int(parts[3])
                if baihatyeuthich_bus.exists_baihatyeuthich(id_user,song_id):
                    client_socket.sendall(b'add_thatbai')
                else:
                    ktra = baihatyeuthich_bus.add_baihat_yeuthich(id_user, song_id)
                    if ktra:
                        client_socket.sendall(b'add_thanhcong')
            elif request.startswith("DEL_MUSIC_ID"):
                parts = request.split("_")
                song_id = int(parts[3])
                ktra = baihatyeuthich_bus.delete_baihat_yeuthich(song_id, id_user)
                if ktra != 0:
                    client_socket.sendall(b'del_thanhcong')
            elif request.startswith("GET_USER_DATA"):
                parts = request.split("_")
                username = parts[3]
                password = parts[4]
                if user_bus.get_username(username):
                    client_socket.sendall(b'add_user_that_bai')
                else:
                    ktra = user_bus.create_user(username, password)
                    if ktra:
                        client_socket.sendall(b'add_user_thanh_cong')
    except Exception as e:
        print(f"Error handling client request: {e}")
    finally:
        print(f"Kết thúc kết nối với client {address}.")
        client_socket.close()


while True:
    client_socket, address = server_socket.accept()
    threading.Thread(target=handle_client_connection, args=(client_socket, address)).start()
