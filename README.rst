====================
Django-Social-Poster
====================

Signals for posting messages on Facebook and Twitter.


Requirements
============

  * Django
  * facepy
  * python-twitter


Installation
============

Using PyPI you can simply type into a terminal::

  pip install django-social-poster

or::

  easy_install django-social-poster


Configuration
=============

Add ``social_poster`` to the list of ``INSTALLED_APPS`` in your ``settings.py``
file.


Following settings are required:


Twitter
-------

  * ``TWITTER_CONSUMER_KEY``
  * ``TWITTER_CONSUMER_SECRET``
  * ``TWITTER_ACCESS_TOKEN_KEY``
  * ``TWITTER_ACCESS_TOKEN_SECRET``

You have to create a `new Twitter application
<https://dev.twitter.com/apps/new>`_. After creating one, the four required
strings are in the details tab. Please make sure that the application can write.
You can set the permissions in the settings tab.


Facebook
--------

  * ``FACEBOOK_ACCESS_TOKEN``: You can get the required access token at the `Graph Explorer <https://developers.facebook.com/tools/explorer/>`_


In your models, you have to create a new model which inherits from
``social_poster.models.AbstractSocialPoster``. Please override
``twitter_message`` and ``facebook_message``, because they are empty. Don't forget to sync your database!


Last but not least, add signals::

  from social_poster import signals
  models.signals.post_save.connect(signals.post_to_twitter,
                                   sender=MyModel)
  models.signals.post_save.connect(signals.post_to_facebook,
                                   sender=MyModel)


Author
======

Copyright 2013 Raphael Jasjukaitis <webmaster@raphaa.de>


Released under the BSD license.
