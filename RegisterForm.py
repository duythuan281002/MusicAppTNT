import socket
import tkinter as tk
from tkinter import messagebox

class RegisterForm:
    def __init__(self, root, parent_window):
        self.root = root
        self.parent_window = parent_window
        self.root.title("Đăng kí")

        # Kích thước cửa sổ đăng kí
        self.window_width = 250
        self.window_height = 150

        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Tính toán vị trí của cửa sổ đăng kí
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

        # Tạo các thành phần trong form đăng kí
        self.label_username = tk.Label(self.root, text="Tài khoản:")
        self.entry_username = tk.Entry(self.root)

        self.label_password = tk.Label(self.root, text="Mật khẩu:")
        self.entry_password = tk.Entry(self.root, show="*")

        self.label_password1 = tk.Label(self.root, text="Xác nhận:")
        self.entry_password1 = tk.Entry(self.root, show="*")

        self.button_register = tk.Button(self.root, text="Đăng kí", command=self.register)

        # Định vị các thành phần trong form đăng kí
        self.label_username.place(x=20, y=20)
        self.entry_username.place(x=100, y=20)
        self.label_password.place(x=20, y=50)
        self.entry_password.place(x=100, y=50)
        self.label_password1.place(x=20, y=80)
        self.entry_password1.place(x=100, y=80)
        self.button_register.place(x=100, y=110)

    def register(self):
        # Lấy dữ liệu từ các ô nhập liệu
        username = self.entry_username.get()
        password = self.entry_password.get()
        password_confirmation = self.entry_password1.get()
        # Kiểm tra xem các ô nhập liệu có trống không
        if not username or not password or not password_confirmation:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        elif password != password_confirmation:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
        else:
            host = '192.168.138.48'
            port = 1236
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                    client.connect((host, port))
                    # Gửi thông tin đăng nhập
                    data = username + '_' + password
                    request = f'GET_USER_DATA_{data}'
                    client.sendall(request.encode())
                    print(f"Gửi dữ liệu đến sever : {data}")
                    # Nhận kết quả từ server
                    response1 = client.recv(1024).decode('utf-8')
                    if response1 == 'add_user_thanh_cong':
                        # Xử lý khi đăng nhập thất bại
                        messagebox.showinfo("Thêm", "Đăng ký tài khoản thành công")
                        self.root.destroy()  # Đóng cửa sổ hiện tại
                        self.parent_window.deiconify()  # Mở cửa sổ gốc
                    else:
                        messagebox.showerror("Thêm", "Tài khoản đã tồn tại")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi khi kết nối đến máy chủ: {e}")
                print(e)
            finally:
                client.close()


