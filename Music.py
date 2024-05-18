import io
import os
import pickle
import tempfile
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pygame
import socket
import random
from tkinter import PhotoImage

pygame.mixer.init()
global thoiGian
thoiGian = 0
class MusicTab:
    def __init__(self, parent, parent_window):
        self.root = parent
        self.parent_window = parent_window
        self.parent = parent
        self.frame = ttk.Frame(self.parent)
        self.id = None
        self.thoiLuongNhac = None
        self.is_playing = False
        self.isPlayStop = False
        self.isLap = False
        self.path = None
        self.xu_ly_baihat_path = None
        self.length_in_secs = None
        self.timer_id = None  # ID của bộ đếm thời gian hiện tại

        self.tab_control = ttk.Notebook(self.parent)
        # Tạo tab đầu tiên và khung chứa
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Nghe nhạc')

        self.labelframe1 = ttk.LabelFrame(self.tab1, text="Tất cả bài hát")
        self.labelframe1.place(x=310, y=10, width=420, height=400)

        # Combobox để chọn thể loại
        self.combobox_loaiBH = ttk.Combobox(self.labelframe1, values=["Tất cả", "Rap", "Trẻ", "Nhạc Xưa", "Nước Ngoài"],
                                            width=15)
        self.combobox_loaiBH.place(x=10, y=10)  # 559
        self.combobox_loaiBH.bind("<<ComboboxSelected>>", self.on_combobox_select)

        # Entry để nhập tên bài hát
        self.entry_find = tk.Entry(self.labelframe1, width=20)
        self.entry_find.place(x=210, y=10)

        # Button find
        self.button_find = tk.Button(self.labelframe1, text="Tìm", command=self.handleFind, width=8)
        self.button_find.place(x=340, y=6)

        # Bảng dữ liệu
        self.tree = ttk.Treeview(self.labelframe1, columns=("STT", "ID", "Tên bài hát", "Loại nhạc"), show="headings")
        self.tree.heading("STT", text="STT")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tên bài hát", text="Tên bài hát")
        self.tree.heading("Loại nhạc", text="Loại nhạc")

        # Định dạng cột cho Treeview
        self.tree.column("STT", width=50)
        self.tree.column("ID", width=50)
        self.tree.column("Tên bài hát", width=200)
        self.tree.column("Loại nhạc", width=100)

        # Scrollbar cho Treeview
        self.tree_scroll = ttk.Scrollbar(self.labelframe1, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        # Đặt vị trí của Treeview và Scrollbar
        self.tree.place(x=10, y=40, width=390, height=300)
        self.tree_scroll.place(x=400, y=40, height=300)

        # Button chọn
        self.button_chon = tk.Button(self.labelframe1, text="Chọn", command=self.chon_bai_hat, width=10)
        self.button_chon.place(x=320, y=350)

        # Button yêu thích
        self.button_ythich = tk.Button(self.labelframe1, text="Yêu thích", command=self.handleYeuThich, width=10)
        self.button_ythich.place(x=10, y=350)

        # Tạo tab thứ hai và khung chứa
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Yêu thích')

        self.labelframe2 = ttk.LabelFrame(self.tab2, text="Bài hát yêu thích")
        self.labelframe2.place(x=310, y=10, width=420, height=400)

        self.tab_control.pack(expand=1, fill='both')

        # Các thành phần trong labelframe2
        self.combobox_loaiBH2 = ttk.Combobox(self.labelframe2, values=["Tất cả", "Rap", "Trẻ", "Nhạc Xưa", "Nước Ngoài"],
                                            width=15)
        self.combobox_loaiBH2.place(x=10, y=10)  # 559
        self.combobox_loaiBH2.bind("<<ComboboxSelected>>", self.on_combobox_select2)

        # Entry để nhập tên bài hát
        self.entry_find2 = tk.Entry(self.labelframe2, width=20)
        self.entry_find2.place(x=210, y=10)

        # Button find
        self.button_find2 = tk.Button(self.labelframe2, text="Tìm", command=self.handleFind2, width=8)
        self.button_find2.place(x=340, y=6)

        # Bảng dữ liệu
        self.tree2 = ttk.Treeview(self.labelframe2, columns=("STT", "ID", "Tên bài hát", "Loại nhạc"), show="headings")
        self.tree2.heading("STT", text="STT")
        self.tree2.heading("ID", text="ID")
        self.tree2.heading("Tên bài hát", text="Tên bài hát")
        self.tree2.heading("Loại nhạc", text="Loại nhạc")

        # Định dạng cột cho Treeview
        self.tree2.column("STT", width=50)
        self.tree2.column("ID", width=50)
        self.tree2.column("Tên bài hát", width=200)
        self.tree2.column("Loại nhạc", width=100)

        # Scrollbar cho Treeview
        self.tree_scroll2 = ttk.Scrollbar(self.labelframe2, orient="vertical", command=self.tree2.yview)
        self.tree2.configure(yscrollcommand=self.tree_scroll2.set)

        # Đặt vị trí của Treeview và Scrollbar
        self.tree2.place(x=10, y=40, width=390, height=300)
        self.tree_scroll2.place(x=400, y=40, height=300)

        # Button chọn
        self.button_chon2 = tk.Button(self.labelframe2, text="Chọn",command=self.chon_bai_hat2, width=10)
        self.button_chon2.place(x=320, y=350)

        # Button yêu thích
        self.button_ythich2 = tk.Button(self.labelframe2, text="Bỏ thích",command=self.handleDelYeuThich, width=10)
        self.button_ythich2.place(x=10, y=350)


        self.image_path2 = "D:/App_Music_python/src/imgBtn/icons8-play-50.png"
        self.image_path3 = "D:/App_Music_python/src/imgBtn/icons8-pause-50.png"
        self.image_path4 = "D:/App_Music_python/src/imgBtn/prev.png"
        self.image_path5 = "D:/App_Music_python/src/imgBtn/next.png"
        self.image_path6 = "D:/App_Music_python/src/imgBtn/repeat.png"
        self.image_path7 = "D:/App_Music_python/src/imgBtn/repeat-no.png"
        self.image_path8 = "D:/App_Music_python/src/imgBtn/random.png"

        self.imgPrev = PhotoImage(file=self.image_path4)
        self.imgPlay = PhotoImage(file=self.image_path2)
        self.imgPau = PhotoImage(file=self.image_path3)
        self.imgNext = PhotoImage(file=self.image_path5)
        self.imgRepeat = PhotoImage(file=self.image_path6)
        self.imgRepeatNo = PhotoImage(file=self.image_path7)
        self.ingRandom = PhotoImage(file=self.image_path8)

        self.label_tenBH = tk.Label(parent, font=("Arial", 16))
        self.label_tenBH.place(x=10, y=25)

        self.label_theloai = tk.Label(parent, font=("Arial", 10))
        self.label_theloai.place(x=10, y=60)

        self.label_hinhAnh = tk.Label(parent)
        self.label_hinhAnh.place(x=10, y=100)

        self.button_lui = tk.Button(parent, image=self.imgPrev, command=self.lui_music, width=32, height=32)
        self.button_lui.place(x=60, y=360)

        self.button_play = tk.Button(parent, image=self.imgPlay, command=self.play_music, width=32, height=32)
        self.button_play.place(x=110, y=360)

        self.button_lap = tk.Button(parent, image=self.imgRepeat, command=self.xulyLap, width=32, height=32)
        self.button_lap.place(x=10, y=360)

        self.button_phatNN = tk.Button(parent, image=self.ingRandom, command=self.phatNgauNhien, width=32, height=32)
        self.button_phatNN.place(x=210, y=360)

        self.button_tien = tk.Button(parent, image=self.imgNext, command=self.next_music, width=32, height=32)
        self.button_tien.place(x=160, y=360)

        self.button_out = tk.Button(parent, text="Đăng xuất", command=self.logout)
        self.button_out.place(x=670, y=0)

        # Tạo thanh điều khiển âm thanh
        self.volume_scale = ttk.Scale(parent, from_=0, to=100, orient="vertical", length=100)
        self.volume_scale.set(0)
        self.volume_scale.place(x=260, y=245)
        self.volume_scale.bind("<ButtonRelease-1>", self.change_volume)

        self.canvas = tk.Canvas(self.parent, height=4, width=225, bg="gray", highlightthickness=0)
        self.canvas.place(x=10, y=340)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.canvas1 = tk.Canvas(self.parent, height=4, width=0, bg="red", highlightthickness=0)
        self.canvas1.place(x=10, y=340)
        self.canvas1.bind("<Button-1>", self.on_canvas1_click)

        # Gán sự kiện thay đổi tab
        self.tab_control.bind("&lt;&lt;NotebookTabChanged&gt;&gt;", self.on_tab_changed)
        self.danh_sach_bai_hat = []
        self.danh_sach_bai_hat_yeu_thich = []
        self.hien_thi_danh_sach_bai_hat()
        self.hien_thi_danh_sach_bai_hat_yeu_thich()
        self.id = self.danh_sach_bai_hat[-1]['id']
        self.setBaiHatMacDinh(self.id)

    def setBaiHatMacDinh(self, id):
        for bai_hat in self.danh_sach_bai_hat:
            if bai_hat['id'] == id:
                self.label_tenBH.config(text=bai_hat['tenBH'])
                self.label_theloai.config(text="Thể loại: " + bai_hat['loaiBH'])
                image_path = os.path.join(r"D:\App_Music_python\src\img", bai_hat['hinhAnh'])
                if os.path.exists(image_path):
                    # Load hình ảnh sử dụng PIL
                    image = Image.open(image_path)
                    image.thumbnail((220, 220))  # Thay đổi kích thước hình ảnh
                    photo = ImageTk.PhotoImage(image)
                    self.label_hinhAnh.config(image=photo)
                    self.label_hinhAnh.image = photo  # Giữ tham chiếu để hình ảnh không bị garbage collected
        try:
            if id is None:
                print("No song selected.")
                return

            host = '192.168.138.48'
            port = 1236
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                    client.connect((host, port))
                    # Gửi yêu cầu danh sách nhạc
                    request = f'GET_MUSIC_ID_{id}'
                    client.sendall(request.encode())
                    print(f"yêu cầu lấy dữ liệu của id : {id}")
                    # Nhận dữ liệu âm nhạc từ server và lưu vào một tệp tạm
                    music_file_data = tempfile.SpooledTemporaryFile(max_size=10000000)
                    while True:
                        data = client.recv(1024)
                        if not data:
                            break
                        music_file_data.write(data)
                    music_file_data.seek(0)
                    music_bytes = music_file_data.read()
                    self.xu_ly_baihat_path = music_bytes
                    pygame.mixer.music.load(io.BytesIO(music_bytes))
                    pygame.mixer.Sound(io.BytesIO(music_bytes))
            except ConnectionResetError as e:
                print("Kết nối đã bị đóng bởi máy chủ từ xa.")
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")
                client.close()
        except Exception as e:
            print(f"Error playing selected song: {e}")

    def hien_thi_danh_sach_bai_hat(self):
        host  = '192.168.138.48'
        port = 1236
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((host, port))

                # Gửi yêu cầu danh sách nhạc
                client.sendall(b'GET_MUSIC_LIST')
                serialized_data = client.recv(4096)
                # Giải mã dữ liệu nhận được từ dạng bytes sang danh sách
                data_received = pickle.loads(serialized_data)

                self.danh_sach_bai_hat = data_received
                for item in self.tree.get_children():
                    self.tree.delete(item)
                vtri = 1
                for bai_hat in self.danh_sach_bai_hat:
                    data = self.entry_find.get().strip()
                    if data.lower() in bai_hat['tenBH'].lower():
                        id_value = bai_hat['id']
                        tenBH_value = bai_hat['tenBH']
                        loaiBH_value = bai_hat['loaiBH']
                        self.tree.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                        vtri += 1
        except ConnectionResetError as e:
            print("Kết nối đã bị đóng bởi máy chủ từ xa.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
            client.close()


    def hien_thi_danh_sach_bai_hat_yeu_thich(self):
        host = '192.168.138.48'
        port = 1236
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((host, port))
                # Gửi yêu cầu danh sách nhạc
                client.sendall(b'GET_MUSIC_LIST_YEU_THICH')
                serialized_data = client.recv(4096)
                # Giải mã dữ liệu nhận được từ dạng bytes sang danh sách
                data_received = pickle.loads(serialized_data)
                self.danh_sach_bai_hat_yeu_thich = data_received
                for item in self.tree2.get_children():
                    self.tree2.delete(item)
                vtri = 1
                for bai_hat in self.danh_sach_bai_hat_yeu_thich:
                        data = self.entry_find.get().strip()
                        if data.lower() in bai_hat['tenBH'].lower():
                            id_value = bai_hat['id']
                            tenBH_value = bai_hat['tenBH']
                            loaiBH_value = bai_hat['loaiBH']
                            self.tree2.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                            vtri += 1
        except ConnectionResetError as e:
            print("Kết nối đã bị đóng bởi máy chủ từ xa.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
            client.close()

    def handleYeuThich(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)["values"]
            id_bai_hat = item_values[1]
            print(id_bai_hat)
            try:
                if id_bai_hat is None:
                    print("No song selected.")
                    return
                host = '192.168.138.48'
                port = 1236
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                        client.connect((host, port))
                        # Gửi yêu cầu danh sách nhạc
                        request = f'ADD_MUSIC_ID_{id_bai_hat}'
                        client.sendall(request.encode())
                        print(f"Gửi yêu cùa thêm id yêu thích : {id_bai_hat}")

                        # Nhận kết quả từ server
                        response1 = client.recv(1024).decode('utf-8')
                        if response1 == 'add_thanhcong':
                            messagebox.showinfo("Thêm", "Thêm bài hát yêu thích thành công")

                            # Gửi yêu cầu danh sách nhạc
                            client.sendall(b'GET_MUSIC_LIST_YEU_THICH')
                            serialized_data = client.recv(4096)
                            # Giải mã dữ liệu nhận được từ dạng bytes sang danh sách
                            data_received = pickle.loads(serialized_data)
                            self.danh_sach_bai_hat_yeu_thich = data_received
                            for item in self.tree2.get_children():
                                self.tree2.delete(item)
                            vtri = 1
                            for bai_hat in self.danh_sach_bai_hat_yeu_thich:
                                data = self.entry_find.get().strip()
                                if data.lower() in bai_hat['tenBH'].lower():
                                    id_value = bai_hat['id']
                                    tenBH_value = bai_hat['tenBH']
                                    loaiBH_value = bai_hat['loaiBH']
                                    self.tree2.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                                    vtri += 1
                        else:
                            messagebox.showerror("Thêm", "Bài hát đã tồn tại trong danh sách yêu thích")
                except ConnectionResetError as e:
                    print("Kết nối đã bị đóng bởi máy chủ từ xa.")
                except Exception as e:
                    print(f"Có lỗi xảy ra: {e}")
                    client.close()
            except Exception as e:
                print(f"Error playing selected song: {e}")

    def handleDelYeuThich(self):
        selected_item = self.tree2.selection()
        if selected_item:
            item_values = self.tree2.item(selected_item)["values"]
            id_bai_hat = item_values[1]
            try:
                if id_bai_hat is None:
                    print("No song selected.")
                    return
                host = '192.168.138.48'
                port = 1236
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                        client.connect((host, port))
                        # Gửi yêu cầu danh sách nhạc
                        request = f'DEL_MUSIC_ID_{id_bai_hat}'
                        client.sendall(request.encode())
                        print(f"Gửi yêu cùa thêm id yêu thích : {id_bai_hat}")

                        # Nhận kết quả từ server
                        response1 = client.recv(1024).decode('utf-8')
                        if response1 == 'del_thanhcong':
                            messagebox.showinfo("Xoá", "Bỏ bài hát yêu thích thành công")

                            # Gửi yêu cầu danh sách nhạc
                            client.sendall(b'GET_MUSIC_LIST_YEU_THICH')
                            serialized_data = client.recv(4096)
                            # Giải mã dữ liệu nhận được từ dạng bytes sang danh sách
                            data_received = pickle.loads(serialized_data)
                            self.danh_sach_bai_hat_yeu_thich = data_received
                            for item in self.tree2.get_children():
                                self.tree2.delete(item)
                            vtri = 1
                            for bai_hat in self.danh_sach_bai_hat_yeu_thich:
                                data = self.entry_find.get().strip()
                                if data.lower() in bai_hat['tenBH'].lower():
                                    id_value = bai_hat['id']
                                    tenBH_value = bai_hat['tenBH']
                                    loaiBH_value = bai_hat['loaiBH']
                                    self.tree2.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                                    vtri += 1
                except ConnectionResetError as e:
                    print("Kết nối đã bị đóng bởi máy chủ từ xa.")
                except Exception as e:
                    print(f"Có lỗi xảy ra: {e}")
                    client.close()
            except Exception as e:
                print(f"Error playing selected song: {e}")
    def handleFind(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        vtri = 1
        for bai_hat in self.danh_sach_bai_hat:
            data = self.entry_find.get().strip()
            if data.lower() in bai_hat['tenBH'].lower():
                id_value = bai_hat['id']
                tenBH_value = bai_hat['tenBH']
                loaiBH_value = bai_hat['loaiBH']
                self.tree.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                vtri += 1

    def handleFind2(self):
        for item in self.tree2.get_children():
            self.tree2.delete(item)
        vtri = 1
        for bai_hat in self.danh_sach_bai_hat_yeu_thich:
            data = self.entry_find2.get().strip()
            if data.lower() in bai_hat['tenBH'].lower():
                id_value = bai_hat['id']
                tenBH_value = bai_hat['tenBH']
                loaiBH_value = bai_hat['loaiBH']
                self.tree2.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                vtri += 1

    def play_music(self):
        self.isPlayStop = not self.isPlayStop
        if self.isPlayStop:
            self.button_play.config(image=self.imgPau)
            if self.xu_ly_baihat_path:
                pygame.mixer.music.load(io.BytesIO(self.xu_ly_baihat_path))
                pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path))
                pygame.mixer.music.play()

                length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
                start = self.canvas1.winfo_width() / (225 / length_in_secs)
                pygame.mixer.music.set_pos(start)
                self.is_playing = True
                self.start_counting(length_in_secs)
        else:
            self.button_play.config(image=self.imgPlay)
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                self.is_playing = False

    def start_counting(self, length_in_secs):
        self.length_in_secs = length_in_secs
        # print(self.length_in_secs)
        global thoiGian
        if self.is_playing:
            if thoiGian <= 225:
                thoiGian += (225 / self.length_in_secs)
                self.canvas1.config(width=thoiGian)
                print(thoiGian)
                print("---------------")
            else:
                thoiGian = 0
                self.canvas1.config(width=thoiGian)
                if self.isLap == False:
                    self.button_play.config(image=self.imgPau)
                    list_length = len(self.danh_sach_bai_hat)
                    current_index = None
                    for index, bai_hat in enumerate(self.danh_sach_bai_hat):
                        if bai_hat['id'] == self.id:
                            current_index = index + 1
                            break
                    if current_index >= list_length:
                        current_index = current_index - 1
                    self.id = self.danh_sach_bai_hat[current_index]['id']
                    self.setBaiHatMacDinh(self.id)
                    try:
                        if self.id is None:
                            print("No song selected.")
                            return
                        host = '192.168.138.48'
                        port = 1236
                        try:
                            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                                client.connect((host, port))
                                # Gửi yêu cầu danh sách nhạc
                                request = f'GET_MUSIC_ID_{self.id}'
                                client.sendall(request.encode())
                                print(f"yêu cầu lấy dữ liệu của id : {self.id}")
                                # Nhận dữ liệu âm nhạc từ server và lưu vào một tệp tạm
                                music_file_data = tempfile.SpooledTemporaryFile(max_size=10000000)
                                while True:
                                    data = client.recv(1024)
                                    if not data:
                                        break
                                    music_file_data.write(data)
                                print(music_file_data)
                                music_file_data.seek(0)
                                music_bytes = music_file_data.read()
                                self.xu_ly_baihat_path = music_bytes
                                pygame.mixer.music.load(io.BytesIO(music_bytes))
                                pygame.mixer.Sound(io.BytesIO(music_bytes))
                                pygame.mixer.music.play()
                                length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
                        except ConnectionResetError as e:
                            print("Kết nối đã bị đóng bởi máy chủ từ xa.")
                        except Exception as e:
                            print(f"Có lỗi xảy ra: {e}")
                            client.close()
                    except Exception as e:
                        print(f"Error playing selected song: {e}")
                else:
                    pygame.mixer.music.play()
            # Hủy bộ đếm thời gian hiện tại nếu có
            if self.timer_id is not None:
                self.parent.after_cancel(self.timer_id)
            # Thiết lập một bộ đếm thời gian mới
            self.timer_id = self.parent.after(1000, lambda: self.start_counting(self.length_in_secs))

    def xulyLap(self):
        self.isLap = not self.isLap
        if self.button_lap.cget('image') == str(self.imgRepeat):
            self.button_lap.config(image=self.imgRepeatNo)
        else:
            self.button_lap.config(image=self.imgRepeat)


    def phatNgauNhien(self):
        do_dai_ds_bai_hat = len(self.danh_sach_bai_hat)
        so_ngau_nhien = random.randint(0, do_dai_ds_bai_hat - 1)
        bai_hat_ngau_nhien = self.danh_sach_bai_hat[so_ngau_nhien]
        self.id = bai_hat_ngau_nhien['id']
        self.get_path_song(self.id)
        length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
        self.start_counting(length_in_secs)

    def lui_music(self):
        if self.id:
            current_index = None
            for index, bai_hat in enumerate(self.danh_sach_bai_hat):
                if bai_hat['id'] == self.id:
                    current_index = index - 1
                    break
            if current_index <= 0:
                current_index = 0
            self.id = self.danh_sach_bai_hat[current_index]['id']
            self.get_path_song(self.id)
            length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
            self.start_counting(length_in_secs)

    def next_music(self):
        if self.id:
            list_length = len(self.danh_sach_bai_hat)
            current_index = None
            for index, bai_hat in enumerate(self.danh_sach_bai_hat):
                if bai_hat['id'] == self.id:
                    current_index = index + 1
                    break
            if current_index >= list_length:
                current_index = current_index - 1
            self.id = self.danh_sach_bai_hat[current_index]['id']
            self.get_path_song(self.id)
            length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
            self.start_counting(length_in_secs)

    def chon_bai_hat(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)["values"]
            id_bai_hat = item_values[1]
            self.id = id_bai_hat
            self.get_path_song(self.id)
        length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
        self.start_counting(length_in_secs)


    def chon_bai_hat2(self):
        selected_item = self.tree2.selection()
        if selected_item:
            item_values = self.tree2.item(selected_item)["values"]
            id_bai_hat = item_values[1]
            self.id = id_bai_hat
            self.get_path_song(self.id)
        length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
        self.start_counting(length_in_secs)

    def get_path_song(self,id):
        self.setBaiHatMacDinh(id)
        self.canvas1.config(width=0)
        global thoiGian
        thoiGian = 0
        self.button_play.config(image=self.imgPau)
        self.isPlayStop = True
        try:
            if self.id is None:
                print("No song selected.")
                return
            host = '192.168.138.48'
            port = 1236
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                    client.connect((host, port))
                    # Gửi yêu cầu danh sách nhạc
                    request = f'GET_MUSIC_ID_{id}'
                    client.sendall(request.encode())
                    print(f"yêu cầu lấy dữ liệu của id : {id}")
                    # Nhận dữ liệu âm nhạc từ server và lưu vào một tệp tạm
                    music_file_data = tempfile.SpooledTemporaryFile(max_size=10000000)
                    while True:
                        data = client.recv(1024)
                        if not data:
                            break
                        music_file_data.write(data)
                    print(music_file_data)
                    music_file_data.seek(0)
                    music_bytes = music_file_data.read()
                    self.xu_ly_baihat_path = music_bytes
                    pygame.mixer.music.load(io.BytesIO(music_bytes))
                    pygame.mixer.Sound(io.BytesIO(music_bytes))
                    pygame.mixer.music.play()
                    self.is_playing = True
            except ConnectionResetError as e:
                print("Kết nối đã bị đóng bởi máy chủ từ xa.")
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")
                client.close()
        except Exception as e:
            print(f"Error playing selected song: {e}")

    def change_volume(self, event):
        volume_level = self.volume_scale.get()
        vol = 100 - volume_level
        pygame.mixer.music.set_volume(vol / 100)

    def on_canvas_click(self, event):
        if pygame.mixer.music.get_busy():
            length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
            global thoiGian
            self.canvas1.config(width=event.x)
            start = event.x / (225 / length_in_secs)
            pygame.mixer.music.set_pos(start)
            thoiGian = event.x

    def on_canvas1_click(self, event):
        if pygame.mixer.music.get_busy():
            length_in_secs = pygame.mixer.Sound(io.BytesIO(self.xu_ly_baihat_path)).get_length()
            global thoiGian
            self.canvas1.config(width=event.x)
            start = event.x / (225 / length_in_secs)
            pygame.mixer.music.set_pos(start)
            thoiGian = event.x

    def on_combobox_select(self, event):
        selected_value = self.combobox_loaiBH.get()
        if selected_value == 'Tất cả':
            self.hien_thi_danh_sach_bai_hat()
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)
            vtri = 1
            for bai_hat in self.danh_sach_bai_hat:
                if bai_hat['loaiBH'] == selected_value:
                    id_value = bai_hat['id']
                    tenBH_value = bai_hat['tenBH']
                    loaiBH_value = bai_hat['loaiBH']
                    self.tree.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                    vtri += 1

    def on_combobox_select2(self, event):
        selected_value = self.combobox_loaiBH2.get()
        if selected_value == 'Tất cả':
            self.hien_thi_danh_sach_bai_hat_yeu_thich()
        else:
            for item in self.tree2.get_children():
                self.tree2.delete(item)
            vtri = 1
            for bai_hat in self.danh_sach_bai_hat_yeu_thich:
                if bai_hat['loaiBH'] == selected_value:
                    id_value = bai_hat['id']
                    tenBH_value = bai_hat['tenBH']
                    loaiBH_value = bai_hat['loaiBH']
                    hinhAnh_value = bai_hat['hinhAnh']
                    link_value = bai_hat['link']
                    self.tree2.insert("", "end", values=(vtri, id_value, tenBH_value, loaiBH_value))
                    vtri += 1

    def logout(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.is_playing = False
        self.root.destroy()  # Đóng cửa sổ hiện tại
        self.parent_window.deiconify()  # Mở cửa sổ gốc

    def on_tab_changed(self, event):
        current_tab = self.tab_control.index(self.tab_control.select())
        print(f"Tab hiện tại: {current_tab}")

# def on_closing(music_tab):
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         music_tab.stop_music()
#         root.destroy()

# def main():
#     global roots
#     root = tk.Tk()
#     root.title("Ứng dụng nghe nhạc")
#
#     window_width = 750
#     window_height = 450
#     root.geometry(f"{window_width}x{window_height}")
#     music_tab = MusicTab(root)
#     root.protocol("WM_DELETE_WINDOW", lambda: on_closing(music_tab))
#     MusicTab(root)
#
#     root.mainloop()
#
#
# if __name__ == "__main__":
#     main()
