from typing import Tuple, List, Dict

from django.db import models
from rest_framework import serializers
from electronics_network.models import Node, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model: models.Model = Contact
        fields: List[str] = ["email", "country", "city", "street", "house_number"]


class NodeCreateSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(required=False, queryset=Node.objects.all(), slug_field="name")
    contact = ContactSerializer(required=False)

    class Meta:
        model: models.Model = Node
        read_only_fields: Tuple[str, ...] = ("id", "debt_to_the_supplier", "date_of_creation")
        fields: str = "__all__"

    def is_valid(self, *, raise_exception=False):
        self._contact: Dict[str, str] = self.initial_data.pop("contact", {})
        self.initial_data["level"] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data: dict) -> Node:
        node: Node = Node.objects.create(**validated_data)
        node.save()

        contact: Contact = Contact.objects.create(
            member=node,
            email=self._contact.get("email", None),
            country=self._contact.get("country", None),
            city=self._contact.get("city", None),
            street=self._contact.get("street", None),
            house_number=self._contact.get("house_number", None)
        )
        contact.save()

        return node


class NodeListSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(queryset=Node.objects.all(), slug_field="name")
    contact = ContactSerializer()

    class Meta:
        model: models.Model = Node
        fields: List[str] = ["id", "name", "level", "supplier", "debt_to_the_supplier", "contact"]


class NodeSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(required=False, queryset=Node.objects.all(), slug_field="name")
    contact = ContactSerializer(required=False)

    class Meta:

        model: models.Model = Node
        fields: str = "__all__"
        read_only_fields: Tuple[str, ...] = ("id", "debt_to_the_supplier", "date_of_creation", "level")

    def is_valid(self, *, raise_exception=False):
        self._contact = self.initial_data.pop("contact", {})
        if "supplier" in self.initial_data:
            self.initial_data["level"] = level_detection(self.initial_data)
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        super().save()

        if self._contact != {}:
            self.instance.contact = self.update(self.instance.contact, self._contact)

        return self.instance


def level_detection(kwargs: dict) -> int:
    level: int = 0
    if kwargs.get("supplier") is None:
        return level

    supplier: Node = Node.objects.get(name=kwargs["supplier"])

    for i in range(2):
        level += 1
        if supplier.supplier is None:
            return level
        supplier = supplier.supplier

    raise Exception("Incorrect links in the hierarchical system")
