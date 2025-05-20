from import_export import resources

# Register your models here.
class BaseFullResource(resources.ModelResource):
    class Meta:
        abstract = True
        fields = '__all__'
