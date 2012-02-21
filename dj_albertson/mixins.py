from django.conf import settings


class DjangoSettingsMixin(object):
    '''
    A mixin for CounterPools that automatically pulls configuration info in
    from the Django settings module.
    '''

    def __init__(self, *args, **kwargs):
        new_settings = self.get_settings()
        new_settings.update(kwargs)

        super(DjangoSettingsMixin, self).__init__(*args, **new_settings)

    def get_settings(self):
        new_settings = {}

        new_settings.update(self.try_generic_settings())
        new_settings.update(self.try_namespaced_settings())

        return new_settings

    def build_settings(self, aws_access_key, aws_secret_key, read_units=None, write_units=None, auto_create_table=None):
        new_settings = {}

        if aws_access_key and aws_secret_key:
            new_settings['aws_access_key'] = aws_access_key
            new_settings['aws_secret_key'] = aws_secret_key

        if read_units:
            new_settings['read_units'] = read_units

        if write_units:
            new_settings['write_units'] = write_units

        if auto_create_table is not None:
            new_settings['auto_create_table'] = auto_create_table

        return new_settings

    def try_namespaced_settings(self):
        aws_access_key = getattr(settings, 'ALBERTSON_AWS_ACCESS_KEY', None)
        aws_secret_key = getattr(settings, 'ALBERTSON_AWS_SECRET_KEY', None)
        read_units = getattr(settings, 'ALBERTSON_DEFAULT_READ_UNITS', None)
        write_units = getattr(settings, 'ALBERTSON_DEFAULT_WRITE_UNITS', None)
        auto_create_table = getattr(settings, 'ALBERTSON_AUTO_CREATE_TABLE', None)

        return self.build_settings(
            aws_access_key,
            aws_secret_key,
            read_units,
            write_units,
            auto_create_table,
        )

    def try_generic_settings(self):
        aws_access_key = getattr(settings, 'AWS_ACCESS_KEY_ID', None)
        aws_secret_key = getattr(settings, 'AWS_SECRET_ACCESS_KEY', None)

        return self.build_settings(aws_access_key, aws_secret_key)
