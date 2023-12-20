from rest_framework import serializers

from electronics_network.models import Node, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class NodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = Node
        fields = ("id", "name", "level", "supplier", "debt_to_the_supplier", "contact",)
        read_only_fields = ("id", "debt_to_the_supplier", "date_of_creation",)
