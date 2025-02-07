from models.user import User
from typing import List

class UserRepository:
    Users: List[User] = []
    
    def add_user(self, user: User):
        new_user = User(
                email=user.email,
                fullname=user.fullname,
                password=user.password,
                user_id=len(self.Users) + 1  
            )
        self.Users.append(new_user)
    def autho_user(self, email: str, password: str):
        for user in self.Users:
            if user.email == email and user.password == password:
                return True
        return False

    def get_user_by_email(self, email: str):
        for user in self.Users:
            if user.email == email:
                return user
        return None
    
    def get_all_users(self):
        return self.Users

    def get_user_by_userid(self, user_id: int):
        for user in self.Users:
            if user.user_id == user_id:
                return user
        return None
    



    
    
