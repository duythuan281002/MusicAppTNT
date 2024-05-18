class BaiHatYeuThichDTO:
    def __init__(self, baihat_yeuthich_id, user_id, yeuthich_id):
        self.baihat_yeuthich_id = baihat_yeuthich_id
        self.user_id = user_id
        self.yeuthich_id = yeuthich_id

    def get_baihat_yeuthich_id(self):
        return self.baihat_yeuthich_id

    def set_baihat_yeuthich_id(self, baihat_yeuthich_id):
        self.baihat_yeuthich_id = baihat_yeuthich_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_yeuthich_id(self):
        return self.yeuthich_id

    def set_yeuthich_id(self, yeuthich_id):
        self.yeuthich_id = yeuthich_id