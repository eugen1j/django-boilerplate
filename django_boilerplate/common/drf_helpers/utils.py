from typing import Type

from rest_framework.serializers import Serializer


def deserialize(serializer_class: Type[Serializer], data, *,
                raise_exception=True, **kwargs):
    """Deserialize data by serializer_class. Returns instance."""
    serializer: Serializer = serializer_class(data=data, **kwargs)
    serializer.is_valid(raise_exception=raise_exception)
    return serializer.save()


def serialize(serializer_class: Type[Serializer], instance, *, many=False, **kwargs):
    """
    Serializer instance by serializer_class. Returns serialized data.
    """
    serializer: Serializer = serializer_class(instance=instance, many=many, **kwargs)
    return serializer.data
