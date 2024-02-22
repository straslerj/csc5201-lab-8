class UserService:
    users = []
    user_id_counter = 1

    @classmethod
    def list_users(cls):
        print(f"{cls.users=}")
        return cls.users

    @classmethod
    def create_user(cls, user_data):
        user_data["id"] = cls.user_id_counter
        cls.user_id_counter += 1
        cls.users.append(user_data)
        print(f"{cls.users=}")
        return user_data

    @classmethod
    def delete_user(cls, user_id):
        user_id = int(user_id)
        for user in cls.users:
            if user["id"] == user_id:
                cls.users.remove(user)
                return {"message": f"User with id {user_id} deleted"}
        return {"error": f"User with id {user_id} not found"}
