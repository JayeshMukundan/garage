import os
import re
from functools import lru_cache

from slack import WebClient

from .brownie import Brownie, BrownieService
from .profile import profileService


class SlackService():
    BOT_USER_NAME = 'covid_service'
    def __init__(self):
        # Initialize a Web API client
        self.slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
        self.brownie_service = BrownieService()

    @lru_cache(maxsize=100)
    def get_users_info(self):
        response = self.slack_web_client.users_list()
        if response['ok']:
            users_info = {}
            for user in response['members']:
                users_info[user['id']] = user
            return users_info
        else:
            return None

    def get_user_name(self, id):
        user_info = self.get_users_info()[id]
        return user_info.get('name') if user_info else None

    def get_user_email(self, id):
        user_info = self.get_users_info()[id]
        return user_info['profile'].get('email') if user_info else None

    @lru_cache(maxsize=1)
    def get_bot_user_id(self):
        for user in self.get_users_info().values():
            if user['name'] == SlackService.BOT_USER_NAME:
                return user['id']
        return None

    def has_claps(self, text):
        bot_user_id = self.get_bot_user_id()
        if '<@{}>'.format(bot_user_id) in text and re.search("(\d+)\s+claps\s+to.+?\<\@(\w+)\>", text):
            return True
        else:
            return False

    def save_brownies(self, brownie_giver_id, text):
        claps_group = re.search("(\d+)\s+claps\s+to.+?\<\@(\w+)\>", text)
        brownies = []

        brownie_giver_email_id = self.get_user_email(brownie_giver_id)
        brownie_giver_profile_id = profileService.get_profile_id_from_work_email(brownie_giver_email_id)
        num_claps = claps_group.group(1)
        slack_user_id = claps_group.group(2)
        comments = text[claps_group.span()[1]:]
        user_email = self.get_user_email(slack_user_id)
        user_profile_id = profileService.get_profile_id_from_work_email(user_email)
        b = Brownie(user_profile_id, num_claps, comments)
        brownies.append(b)
        self.brownie_service.save_brownies(brownie_giver_profile_id, brownies)


slackService = SlackService()
