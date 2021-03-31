from typing import Type

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class RelatedField(serializers.PrimaryKeyRelatedField):
    # https://stackoverflow.com/questions/29950956/drf-simple-foreign-key-assignment-with-nested-serializers
    def __init__(self, serializer: Type[ModelSerializer], **kwargs):
        self.serializer = serializer
        if (not hasattr(self.serializer, 'Meta')
                or not hasattr(self.serializer.Meta, 'model')):  # noqa
            raise AttributeError('"serializer" has no Meta.model attribute')
        if kwargs.get('read_only') is not True:
            kwargs['queryset'] = kwargs.pop(
                'queryset', self.serializer.Meta.model.objects.all())  # noqa
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)
