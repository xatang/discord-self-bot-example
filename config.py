import os

debug = True

##################
if debug == True:
    from pyaml_env import parse_config

    config = parse_config("docker-compose.yml")
    config = config["services"]["discord_bot"]["environment"]
    temp_config = {}
    for item in config:
        item_str = item.split("=", 1)
        temp_config[item_str[0]] = item_str[1]
    config = temp_config
else:
    config = os.environ
##################

bot_token = config["TOKEN"]
owner_id = int(config["OWNER_ID"])
