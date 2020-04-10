from datetime import date

from db.orm import dbInterface
from db.tables import BrowniePoints


class Brownie():
    def __init__(self, profile_id, num_claps, message):
        self.profile_id = profile_id
        self.num_claps = num_claps
        self.message = message

class BrownieService():
    def save_brownies(self, brownie_giver_profile_id, brownies):
        for brownie in brownies:
            self._save_brownies_to_db(brownie_giver_profile_id, brownie)

    def _save_brownies_to_db(self, brownie_giver_profile_id, brownie):
        bp = BrowniePoints(points=brownie.num_claps, comments=brownie.message, effective_date=date.today(),
                           giver_profile_id=brownie_giver_profile_id, profile_id=brownie.profile_id)
        dbInterface.create_brownie_points(bp)

brownieService = BrownieService()
