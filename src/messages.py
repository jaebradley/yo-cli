import emoji
import termcolor

USER_ERROR_MESSAGE = termcolor.colored(emoji.emojize(':frowning: :confused: :anguished: :sweat:  Looks like there was a problem with the recipient, message, or link! :frowning: :confused: :anguished: :sweat:',
                                                     use_aliases=True),
                                       'red',
                                       attrs=['bold'])


def generate_successful_message(yo_id, recipient):
    return termcolor.colored(emoji.emojize(':+1:  Sent Yo #{yo_id} to {recipient}! :+1:'
                                           .format(yo_id=yo_id, recipient=recipient),
                             use_aliases=True),
                             'green',
                             attrs=['bold'])


def generate_unknown_error_message(e):
    return termcolor.colored(emoji.emojize(':astonished: :rage: :sob: :confounded:  Unknown error: {message} :astonished: :rage: :sob: :confounded:')
                             .format(message=e.message if hasattr(e, 'message') else e))


