from dataclasses import dataclass
from typing import Dict, Optional
import re


@dataclass
class UserProfile:
    user_id: str
    name: str
    email: str
    phone: str
    active: bool = True


class UserProfileService:

    def __init__(self):
        self.users: Dict[str, UserProfile] = {}

    def create_profile(self, user_id, name, email, phone):

        if user_id in self.users:
            raise ValueError("User already exists")

        if not self.validate_email(email):
            raise ValueError("Invalid email")

        profile = UserProfile(
            user_id=user_id,
            name=name,
            email=email,
            phone=phone
        )

        self.users[user_id] = profile
        return profile

    def get_profile(self, user_id):

        return self.users.get(user_id)

    def update_name(self, user_id, name):

        profile = self.get_profile(user_id)

        if not profile:
            raise ValueError("User not found")

        profile.name = name

        return profile

    def update_email(self, user_id, email):

        profile = self.get_profile(user_id)

        if not profile:
            raise ValueError("User not found")

        if not self.validate_email(email):
            raise ValueError("Invalid email")

        profile.email = email

        return profile

    def update_phone(self, user_id, phone):

        profile = self.get_profile(user_id)

        if not profile:
            raise ValueError("User not found")

        profile.phone = phone

        return profile

    def deactivate_profile(self, user_id):

        profile = self.get_profile(user_id)

        if not profile:
            raise ValueError("User not found")

        profile.active = False

        return profile

    def activate_profile(self, user_id):

        profile = self.get_profile(user_id)

        if not profile:
            raise ValueError("User not found")

        profile.active = True

        return profile

    def delete_profile(self, user_id):

        if user_id not in self.users:
            raise ValueError("User not found")

        del self.users[user_id]

    def profile_exists(self, user_id):

        return user_id in self.users

    def list_active_profiles(self):

        return [
            profile
            for profile in self.users.values()
            if profile.active
        ]

    def list_all_profiles(self):

        return list(self.users.values())

    def search_by_name(self, keyword):

        keyword = keyword.lower()

        return [
            profile
            for profile in self.users.values()
            if keyword in profile.name.lower()
        ]

    def search_by_email(self, email):

        for profile in self.users.values():
            if profile.email == email:
                return profile

        return None

    def validate_email(self, email):

        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        return re.match(pattern, email) is not None

    def total_users(self):

        return len(self.users)

    def total_active_users(self):

        return len(self.list_active_profiles())
