from rest_framework import ISO_8601
from rest_framework import serializers
from django.conf import settings


class CustomDateTimeField(serializers.DateTimeField):

    def to_representation(self, value):
        if not value:
            return None

        output_format = getattr(self, 'format', settings.DATETIME_FORMAT)

        if output_format is None or isinstance(value, str):
            return value

        value = self.enforce_timezone(value)

        if output_format.lower() == ISO_8601:
            value = value.isoformat()
            # remove lines that convert "+00:00" to "Z"
            # See https://github.com/encode/django-rest-framework/blob/f4cf0260bf3c9323e798325702be690ca25949ca/rest_framework/fields.py#L1239:L1240
            return value
        return value.strftime(output_format)