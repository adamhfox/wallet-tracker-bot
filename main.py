
import  tweepy
import threading
import time
import discord
import discum
from discord import Webhook, RequestsWebhookAdapter
import config

api_secret = "BfKWSvOlIaMucaTPYbdftmCgKWXwoydS0S7TTg7wO7I2ep8fTV"
api_key = "XdCvyY78qP6ml6ZqKhpURXmcR"
bearer_token="AAAAAAAAAAAAAAAAAAAAAHBwgwEAAAAAEta0j69l3NY0f0i%2FCHd0NYuVY68%3Dm4fm9LwMD1emRMSavuI0HG60W2YPE7UYSpDUgWJn2DOTA7bQM8"
client_id = "1499505057200578562-ng2DIVhaPxVlcbJUoouRe81zJMTzbL"
client_secret = "NIraDrqzEOVyzU1V6hlT7KK8Q7suga6aYKezxk3IEoQGo"


client = tweepy.Client(bearer_token, api_key, api_secret, client_id, client_secret)


#auth = tweepy.OAuth1UserHandler(api_key, api_secret, client_id, client_secret)
#api = tweepy.API(auth)


#client.create_tweet(text="New profile pic @fastdagod")





bot = discum.Client(token=config.token, log=False)

channels_webhooks = {}


@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental:
        try:
            user = bot.gateway.session.user
            print(f"Forwarding bot started. Logged in as {user['username']}#{user['discriminator']}")
            guilds = bot.gateway.session.guilds
            for guild_id, guild in guilds.items():
                bot.gateway.request.lazyGuild(guild_id, {1: [[0, 99]]}, typing=True, threads=False, activities=True, members=[])
        except Exception as e:
            return
    if resp.event.message:
        m = resp.parsed.auto()
        if str(m['channel_id']) in channels_webhooks.keys():
            for webhook_url in channels_webhooks[str(m['channel_id'])]:
                webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())

                if config.webhook_username != "":
                    username = config.webhook_username
                else:
                    username = f"{m['author']['username']}#{m['author']['discriminator']}"

                if config.webhook_profile_picture_URL != "":
                    avatar_url = config.webhook_profile_picture_URL
                else:
                    avatar_url = f"https://cdn.discordapp.com/avatars/{m['author']['id']}/{m['author']['avatar']}"

                if config.show_replied_to_messages and 'referenced_message' in list(m) and m['referenced_message']:
                    
                    if config.remove_custom_emojis:
                        content = remove_emojis(m['referenced_message']['content'])
                    else:
                        content = m['referenced_message']['content']

                    if config.remove_mentions:
                        content = remove_mentions(content)
                    
                    text = f"(**in reply to {m['referenced_message']['author']['username']}#{m['referenced_message']['author']['discriminator']}:** {content.strip()})"
                    webhook.send(text, username=username, avatar_url=avatar_url)

                if m['content'] and m['content'] != "":
                    try:
                        if config.remove_custom_emojis:
                            text = remove_emojis(m['content'])
                        else:
                            text = m['content']

                        if config.remove_mentions:
                            text = remove_mentions(text)

                        webhook.send(text.strip(), username=username, avatar_url=avatar_url)
                    except Exception as e:
                        pass

                if len(m['attachments']) > 0:
                    for attachment in m['attachments']:
                        try:
                            webhook.send(attachment['url'], username=username, avatar_url=avatar_url)
                        except Exception as e:
                            pass

                if len(m['embeds']) > 0:
                    for i in range(len(m['embeds'])):
                        content = m['embeds'][i]

                        if 'type' in list(content) and (content['type'] == 'image' or content['type'] == 'video' or content['type'] == 'gifv'):
                            continue

                        embed = discord.Embed(title="", description="")
                        try:
                            embed.title = content['title']
                        except Exception as e:
                            pass
                        try:
                            embed.url = content['url']
                        except Exception as e:
                            pass
                        try:
                            embed.colour = content['color']
                        except Exception as e:
                            pass
                        try:
                            embed.description = content['description']
                        except Exception as e:
                            pass
                        try:
                            embed.set_thumbnail(url="https://gateway.pinata.cloud/ipfs/QmQmyojU6z9nKUFFiqYBdRSnWwincm3KwnhQeHAH4ghMkX")
                        except Exception as e:
                            pass
                        try:
                            embed.set_image(url=content['image']['url'])
                        except Exception as e:
                            pass
                        try:
                            embed.set_footer(text="Powered by Potheads HQ", icon_url="https://gateway.pinata.cloud/ipfs/QmQmyojU6z9nKUFFiqYBdRSnWwincm3KwnhQeHAH4ghMkX")
                        except Exception as e:
                            pass
                        try:
                            embed.set_author(name=content['author']['name'], url="")
                        except Exception as e:
                            pass

                        if 'fields' in content.keys():
                            for field in content['fields']:
                                try:
                                    name = field['name']
                                    value = field['value']

                                    if name == "":
                                        name = "\u200b"
                                    if value == "":
                                        value = "\u200b"
                                    embed.add_field(name=name, value=value, inline=field['inline'])
                                except Exception as e:
                                    continue

                        try:
                            name = content['author']['name'].replace("Unknown", "")
                            """
                            if "skellymode" in name.lower():
                                name = "@0xskellymode"
                            if "jawn" in name.lower():
                                name = "@Jawnxwick"
                            if "hge" in name.lower():
                                name = "@HGESOL"
                            if "emperor" in name.lower():
                                name = "@Solana_Emperor"
                            """

                            #webhook.send(embed=embed, username=username, avatar_url=avatar_url)
                            tweet_text = "Your favorite influencer " + name + "\n" + "\n"
                            tweet_text = tweet_text + content['title'].replace("NFT", "") + "\n"
                            test_description = embed.description.split('\n')
                            #tweet_text = tweet_text + embed.description
                            tweet_text = tweet_text + test_description[0].replace("*","") + "\n" + test_description[4].replace("[ME link](", "").replace(")", "")

                            tweet_text = tweet_text + "\n" + "\n" + "#Solana #SolanaNFT #NFTGiveaway"
                            client.create_tweet(text=tweet_text)

                            if "skelly" in name.lower():
                                name = "@0xskellymode"
                        except Exception as e:
                            continue


def remove_mentions(text):
    new_text = text
    try:
        i = 0
        while i < len(new_text):
            if new_text[i] == '<' and i + 1 < len(new_text) and (new_text[i + 1] == '!' or new_text[i + 1] == '@'):
                for j in range(i, len(new_text), 1):
                    if new_text[j] == '>':
                        new_text = new_text[:i] + new_text[j+1:]
                        break
            i += 1

        return new_text.replace('   ', ' ').replace('  ', ' ')
    except Exception as e:
        return text


def remove_emojis(text):

    # Replace custom animated emojis
    new_text = text
    try:
        i = 0
        while i < len(new_text):
            if new_text[i] == '<' and i + 2 < len(new_text) and new_text[i + 1] == 'a' and new_text[i + 2] == ':':
                for j in range(i, len(new_text), 1):
                    if new_text[j] == '>':
                        new_text = new_text[:i] + new_text[j + 1:]
                        break
            i += 1

        new_text = new_text.replace('   ', ' ').replace('  ', ' ')
    except Exception as e:
        pass

    # Replace custom emojis
    try:
        i = 0
        while i < len(new_text):
            if new_text[i] == '<' and i + 1 < len(new_text) and new_text[i + 1] == ':':
                for j in range(i, len(new_text), 1):
                    if new_text[j] == '>':
                        new_text = new_text[:i] + new_text[j + 1:]
                        break
            i += 1

        new_text = new_text.replace('   ', ' ').replace('  ', ' ')
    except Exception as e:
        pass

    # Replace failed emojis
    try:
        i = 0
        while i < len(new_text):
            if new_text[i] == ':' and i + 1 < len(new_text) and new_text[i + 1] != ' ' and new_text[i + 1] != '/':
                for j in range(i+1, len(new_text), 1):
                    if new_text[j] == ':':
                        new_text = new_text[:i] + new_text[j+1:]
                        break
            i += 1

        return new_text.replace('   ', ' ').replace('  ', ' ')
    except Exception as e:
        return text


def scan_channel_webhooks():
    global channels_webhooks

    while True:
        new_channels_webhooks = {}

        with open(config.channels_webhooks_file_path, "r") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]

        for line in lines:
            if ' ' not in line or line == "" or line == "\n":
                continue

            if line.endswith('\r'):
                line = line[:-2]

            splits = line.split(" ")
            channel = splits[0]
            webhook = splits[1]
            if channel not in new_channels_webhooks.keys():
                new_channels_webhooks[channel] = []
            new_channels_webhooks[channel].append(webhook)

        channels_webhooks = new_channels_webhooks
        time.sleep(config.scan_interval_seconds)


thread = threading.Thread(target=scan_channel_webhooks, args=())
thread.start()
bot.gateway.run()
