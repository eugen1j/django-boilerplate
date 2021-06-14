from typing import Type

import coreapi
import coreschema
from django.db.models import Choices, IntegerChoices
from rest_framework.filters import BaseFilterBackend


class BaseKeyFilter(BaseFilterBackend):
    """Filter by foreign or primary key implementation."""

    key: str

    def _get_pk_parameter(self, params):
        if self.key not in params:
            return None
        else:
            return [int(key) for key in params[self.key].split(",")]

    def filter_queryset(self, request, queryset, view):
        """Parse pk parameter, filter results."""
        params = request.query_params
        filtered_ids = self._get_pk_parameter(params)
        if filtered_ids is not None:
            queryset = queryset.filter(**{f"{self.key}__in": filtered_ids})
        return queryset

    def get_schema_fields(self, view):
        """Return schema for filter parameters."""
        return [
            coreapi.Field(
                name=self.key,
                required=False,
                location="query",
                schema=coreschema.String(description=f"filter objects by {self.key}"),
            ),
        ]


class BaseChoicesFilter(BaseFilterBackend):
    """Filter by choice field implementation."""

    choices: Type[Choices]  # allowed choices
    field: str  # choice field

    def _get_choice_parameter(self, params):
        """Filter unsupported values"""
        if self.field not in params:
            return None
        else:
            return [
                choice
                for choice in params[self.field].split(",")
                if choice in self.choices.values
            ]

    def filter_queryset(self, request, queryset, view):
        """Parse choice field parameter, filter results."""
        params = request.query_params
        filtered_choices = self._get_choice_parameter(params)
        if filtered_choices is not None:
            queryset = queryset.filter(**{f"{self.field}__in": filtered_choices})
        return queryset

    def get_schema_fields(self, view):
        """Return schema for filter parameters."""
        return [
            coreapi.Field(
                name=self.field,
                required=False,
                location="query",
                schema=coreschema.String(
                    description=f"filter objects by {self.field}",
                ),
            ),
        ]


class BaseIntegerChoicesFilter(BaseChoicesFilter):
    """Filter by integer choice field implementation."""

    choices: IntegerChoices

    def _get_choice_parameter(self, params):
        """Filter unsupported values"""
        if self.field not in params:
            return None
        else:
            return [
                int(choice)
                for choice in params[self.field].split(",")
                if choice in self.choices.values and choice.isdigit()
            ]


def key_filter(key_: str):
    class DynamicFilter(BaseKeyFilter):
        key = key_

    return DynamicFilter


def choices_filter(choices_: Type[Choices], field_: str) -> Type[BaseChoicesFilter]:
    class DynamicFilter(BaseChoicesFilter):
        choices = choices_
        field = field_

    return DynamicFilter


def integer_choices_filter(
    choices_: IntegerChoices, field_: str
) -> Type[BaseIntegerChoicesFilter]:
    class DynamicFilter(BaseIntegerChoicesFilter):
        choices = choices_
        field = field_

    return DynamicFilter
