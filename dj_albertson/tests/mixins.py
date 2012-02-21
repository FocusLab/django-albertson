from ConfigParser import SafeConfigParser
from copy import copy
import os
import unittest

from albertson.base import CounterPool

from boto.exception import NoAuthHandlerFound

from django.conf import settings

from dj_albertson.mixins import DjangoSettingsMixin


class DjangoCounterPool(DjangoSettingsMixin, CounterPool):
    '''
    Simple CounterPool decendent used to test the DjangoSettingsMixin.
    '''


class SettingsMixinTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.config = self.get_config()

        super(SettingsMixinTests, self).__init__(*args, **kwargs)

    def tearDown(self):
        settings_to_clear = [
            'AWS_ACCESS_KEY_ID',
            'AWS_SECRET_ACCESS_KEY',
            'ALBERTSON_AWS_ACCESS_KEY',
            'ALBERTSON_AWS_SECRET_KEY',
        ]

        for setting in settings_to_clear:
            if hasattr(settings, setting):
                delattr(settings, setting)

    def get_config(self):
        config = SafeConfigParser()
        config.read([
            'test.ini',
            os.path.expanduser('~/.dj_albertson_test.ini'),
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), '../test.ini'
                )
            )
        ])

        return config

    def test_missing_settings(self):
        with self.assertRaises(NoAuthHandlerFound):
            DjangoCounterPool()

    def test_generic_settings(self):
        settings.AWS_ACCESS_KEY_ID = self.config.get('aws', 'access_key')
        settings.AWS_SECRET_ACCESS_KEY = self.config.get('aws', 'secret_key')
        DjangoCounterPool()

    def test_namespaced_settings(self):
        settings.ALBERTSON_AWS_ACCESS_KEY = self.config.get('aws', 'access_key')
        settings.ALBERTSON_AWS_SECRET_KEY = self.config.get('aws', 'secret_key')
        settings.ALBERTSON_DEFAULT_READ_UNITS = self.config.getint('albertson', 'read_units')
        settings.ALBERTSON_DEFAULT_WRITE_UNITS = self.config.getint('albertson', 'write_units')
        settings.ALBERTSON_AUTO_CREATE_TABLE = self.config.getboolean('albertson', 'auto_create_table')

        pool = DjangoCounterPool()

        self.assertEquals(self.config.getint('albertson', 'read_units'), pool.read_units)
        self.assertEquals(self.config.getint('albertson', 'write_units'), pool.write_units)
        self.assertEquals(self.config.getboolean('albertson', 'auto_create_table'), pool.auto_create_table)

    def test_kwargs_override(self):
        settings.ALBERTSON_AWS_ACCESS_KEY = 'bad'
        settings.ALBERTSON_AWS_SECRET_KEY = 'value'
        DjangoCounterPool(
            aws_access_key=self.config.get('aws', 'access_key'),
            aws_secret_key=self.config.get('aws', 'secret_key'),
        )

    def test_cascading(self):
        settings.ALBERTSON_AWS_ACCESS_KEY = self.config.get('aws', 'access_key')
        settings.ALBERTSON_AWS_SECRET_KEY = self.config.get('aws', 'secret_key')
        settings.AWS_ACCESS_KEY_ID = 'bad'
        settings.AWS_SECRET_ACCESS_KEY = 'value'
        DjangoCounterPool()
