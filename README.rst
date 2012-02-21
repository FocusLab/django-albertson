================
django-albertson
================

Homepage:  https://github.com/FocusLab/django-albertson

Integration library for Django and `Albertson <https://github.com/FocusLab/Albertson>`_.

---
Use
---

DjangoSettingsMixin
===================

`dj_albertson.mixins.DjangoSettingsMixin`

This mixin provides automatic loading of default settings for a CounterPool
from the django settings module.

Below is an example use::

    from albertson import CounterPool
    from dj_albertson.mixins import DjangoSettingsMixin

    class MyCounter(DjangoSettingsMixin, CounterPool):
        '''
        That's it, your done!
        '''

Once you've added this mixin to your counter pool classes, the following
settings will be used:

ALBERTSON_AWS_ACCESS_KEY
    The AWS access key id that will be used to access DynamoDB.  This is the
    setting that will be used if both `AWS_ACCESS_KEY_ID` and
    `ALBERTSON_AWS_ACCESS_KEY` are provided.

ALBERTSON_AWS_SECRET_KEY
    The AWS secet key that will be used to access DynamoDB.  This is the
    setting that will be used if both `AWS_SECRET_ACCESS_KEY` and
    `ALBERTSON_AWS_SECRET_KEY` are provided.

AWS_ACCESS_KEY_ID
    A more generic form of `ALBERTSON_AWS_ACCESS_KEY`

AWS_SECRET_ACCESS_KEY
    A more generic form of `ALBERTSON_AWS_SECRET_KEY`

ALBERTSON_DEFAULT_READ_UNITS
    The default read throughput that will be set on newly created tables.

    **default:** 3

ALBERTSON_DEFAULT_WRITE_UNITS
    The default write throughput that will be set on newly created tables.

    **default:** 5

ALBERTSON_AUTO_CREATE_TABLE
    A flag to control how Albertson should behave when it tries to use a
    table that doesn't exist.  If set to `True`, Albertson will create a new
    table.  If set to `False`, Albertson will allow the underlying boto
    exception to bubble up through the stack.

    **default:** True
