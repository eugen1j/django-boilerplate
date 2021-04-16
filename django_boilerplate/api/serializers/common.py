from dataclasses import dataclass

from rest_framework_dataclasses.serializers import DataclassSerializer


@dataclass
class FieldChoice:
    value: str
    label: str


class FieldChoiceSerializer(DataclassSerializer):
    class Meta:
        dataclass = FieldChoice
