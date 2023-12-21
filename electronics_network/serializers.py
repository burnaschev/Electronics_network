from rest_framework import serializers

from electronics_network.models import Node, Contact, Levels, Product


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(required=False)
    product = ProductSerializer(many=True, read_only=True, source='owners')

    class Meta:
        model = Node
        fields = ("id", "name", "level", "supplier", "debt_to_the_supplier", "contact", "product",)
        read_only_fields = ("debt_to_the_supplier", "created_at",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        level = 0
        current_node = instance
        while current_node.supplier:
            level += 1
            current_node = current_node.supplier

        level_mapping = {
            0: Levels.FACTORY,
            1: Levels.RETAIL_NETWORK,
            2: Levels.IP,
        }

        representation['level'] = level_mapping.get(level, Levels.FACTORY)

        return representation
