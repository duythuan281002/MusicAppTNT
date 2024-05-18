from src.DAO.baihatyeuthichDAO import BaiHatYeuThichDAO

class BaiHatYeuThichBUS:
    def __init__(self):
        self.baihat_yeuthich_dao = BaiHatYeuThichDAO()

    def add_baihat_yeuthich(self, id_user, id_yeuthich):
        return self.baihat_yeuthich_dao.add_baihat_yeuthich(id_user, id_yeuthich)

    def delete_baihat_yeuthich(self, id_baihat, id_user):
        return self.baihat_yeuthich_dao.delete_baihat_yeuthich(id_baihat, id_user)

    def get_all_baihat_yeuthich(self):
        return self.baihat_yeuthich_dao.get_all_baihat_yeuthich()

    def get_all_baihat_yeuthich_byID_user(self, id_user):
        return self.baihat_yeuthich_dao.get_all_baihat_yeuthich_byID_user(id_user)

    def exists_baihatyeuthich(self, id_user, id_baihat):
        return self.baihat_yeuthich_dao.exists_baihatyeuthich(id_user, id_baihat)
