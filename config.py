# User account token. Check the included get_auth_token.png file to learn how to find your token
token = "NzI4NDk4MTQyNTQyMTY4MDc2.G4WG0x.4v1G1lvsqrS2b5oY8uPMX0sM2df1QGHKEr2Ges"

# Time (in seconds) between updating the list of channels/webhooks from the text file
scan_interval_seconds = 120

# Path of the file where the channels and webhooks are specified
channels_webhooks_file_path = "channels_webhooks.txt"

# Set to True if the bot should remove any custom/failed emojis from the original messages
# Set to False otherwise
remove_custom_emojis = True

# Set to True if the bot should remove any mentions from the original messages (normally show up as deleted-role)
# Set to False otherwise
remove_mentions = True

# Set to True if the bot should show messages that are being replied to (in case the new message is replying to any other)
# Set to False otherwise.
# If set to True, the bot will only be able to show the text of the message that is being replied to
show_replied_to_messages = True

# Webhook username. Leave empty if you want the bot to try and use the username of the original message sender
webhook_username = "PotHeads HQ"

# Webhook profile picture URL. Leave empty if you want the bot to try and use the profile picture of the original message sender
# URL must be a direct link to the picture itself, not a google images search page. To make sure it is a direct link,
# when you click it and open it, a new tab should open and there should be nothing in it but the image
webhook_profile_picture_URL = "https://gateway.pinata.cloud/ipfs/QmQmyojU6z9nKUFFiqYBdRSnWwincm3KwnhQeHAH4ghMkX"
