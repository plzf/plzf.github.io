from webex_bot.webex_bot import WebexBot
from PLZFboto.4.0 import findplz

api_token = "ZTA1M2EwODUtMTUyOC00N2M0LThjMWEtNzFhOGUyM2JhNjNkOTQ5NmNhY2ItOTg5_PE93_b6c69aac-d199-4628-980a-d750015d67a5"

bot = WebexBot(api_token) 

bot.add_command(findplz())

bot.run()
