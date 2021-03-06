from ..log import vulnerability
from ..utils import change_parameter, modify_parameter, get_page_text

SYMBOLS = {'"', "'", '<', '{', '(', ')', '}', '>', '&', '|', u"\U0001D550"}
DETECT_STRING = "test"


def test_for_detect_form(form, name, client):
    test_value = modify_parameter(dict(form.get_parameters()), name,
                                  DETECT_STRING)
    value = form.send(client, test_value)

    for text in get_page_text(value):
        if DETECT_STRING in text:
            return True


def try_on_form(form, client, symbol, name):
    guessed_parameters = dict(form.get_parameters())
    parameters = modify_parameter(guessed_parameters, name,
                                  symbol)
    attacked_page = form.send(client, parameters)

    for text in get_page_text(attacked_page):
        if symbol in text:
            return

    vulnerability(form.action, 'Incorrect Unicode Handling!')


def test_for_detect_url(url, parameter, client):
    test_value = change_parameter(url, parameter, DETECT_STRING)
    value = client.download_page(test_value)

    for element in get_page_text(value):
        if DETECT_STRING in element:
            return True


def try_on_url(url, parameter, client, symbol):
    new_url = change_parameter(url, parameter, symbol.encode('utf-8'))
    attacked_page = client.download_page(new_url)

    for element in get_page_text(attacked_page):
        if symbol in element:
            return

    vulnerability(url, 'Incorrect Unicode handling in URL')


def exotic_characters(target_page, client):
    for form in target_page.get_forms():
        for name in form.get_parameters():
            if test_for_detect_form(form, name, client):
                for symbol in SYMBOLS:
                    try_on_form(form, client, symbol, name)

    for parameter, _ in target_page.get_url_parameters:
        if test_for_detect_url(target_page.url, parameter, client):
            for symbol in SYMBOLS:
                try_on_url(target_page.url, parameter, client, symbol)
