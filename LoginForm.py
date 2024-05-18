import socket
import tkinter as tk
from tkinter import messagebox

from Music import MusicTab
from RegisterForm import RegisterForm


class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")

        # Kích thước cửa sổ đăng nhập
        self.window_width = 250
        self.window_height = 120

        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Tính toán vị trí của cửa sổ đăng nhập
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

        # Tạo các thành phần trong form đăng nhập
        self.label_username = tk.Label(self.root, text="Tài khoản:")
        self.label_password = tk.Label(self.root, text="Mật khẩu:")
        self.entry_username = tk.Entry(self.root)
        self.entry_password = tk.Entry(self.root, show="*")
        self.button_login = tk.Button(self.root, text="Đăng nhập", command=self.login)
        self.button_register = tk.Button(self.root, text="Đăng kí", command=self.register)

        # Định vị các thành phần trong form đăng nhập
        self.label_username.place(x=20, y=20)
        self.entry_username.place(x=100, y=20)
        self.label_password.place(x=20, y=50)
        self.entry_password.place(x=100, y=50)
        self.button_login.place(x=140, y=80)
        self.button_register.place(x=70, y=80)

    def login(self):
        # Lấy thông tin đăng nhập từ người dùng
        username = self.entry_username.get()
        password = self.entry_password.get()
        host  = '192.168.138.48'
        port = 1236
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((host, port))
                # Gửi thông tin đăng nhập
                data = username+ '_' + password
                request = f'GET_MUSIC_DATA_{data}'
                client.sendall(request.encode())
                print(f"Gửi dữ liệu đến sever : {data}")
                # Nhận kết quả từ server
                response1 = client.recv(1024).decode('utf-8')
                if response1 == 'fail':
                    # Xử lý khi đăng nhập thất bại
                    messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng!")
                else:
                    self.root.iconify()  # Ẩn cửa sổ hiện tại
                    self.music_window = tk.Toplevel(self.root)  # self.parent là cửa sổ chính của ứng dụng
                    self.music_window.title("App nghe nhạc TNT")
                    window_width = 750
                    window_height = 450
                    self.music_window.geometry(f"{window_width}x{window_height}")
                    music_tab = MusicTab(self.music_window, self.root)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi kết nối đến máy chủ: {e}")
            print(e)
        finally:
            client.close()

    def register(self):
        self.root.iconify()  # Ẩn cửa sổ hiện tại
        register_window = tk.Toplevel(self.root)  # Tạo cửa sổ mới
        register_form = RegisterForm(register_window, self.root)
def main():
    root = tk.Tk()
    login_form = LoginForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
