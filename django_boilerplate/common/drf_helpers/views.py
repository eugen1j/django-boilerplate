from typing import Type, Optional

from django.db.models import Model, Field
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_dataclasses.serializers import DataclassSerializer

from django_boilerplate.common.drf_helpers.utils import deserialize, serialize


class DataclassRequestMixin:
    """Mixin for APIView with Dataclass object in self.request.data"""

    request_serializer_class: Type[DataclassSerializer]

    def data(self):
        return deserialize(self.request_serializer_class, self.request.data)  # noqa


class DataclassListResponseMixin:
    """Mixin for APIView with list Dataclass objects for response"""

    response_serializer_class: Type[DataclassSerializer]

    def response(self, results):
        return serialize(self.response_serializer_class, results, many=True)


class DataclassView(APIView, DataclassRequestMixin, DataclassListResponseMixin):
    """
    View that receives Dataclass in request
    and returns list of Dataclasses in response
    """

    def results(self, request_data):
        return []

    def get(self, *args, **kwargs):
        request_data = self.data()
        results = self.results(request_data)
        response_data = self.response(results)
        return Response(response_data)


class ChoicesMixin:
    model = Type[Model]

    @action(
        detail=False, methods=["GET"], name="Get choices for all Model's ChoiceFields"
    )
    def choices(self, request, *args, **kwargs):
        model_choices = {}
        for field in self.model._meta.fields:  # noqa
            assert isinstance(field, Field)
            if field.choices is not None:
                model_choices[field.name] = dict(field.choices)

        return Response(model_choices)


class LabelsMixin:
    """
    Mixin for retrieving Model field's labels
    """

    model = Type[Model]

    @action(detail=False, methods=["GET"], name="Get labels for all Model's Fields")
    def labels(self, request, *args, **kwargs):
        labels = {}
        for field in self.model._meta.fields:  # noqa
            assert isinstance(field, Field)
            labels[field.name] = dict(field.verbose_name)

        return Response(labels)


class DictionaryMixin:
    label_field: Optional[str] = None

    def get_label(self, instance) -> str:
        if self.label_field is not None:
            return str(getattr(instance, self.label_field))
        return str(instance)

    @action(detail=False, methods=["GET"], name="List Models in id-label format")
    def dictionary(self, request, *args, **kwargs):
        get_label = self.get_label

        class DynamicSerializer(serializers.Serializer):
            id = serializers.IntegerField()
            label = serializers.SerializerMethodField()

            def get_label(self, instance):
                return get_label(instance)

        class DynamicListAPIView(self.__class__):
            serializer_class = DynamicSerializer

        return DynamicListAPIView(**self.__dict__).list(
            request, *args, **kwargs
        )  # noqa
