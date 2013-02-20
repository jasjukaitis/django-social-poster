# -*- coding: utf-8 -*-
"""Signals for posting to Twitter and Facebook."""

import twitter, urllib2
from facepy import GraphAPI

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def post_to_twitter(sender, instance, *args, **kwargs):
    if not instance.post_on_twitter:
        return False
    required = ('TWITTER_CONSUMER_KEY',
                'TWITTER_CONSUMER_SECRET',
                'TWITTER_ACCESS_TOKEN_KEY',
                'TWITTER_ACCESS_TOKEN_SECRET')
    conf = {}
    for e in required:
        try:
            conf[e] = getattr(settings, e)
        except AttributeError:
            raise ImproperlyConfigured('%s does not exist.' % e)
    try:
        twitter_api = twitter.Api(
            consumer_key=conf['TWITTER_CONSUMER_KEY'],
            consumer_secret=conf['TWITTER_CONSUMER_SECRET'],
            access_token_key=conf['TWITTER_ACCESS_TOKEN_KEY'],
            access_token_secret=conf['TWITTER_ACCESS_TOKEN_SECRET'])
        twitter_api.PostUpdate(instance.twitter_message)
    except urllib2.HTTPError:
        return False
    instance.disable_post_on_twitter()


def post_to_facebook(sender, instance, *args, **kwargs):
    if not instance.post_on_facebook:
        return False
    try:
        access_token = settings.FACEBOOK_ACCESS_TOKEN
    except AttributeError:
        raise ImproperlyConfigured('FACEBOOK_ACCESS_TOKEN does not exist.')
    graph = GraphAPI(access_token)
    graph.post(**instance.facebook_message)
    instance.disable_post_on_facebook()
