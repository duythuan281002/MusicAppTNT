from src.DAO.baihatDAO import BaiHatDAO
class BaiHatBUS:
    def __init__(self):
        self.dao = BaiHatDAO()
    def load_data_bai_hat(self):
        return self.dao.load_data_bai_hat()
    def get_linkBH(self, id):
        return self.dao.get_linkBH(id)

    def add(self, tenBH, loaiBH, hinhAnh, link):
        return self.dao.add(tenBH, loaiBH, hinhAnh, link)

    def update(self, id_bai_hat, tenBH, loaiBH, hinhAnh, link):
        return self.dao.update(id_bai_hat, tenBH, loaiBH, hinhAnh, link)

    def delete(self, id_bai_hat):
        return self.dao.delete(id_bai_hat)

    def get_latest_song(self, id):
        return self.dao.get_latest_song(id)

    def get_max_id(self):
        return self.dao.get_max_id()

    def get_by_the_loai(self, the_loai):
        return self.dao.get_by_the_loai(the_loai)

