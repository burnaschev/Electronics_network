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

    def to_representation(self, instance):
        level = 0
        current_node = instance
        while current_node.supplier:
            level += 1
            current_node = current_node.supplier

        representation = super().to_representation(instance)
        representation['level'] = level
        return representation
