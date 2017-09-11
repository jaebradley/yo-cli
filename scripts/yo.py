import click
import yo_client
from requests.exceptions import HTTPError

from src.data import get_account_details
from src.messages import USER_ERROR_MESSAGE, generate_successful_message, generate_unknown_error_message


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
            print(generate_successful_message(yo_id=yo_id, recipient=recipient))
        except HTTPError:
            print(USER_ERROR_MESSAGE)
        except BaseException as e:
            print(generate_unknown_error_message(e))

yo.add_command(set_username)
yo.add_command(set_api_key)
yo.add_command(send)
