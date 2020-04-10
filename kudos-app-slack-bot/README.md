This is a basic application of slackbots in the real world.

**Use Case**
 
We would like to give a team member a few brownie points for their work in a particular project.
The company would like to keep track of these brownie points so that they can simplify their
performance review process. Rather than creating an app (or a website) to let users give kudos,
we can use slack to give one.

**Workflow**

Lets assume that employees are using slack in their company.
1. Edison (@edison, edison@example.com)
1. Issac Newton (@issac_newton, issac_newton@example.com)
1. Albert Einstein (@albert_einstein, albert_einstein@example.com)

Now, lets say @edison, would like to give kudos to @issac_newton and  @albert_einstein. He could do

```
Hey @brownie_genie, give 10 claps to @issac_newton, for without him we may not have found the law of gravity.
Hey @brownie_genie, give 10 claps to @albert_einstein, for without him we may not have found the theory of relativity.
```

Wouldn't it be nice if we can capture this in a database and keep track of the kudos. 
Hopefully, we will know which employees are more engaged in terms of getting the actual work done :)

**Backend Data**

This garage github code captures this information into a backend table named ('BrowniePoints').
The messages can be accessed as follows:

```
for bp in list(profileService.get_brownie_points_from_work_email("albert_einstein@example.com")):
    name = bp.profile.first_name + " " + bp.profile.last_name
    print("{} received this appreciation : {}".format(name, bp.profile.bp.comments))  

``` 

**Setup Highlevel**

1. Setup the `brownie_genie` bot and provide the necessary permissions. See steps below.
1. Setup a virtualenv for python3
1. Download the `slack-bot` folder and do `pip install -r requirements.txt`
1. Setup env variables, see details below
1. Create the backend tables by running python tables.py. It should create a file called `db/sqlalchemy_example.db`
1. Edit setup_dummy_data.py with the details of the users who are available in your slack. The email id in the profile objects should match that of the information in slack
1. Setup ngrok tunneling so that the localhost server can be accessed via a publicly accessible url
1. Configure the ngrok url in slack 
1. Run python server/app.py
1. Now give kudos in slack as explained above

**Setup Details for some of the non trivial ones**

***Slack Setup***

This setup assumes that your slack environment has 3 users
1. Edison (edison@example.com)
1. Issac Newton (issac.newton@example.com)
1. Albert Einstein (albert.einstein@example.com)

Now, lets add the `brownie_genie` bot. In `slack` parlance, this bot is an app. Follow the steps in [here](https://github.com/slackapi/python-slackclient/blob/master/tutorial/01-creating-the-slack-app.md) to create the `brownie_genie` bot.
Once you do this, go to the `Event Subscriptions` section in https://api.slack.com for your bot and then subscribe to the `app_mention` event. Once you save changes, reinstall the app.

***Setup virtualenv***

virtualenv -p python3 venv_p3
source venv_p3/bin/activate

***Setup env variables***

This project requires two env variables

1. export SLACK_BOT_TOKEN='....'. You can copy the value of this from `OAuth & Permissions` section of your https://api.slack.com section for your bot.
1. export SLACK_SIGNING_SECRET='....' You can copy the value of this from `Basic Information` section of your https://api.slack.com section for your bot.

You can also follow the steps outlined [here](https://github.com/slackapi/python-slackclient/blob/master/tutorial/04-running-the-app.md) to get the env values

***ngrok setup***

This is very straightforward. Goto [ngrok](https://ngrok.com/download) and follow the steps. You will need to signin to get your Auth token.

***Configure the ngrok url in your slack account***

Follow the steps outlined in the [`Subscribe to Events`](https://github.com/slackapi/python-slackclient/blob/master/tutorial/04-running-the-app.md
) section

