""" slacker.py - My initial attempt at a Slack bot to learn about the slack
    APIs and do a few useful things.
"""

import settings
import requests
from slackclient import SlackClient

# Needed for SSL support on my machine, at least
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


def message(channel, text):
    sc = SlackClient(token)

    print sc.api_call("chat.postMessage",
                          as_user="false",
                          channel=channel,
                          text=text)

def pull_req_check(channel, repo_url):
    resp = requests.get(repo_url)
    if resp.content == '[]':
        message(channel, "{0} has no pull requests".format(repo_url))
    else:
        message(channel, "{0} pull requests:\n".format(repo_url))
        print "more to come soon..."

def main(token):
    channel = "#bot-testing"
    repo_url = "https://api.github.com/repos/uw-it-aca/scout/pulls"
    pull_req_check(channel, repo_url)


if __name__ == "__main__":
    token = settings.SLACK_API_TOKEN
    main(token)
