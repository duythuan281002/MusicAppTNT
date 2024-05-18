from src.DAO.userDAO import UserDAO

class UserBUS:
    def __init__(self):
        self.user_dao = UserDAO()

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)

    def create_user(self, username, password):
        return self.user_dao.create_user(username, password)

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_id(self, username, password):
        return self.user_dao.get_id(username, password)

    def get_username(self, username):
        return self.user_dao.get_username(username)