import settings
from slackclient import SlackClient

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


def hello(channel, greeting):
    client = SlackClient(token)

    print client.api_call("im.open", user="U0S04BRMJ")
    print client.api_call("chat.postMessage",
                          as_user="false",
                          channel=channel,
                          text=greeting)

def main(token):
    channel = "#bot-testing"
    greeting = "Hello world!"
    hello(channel, greeting)


if __name__ == "__main__":
    token = settings.SLACK_API_TOKEN
    main(token)
