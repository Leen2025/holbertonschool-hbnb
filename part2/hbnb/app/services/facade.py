class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    # Existing methods...
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # New methods to implement
    def get_all_users(self):
        """Retrieve all users from the repository"""
        return self.user_repo.list_all()

    def update_user(self, user_id, user_data):
        """Update a user's information"""
        user = self.user_repo.get(user_id)
        if not user:
            return None

        # Update user attributes
        for key, value in user_data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        return user
