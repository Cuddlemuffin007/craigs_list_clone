from rest_framework import serializers
from pkmn_app.models import Category, SubCategory, Pokemon


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory


class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
