import settings
from slackclient import SlackClient

import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


def main():
    token = settings.SLACK_API_TOKEN
    client = SlackClient(token)

    channel = "#bot-testing"
    greeting = "Hello world!"

    print client.api_call("im.open", user="U0S04BRMJ")
    print client.api_call("chat.postMessage", as_user="false", channel=channel, text=greeting)


if __name__ == "__main__":
    main()
