import logging
import os
import ssl as ssl_lib

import certifi
from flask import Flask
from slackeventsapi import SlackEventAdapter

from services.slack import slackService

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app)

@slack_events_adapter.on("app_mention")
def capture_claps(payload):
    event = payload.get("event", {})
    user_id = event.get("user")
    text = event.get("text")
    if slackService.has_claps(text):
        slackService.save_brownies(user_id, text)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)
