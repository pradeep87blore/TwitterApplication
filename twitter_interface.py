"""
File that acts as an interface to the twitter calls
"""

import twitter
from utils import get_tokens, get_proxy

class TwitterHandler:

    def __init__(self):
        self.twitterTokens = get_tokens()

        http_proxy, https_proxy = get_proxy()

        self.api = twitter.Api(consumer_key=self.twitterTokens['consumer_key'],
                          consumer_secret=self.twitterTokens['consumer_secret'],
                          access_token_key=self.twitterTokens['access_token'],
                          access_token_secret=self.twitterTokens['access_token_secret'],
                               proxies={'http':http_proxy, 'https':https_proxy})

    def print_credentials(self):
        print(self.api.VerifyCredentials())

    def print_user_status(self, user_handle):
        statuses = self.api.GetUserTimeline(screen_name=user_handle)

        print(type(statuses))
        for s in statuses:
            print(s.AsDict())
