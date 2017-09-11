import click
import yo_client
from requests.exceptions import HTTPError
import emoji

from src.data import get_account_details


@click.group()
def yo():
    pass


@click.command()
@click.option('--username', type=click.STRING, prompt='Your username, please')
def set_username(username):
    details = get_account_details()
    details.username = username
    details.update_username()


@click.command()
@click.option('--api_key', type=click.STRING, prompt='Your api key, please')
def set_api_key(api_key):
    details = get_account_details()
    details.api_key = api_key
    details.update_api_key()


@click.command()
@click.option('--to', type=click.STRING, prompt='Send to whom?')
@click.option('--message', type=click.STRING, prompt='What is your message?')
@click.option('--link', type=click.STRING)
def send(to, message, link):
    details = get_account_details()
    if details.api_key:
        client = yo_client.YoClient(details.api_key)
        try:
            response = client.send_yo(username=to, text=message, link=link)
            recipient = response['recipient']['username']
            yo_id = response['yo_id']
            print(emoji.emojize(':+1: Sent Yo #{yo_id} to {recipient}! :+1:'.format(yo_id=yo_id, recipient=recipient),
                                use_aliases=True))
        except HTTPError:
            print(emoji.emojize(':frowning: :confused: :anguished: :sweat:  Looks like there was a problem with the recipient, message, or link! :frowning: :confused: :anguished: :sweat:',
                                use_aliases=True))
        except BaseException as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

yo.add_command(set_username)
yo.add_command(set_api_key)
yo.add_command(send)
