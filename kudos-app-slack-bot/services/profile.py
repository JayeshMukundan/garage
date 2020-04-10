from functools import lru_cache

from db.orm import dbInterface


class ProfileService():
    @lru_cache(maxsize=10)
    def get_profiles(self):
        return dbInterface.get_all_profiles()

    def get_profile_info_by_id(self):
        all_profiles = self.get_profiles()
        return {p.id: p for p in all_profiles}

    def get_profile_name_from_email(self, email):
        profile = self.get_profile_info_by_work_email()[email]
        return profile.first_name + ' ' + profile.last_name

    def get_profile_info_by_work_email(self):
        all_profiles = self.get_profiles()
        return {p.work_email: p for p in all_profiles}

    @lru_cache(maxsize=10)
    def get_profile_id_from_work_email(self, email):
        return self.get_profile_info_by_work_email().get(email).id

    def get_brownie_points_from_work_email(self, email):
        profile_id = self.get_profile_id_from_work_email(email)
        return dbInterface.get_all_brownie_points(profile_id)

profileService = ProfileService()
