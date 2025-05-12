from import_export import resources
from .models import CustomUser

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'birth_year', 'avatar', 'slug', 'created_at', 'updated_at')
        export_order = ('id', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'birth_year', 'avatar', 'slug', 'created_at', 'updated_at')
