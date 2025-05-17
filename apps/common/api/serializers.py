from rest_framework import serializers
from apps.common.models import (Language, Website, Format, ImageSize, Quality, Country, Person, PersonNickname, PersonImage, PersonImageExtra)

########################################################################################################    Serializer Language
class LanguageSerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = Language
        fields = [
            'id',
            'name',
            'name_esp',
            'acronym',
            'initial',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'acronym',
            'initial',
            'slug',
            'created_at',
            'updated_at'
            ]

class LanguageListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = Language
        fields = [
            'id',
            'name',
            'name_esp',
            'initial',
            'acronym',
            'slug',
            'is_active',
        ]
        # Campos que no deben ser editados por el cliente
        read_only_fields = [
            'id',
            'initial',
            'slug',
            'created_at',
            'updated_at',
        ]

########################################################################################################    Serializer Website
class WebsiteSerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = Website
        fields = [
            'id',
            'name',
            'acronym',
            'url',
            'initial',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'initial',
            'slug',
            'created_at',
            'updated_at'
            ]

class WebsiteListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = Website
        fields = [
            'id',
            'name',
            'acronym',
            'initial',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at'
            ]

########################################################################################################    Serializer Format
class FormatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Format
        fields = [
            'id',
            'name',
            'for_video',
            'for_music',
            'for_image',
            'for_document',
            'for_other',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at'
            ]

class FormatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Format
        fields = [
            'id',
            'name',
            'for_video',
            'for_music',
            'for_image',
            'for_document',
            'for_other',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at'
            ]

########################################################################################################    Serializer ImageSize
class ImageSizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageSize
        fields = [
            'id',
            'name',
            'name_esp',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'slug',
            ]

class ImageSizeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageSize
        fields = [
            'id',
            'name',
            'name_esp',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'slug',
            ]

########################################################################################################    Serializer Quality
class QualitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Quality
        fields = [
            'id',
            'name',
            'description',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at'
            ]

class QualityListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = Quality
        fields = [
            'id',
            'name',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'slug',
            'created_at',
            'updated_at'
            ]

########################################################################################################    Serializer Country
class CountrySerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'initial',
            'name_esp',
            'initial_esp',
            'slug',
            'code',
            'numeric_code',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'initial',
            'initial_esp',
            'slug',
            'code',
            'numeric_code',
            'created_at',
            'updated_at'
            ]

class CountryListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = Country
        fields = [
            'id',
            'name',
            'name_esp',
            'initial',
            'initial_esp',
            'slug',
            'is_active',
        ]
        # Campos que no deben ser editados por el cliente
        read_only_fields = [
            'id',
            'initial',
            'initial_esp',
            'slug',
            'code',
            'numeric_code',
            'created_at',
            'updated_at',
        ]

########################################################################################################    Serializer Person
class PersonSerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = Person
        fields = [
            'id',
            'full_name',
            'initial',
            'biography',
            'birth_date',
            'country',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'initial',
            'slug',
            'created_at',
            'updated_at'
            ]

class PersonListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = Person
        fields = [
            'id',
            'initial',
            'full_name',
            'slug',
            'is_active',
        ]
        # Campos que no deben ser editados por el cliente
        read_only_fields = [
            'id',
            'initial',
            'slug',
            'created_at',
            'updated_at',
        ]

########################################################################################################    Serializer PersonNickname
class PersonNicknameSerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = PersonNickname
        fields = [
            'id',
            'person',
            'nickname',
            'initial',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'initial',
            'slug',
            'created_at',
            'updated_at'
            ]

class PersonNicknameListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = PersonNickname
        fields = [
            'id',
            'person',
            'nickname',
            'initial',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'initial',
            'slug',
            'created_at',
            'updated_at'
            ]

########################################################################################################    Serializer PersonImage
class PersonImageSerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = PersonImage
        fields = [
            'id',
            'person',
            'size_image',
            'image',
            'image_url',
            'name',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            ]

class PersonImageListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = PersonImage
        fields = [
            'id',
            'person',
            'image',
            'name',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            ]

########################################################################################################    Serializer PersonImageExtra
class PersonImageExtraSerializer(serializers.ModelSerializer):
    # Serializer para Detalle y Crear
    class Meta:
        model = PersonImageExtra
        fields = [
            'id',
            'person',
            'image',
            'name',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            ]

class PersonImageExtraListSerializer(serializers.ModelSerializer):
    # Serializer para Listado (solo campos esenciales)
    class Meta:
        model = PersonImageExtra
        fields = [
            'id',
            'person',
            'image',
            'name',
            'slug',
            'is_active',
        ]
        read_only_fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            ]

