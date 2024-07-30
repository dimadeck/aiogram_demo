class AdminMessages:
    @staticmethod
    def show_users(users):
        return "\n".join([f"{user.name}({user.id})\n" for user in users])
