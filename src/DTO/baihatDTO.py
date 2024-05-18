class BaiHatDTO:
    def __init__(self, id, tenBH,loaiBH, hinhAnh, link):
        self.id = id
        self.tenBH = tenBH
        self.loaiBH = loaiBH
        self.hinhAnh = hinhAnh
        self.link = link

    def get_id(self):
        return self.id

    def get_tenBH(self):
        return self.tenBH

    def get_hinhAnh(self):
        return self.hinhAnh

    def get_link(self):
        return self.link

    def get_loaiBH(self):
        return self.loaiBH

    def set_tenBH(self, tenBH):
        self.tenBH = tenBH

    def set_hinhAnh(self, hinhAnh):
        self.hinhAnh = hinhAnh

    def set_link(self, link):
        self.link = link

    def set_loaiBH(self, loaiBH):
        self.loaiBH = loaiBH

