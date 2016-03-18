import settings
from slackclient import SlackClient

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


def message(channel, greeting):
    sc = SlackClient(token)

    print sc.api_call("chat.postMessage",
                          as_user="false",
                          channel=channel,
                          text=greeting)

def main(token):
    channel = "#bot-testing"
    greeting = "Hello world!"
    message(channel, greeting)


if __name__ == "__main__":
    token = settings.SLACK_API_TOKEN
    main(token)
