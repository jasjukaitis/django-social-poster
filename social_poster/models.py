# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractSocialPoster(models.Model):
    """Abstract base model for the social poster."""

    post_twitter = models.BooleanField(_(u'Post on Twitter'), default=True)
    post_facebook = models.BooleanField(_(u'Post on Facebook'), default=True)

    class Meta:
        abstract = True

    @property
    def post_on_twitter(self):
        """If True, then post on Twitter.

        Separate boolean for easy overriding if there are further conditions
        (e.g. page must be public).
        """
        return self.post_twitter

    @property
    def post_on_fcebook(self):
        """If True, then post on Facebook.

        Separate boolean for easy overriding if there are further conditions
        (e.g. page must be public).
        """
        return self.post_facebook

    @property
    def twitter_message(self):
        """Returns the whole message for Twitter."""
        return ''

    @property
    def facebook_message(self):
        """Returns the whole Facebook message as a dict.

        Example:
            {
                'path': '/me/feed',
                'message': 'Message',
                'link': 'http://example.com',
            }
        """
        return {}

    def disable_post_on_twitter(self):
        """After posting on Twitter, set the flag to False for preventing a
        double post."""
        self.post_twitter = False
        self.save()

    def disable_post_on_facebook(self):
        """After posting on Facebook, set the flag to False for preventing a
        double post."""
        self.post_facebook = False
        self.save()
