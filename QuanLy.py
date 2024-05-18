import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

from src.BUS.baihatBUS import BaiHatBUS
from src.BUS.userBUS import UserBUS
from src.BUS.baihatyeuthichBUS import BaiHatYeuThichBUS

user_bus = UserBUS()
baihatyeuthich_bus = BaiHatYeuThichBUS()
baihat_bus = BaiHatBUS()
class QuanLyTab:
    def __init__(self, parent):
        self.parent = parent
        self.selected_image = None
        self.tenAnh = None
        self.selected_music_path = tk.StringVar()
        self.isCheck = False
        self.id = None

        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill='both', expand=True)

        self.tab1 = ttk.Frame(parent)
        self.notebook.add(self.tab1, text='Admin')

        self.label_tenBH = tk.Label(self.tab1, text="Nhập tên bài hát:")
        self.label_tenBH.place(x=10, y=10)

        self.entry_tenBH = tk.Entry(self.tab1, width=28)
        self.entry_tenBH.place(x=150, y=10)

        self.label_loaiBH = tk.Label(self.tab1, text="Chọn thể loại:")
        self.label_loaiBH.place(x=10, y=55)

        self.combobox_loaiBH = ttk.Combobox(self.tab1, values=["Rap", "Trẻ", "Nhạc Xưa", "Nước Ngoài"], width=25)
        self.combobox_loaiBH.place(x=150, y=55)

        self.button_chon_hinhAnh = tk.Button(self.tab1, text="Chọn hình ảnh", command=self.chon_hinhAnh)
        self.button_chon_hinhAnh.place(x=450, y=10)

        self.image_label = tk.Label(self.tab1)
        self.image_label.place(x=550, y=10)

        self.button_chon_nhac = tk.Button(self.tab1, text="Chọn file nhạc", command=self.chon_nhac)
        self.button_chon_nhac.place(x=10, y=100)

        self.music_entry_label = tk.Label(self.tab1, textvariable=self.selected_music_path)
        self.music_entry_label.place(x=150, y=100)

        self.tree = ttk.Treeview(self.tab1, columns=("STT", "ID", "Tên bài hát", "Thể loại", "Hình ảnh", "Nhạc"),
                                 show="headings")
        self.tree.heading("STT", text="STT")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tên bài hát", text="Tên bài hát")
        self.tree.heading("Thể loại", text="Thể loại")
        self.tree.heading("Hình ảnh", text="Hình ảnh")
        self.tree.heading("Nhạc", text="Nhạc")
        # Định dạng cột cho Treeview
        self.tree.column("STT", width=30)
        self.tree.column("ID", width=30)
        self.tree.column("Tên bài hát", width=150)
        self.tree.column("Thể loại", width=80)
        self.tree.column("Hình ảnh", width=120)
        self.tree.column("Nhạc", width=120)

        # Scrollbar cho Treeview
        self.tree_scroll = ttk.Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        # Đặt vị trí của Treeview và Scrollbar
        self.tree.place(x=10, y=190, width=700, height=180)
        self.tree_scroll.place(x=710, y=190, height=180)

        # Tạo các nút chức năng
        self.button_them = tk.Button(self.tab1, text="Lưu", command=self.them_bai_hat, width=10)
        self.button_them.place(x=440, y=385)

        self.button_sua = tk.Button(self.tab1, text="Sửa", command=self.sua_bai_hat, width=10)
        self.button_sua.place(x=540, y=385)

        self.button_xoa = tk.Button(self.tab1, text="Xóa", command=self.xoa_bai_hat, width=10)
        self.button_xoa.place(x=640, y=385)

        self.button_lam_moi = tk.Button(self.tab1, text="Làm mới", command=self.reset_data, width=10)
        self.button_lam_moi.place(x=640, y=140)

        danh_sach_bai_hat = baihat_bus.load_data_bai_hat()
        if danh_sach_bai_hat:
            # Cập nhật danh sách bài hát của ứng dụng với danh sách từ cơ sở dữ liệu
            self.danh_sach_bai_hat = danh_sach_bai_hat
            self.hien_thi_danh_sach_bai_hat()

        # Tạo tab 2 và thêm vào notebook
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text='User')

        self.label_title = tk.Label(self.tab2, text="Danh sách User")
        self.label_title.place(x=10, y=10)

        # Tạo ttk.Treeview trong tab2
        self.tree_tab2 = ttk.Treeview(self.tab2, columns=("STT", "ID", "Username", "Password"),
                                      show="headings")
        self.tree_tab2.heading("STT", text="STT")
        self.tree_tab2.heading("ID", text="ID")
        self.tree_tab2.heading("Username", text="Username")
        self.tree_tab2.heading("Password", text="Password")
        # Định dạng cột cho Treeview trong tab2
        self.tree_tab2.column("STT", width=20)
        self.tree_tab2.column("ID", width=20)
        self.tree_tab2.column("Username", width=100)
        self.tree_tab2.column("Password", width=100)

        # Scrollbar cho Treeview trong tab2
        self.tree_scroll_tab2 = ttk.Scrollbar(self.tab2, orient="vertical", command=self.tree_tab2.yview)
        self.tree_tab2.configure(yscrollcommand=self.tree_scroll_tab2.set)

        # Đặt vị trí của Treeview và Scrollbar trong tab2
        self.tree_tab2.place(x=10, y=40, width=300, height=280)
        self.tree_scroll_tab2.place(x=310, y=40, height=280)

        self.button_xem = tk.Button(self.tab2, text="Xem",command=self.hien_thi_baihatyeuthich, width=10)
        self.button_xem.place(x=230, y=340)

        # Tạo ttk.Treeview thứ hai trong tab2
        self.tree_tab2_2 = ttk.Treeview(self.tab2, columns=("STT", "Tên bài hát", "Thể loại"), show="headings")
        self.tree_tab2_2.heading("STT", text="STT")
        self.tree_tab2_2.heading("Tên bài hát", text="Tên bài hát")
        self.tree_tab2_2.heading("Thể loại", text="Thể loại")
        # Định dạng cột cho Treeview thứ hai trong tab2
        self.tree_tab2_2.column("STT", width=30)
        self.tree_tab2_2.column("Tên bài hát", width=180)
        self.tree_tab2_2.column("Thể loại", width=80)

        # Scrollbar cho Treeview thứ hai trong tab2
        self.tree_scroll_tab2_2 = ttk.Scrollbar(self.tab2, orient="vertical", command=self.tree_tab2_2.yview)
        self.tree_tab2_2.configure(yscrollcommand=self.tree_scroll_tab2_2.set)

        # Đặt vị trí của Treeview thứ hai và Scrollbar trong tab2
        self.tree_tab2_2.place(x=360, y=40, width=340, height=280)
        self.tree_scroll_tab2_2.place(x=710, y=40, height=280)

        self.label_title1 = tk.Label(self.tab2, text="Danh sách Bài hát yêu thích")
        self.label_title1.place(x=360, y=10)

        self.label_nameUser = tk.Label(self.tab2, font=("Arial", 10, "bold"))
        self.label_nameUser.place(x=570, y=10)

        danh_sach_user = user_bus.get_all_users()
        if danh_sach_user:
             # Cập nhật danh sách bài hát của ứng dụng với danh sách từ cơ sở dữ liệu
            self.danh_sach_user = danh_sach_user
            self.hien_thi_danh_sach_user()

    def hien_thi_danh_sach_bai_hat(self):
        # Xóa toàn bộ dữ liệu hiện có trên Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        vtri = 1
        for bai_hat in self.danh_sach_bai_hat:
            self.tree.insert("", "end", values=(vtri,bai_hat.id, bai_hat.tenBH, bai_hat.loaiBH, bai_hat.hinhAnh, bai_hat.link))
            vtri += 1

    def hien_thi_danh_sach_user(self):
        # Xóa toàn bộ dữ liệu hiện có trên Treeview
        for item in self.tree_tab2.get_children():
            self.tree_tab2.delete(item)

        vtri = 1
        for user in self.danh_sach_user:
            self.tree_tab2.insert("", "end",
                                  values=(vtri, user['id'], user['username'], user['password']))
            vtri += 1

    def hien_thi_baihatyeuthich(self):
        selected_items = self.tree_tab2.selection()
        for item in selected_items:
            item_values = self.tree_tab2.item(item, 'values')
            id_value = item_values[1]
            userName = item_values[2]
            self.label_nameUser.config(text=f"Username : {userName}")
            filtered_bai_hat = []
            danh_sach_bai_hat = baihat_bus.load_data_bai_hat()
            if danh_sach_bai_hat:
                arr_list = [bai_hat.__dict__ for bai_hat in danh_sach_bai_hat]
                danh_sach_bai_hat_yeu_thich = baihatyeuthich_bus.get_all_baihat_yeuthich_byID_user(id_value)
                if danh_sach_bai_hat_yeu_thich:
                    for bai_hat in arr_list:
                        for item in danh_sach_bai_hat_yeu_thich:
                            id_bai_hat = item['id_baihat']
                            if bai_hat['id'] == id_bai_hat:
                                filtered_bai_hat.append(bai_hat)
            # Xóa toàn bộ dữ liệu hiện có trên Treeview
            for item in self.tree_tab2_2.get_children():
                self.tree_tab2_2.delete(item)
            vtri = 1
            for baihat_yt in filtered_bai_hat:
                self.tree_tab2_2.insert("", "end",
                                      values=(vtri, baihat_yt['tenBH'], baihat_yt['loaiBH']))
                vtri += 1
    def them_bai_hat(self):
        # Kiểm tra xem các trường thông tin đã được nhập đầy đủ
        ten_bai_hat = self.entry_tenBH.get().strip()
        loai_bai_hat = self.combobox_loaiBH.get().strip()
        ten_anh = self.tenAnh
        file_nhac = self.selected_music_path.get()  # Lấy đường dẫn file nhạc đã chọn

        if ten_bai_hat and loai_bai_hat and ten_anh and file_nhac:
                ten_bai_hat = ten_bai_hat.capitalize()
                if self.isCheck == False:
                    ktra = baihat_bus.add(ten_bai_hat, loai_bai_hat, ten_anh, file_nhac)
                    if ktra:
                        danh_sach_bai_hat = baihat_bus.load_data_bai_hat()
                        if danh_sach_bai_hat:
                            self.reset_data()
                            self.danh_sach_bai_hat = danh_sach_bai_hat
                            self.hien_thi_danh_sach_bai_hat()
                else:
                    ktra = baihat_bus.update(self.id,ten_bai_hat, loai_bai_hat, ten_anh, file_nhac)
                    if ktra:
                        self.isCheck = False
                        danh_sach_bai_hat = baihat_bus.load_data_bai_hat()
                        if danh_sach_bai_hat:
                            self.reset_data()
                            self.danh_sach_bai_hat = danh_sach_bai_hat
                            self.hien_thi_danh_sach_bai_hat()
        else:
            # Nếu thiếu thông tin, hiển thị thông báo lỗi
            tk.messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin bài hát và chọn hình ảnh, file nhạc.")

    def sua_bai_hat(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.isCheck = True
            item_values = self.tree.item(selected_item)["values"]
            id_bai_hat = item_values[1]
            ten_bai_hat = item_values[2]
            loai_bai_hat = item_values[3]
            hinh_anh = item_values[4]
            link_bai_hat = item_values[5]
            self.id = id_bai_hat
            self.tenAnh = hinh_anh
            self.entry_tenBH.delete(0, tk.END)
            self.entry_tenBH.insert(0, ten_bai_hat)
            self.combobox_loaiBH.set(loai_bai_hat)
            self.selected_music_path.set(link_bai_hat)
            if hinh_anh:
                image_path = os.path.join(r'D:/App_Music_python/src/img',hinh_anh)
                if os.path.exists(image_path):
                    # Load hình ảnh sử dụng PIL
                    image = Image.open(image_path)
                    image.thumbnail((100, 100))  # Thay đổi kích thước hình ảnh
                    photo = ImageTk.PhotoImage(image)
                    self.image_label.config(image=photo)
                    self.image_label.image = photo  # Giữ tham chiếu để hình ảnh không bị garbage collected
                else:
                    print(f"Không tìm thấy hình ảnh: {image_path}")
            else:
                print("Không có hình ảnh được chọn.")
    def xoa_bai_hat(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)["values"]
            if item_values:
                item_id = int(item_values[1])
                ten_bai_hat = item_values[2]
                confirmation = messagebox.askyesno("Xác nhận xóa",
                                                   f"Bạn có chắc chắn muốn xóa bài hát '{ten_bai_hat}' không?")
                if confirmation:
                    if baihat_bus.delete(item_id):
                        messagebox.showinfo("Thông báo", f"Đã xóa bài hát '{ten_bai_hat}' thành công!")
                        danh_sach_bai_hat = baihat_bus.load_data_bai_hat()
                        if danh_sach_bai_hat:
                            self.reset_data()
                            self.danh_sach_bai_hat = danh_sach_bai_hat
                            self.hien_thi_danh_sach_bai_hat()
                    else:
                        messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi xóa bài hát '{ten_bai_hat}'!")



    def chon_hinhAnh(self):
        # Mở cửa sổ để chọn hình ảnh từ máy tính
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            ten_anh = os.path.basename(file_path)
            self.tenAnh = ten_anh
            # Hiển thị hình ảnh đã chọn trên giao diện
            self.selected_image = Image.open(file_path)
            self.selected_image.thumbnail((100, 100))  # Thay đổi kích thước hình ảnh
            photo = ImageTk.PhotoImage(self.selected_image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Giữ tham chiếu để hình ảnh không bị garbage collected

    def chon_nhac(self):
        # Mở cửa sổ để chọn file nhạc từ máy tính
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            # print("Đường dẫn file nhạc đã chọn:", file_path)
            file_name = os.path.basename(file_path)
            # Cập nhật đường dẫn file nhạc đã chọn
            self.selected_music_path.set(file_name)

    def reset_data(self):
        # Xóa nội dung trong trường nhập liệu và đặt lại các biến
        self.entry_tenBH.delete(0, tk.END)
        self.combobox_loaiBH.set('')
        self.selected_music_path.set('')
        self.tenAnh = None

        # Xóa hiển thị hình ảnh trên label
        if self.image_label is not None and hasattr(self.image_label, 'image'):
            self.image_label.image = None  # Bỏ tham chiếu đến đối tượng PhotoImage
            self.image_label.config(image=None)  # Đặt lại cấu hình của label

        # Xóa nội dung trong treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.hien_thi_danh_sach_bai_hat()

def main():
    root = tk.Tk()
    root.title("Ứng dụng quản lý bài hát")

    window_width = 740
    window_height = 450
    root.geometry(f"{window_width}x{window_height}")

    quan_ly_tab = QuanLyTab(root)

    root.mainloop()

if __name__ == "__main__":
    main()
