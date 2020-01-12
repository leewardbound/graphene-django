import graphene
from django.utils.functional import SimpleLazyObject
from graphene.relay import Node
from rest_framework import serializers

from graphene_django import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

from ..models import MyFakeModelWithChoices


class ChoicesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFakeModelWithChoices
        fields = "__all__"


def test_register_choices_serializer_mutation():
    class ModelType(DjangoObjectType):
        class Meta:
            model = MyFakeModelWithChoices
            fields = ("cool_name", "status")

    class Query(graphene.ObjectType):
        lookup = graphene.Field(ModelType)

        def resolve_lookup(self, info):
            return SimpleLazyObject(
                lambda: MyFakeModelWithChoices(id=1, cool_name="awesome", status="ok")
            )

    class CreateMutation(SerializerMutation):
        class Meta:
            serializer_class = ChoicesModelSerializer

    class AllMutations(graphene.ObjectType):
        create = CreateMutation.Field()

    schema = graphene.Schema(query=Query, mutation=AllMutations)
