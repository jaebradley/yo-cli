import click
import yo_client

from src.account_details import get_account_details


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
def send(to, message):
    details = get_account_details()
    if details.api_key:
        client = yo_client.YoClient(details.api_key)
        response = client.send_yo(username=to, text=message)
        print(response)


yo.add_command(set_username)
yo.add_command(set_api_key)
yo.add_command(send)
