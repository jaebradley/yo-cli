import emoji
import termcolor

USERNAME_NOT_SET_MESSAGE = termcolor.colored(emoji.emojize(':poop: Your username is not set! :poop:', use_aliases=True), 'red', attrs=['bold'])
API_KEY_NOT_SET_MESSAGE = termcolor.colored(emoji.emojize(':poop:  Your api key is not set! :poop:', use_aliases=True), 'red', attrs=['bold'])

USER_ERROR_MESSAGE = termcolor.colored(emoji.emojize(':frowning: :confused: :anguished: :sweat:  Looks like there was a problem with the recipient, message, or link! :frowning: :confused: :anguished: :sweat:',
                                                     use_aliases=True),
                                       'red',
                                       attrs=['bold'])


def generate_successful_message(yo_id, recipient):
    return termcolor.colored(emoji.emojize(':100:  Sent Yo #{yo_id} to {recipient}! :100:'
                                           .format(yo_id=yo_id, recipient=recipient),
                             use_aliases=True),
                             'green',
                             attrs=['bold'])


def generate_unknown_error_message(e):
    return termcolor.colored(emoji.emojize(':astonished: :rage: :sob: :confounded:  Unknown error: {message} :astonished: :rage: :sob: :confounded:')
                             .format(message=e.message if hasattr(e, 'message') else e))


