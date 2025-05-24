from import_export import resources
from .models import Company, Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website,  ContextApp, Genre, Rating, Status, Type
# Register your models here.

########################################################################################################    Resource para Company
class CompanyResource(resources.ModelResource):
    class Meta():
        model = Company

########################################################################################################    Resource para Country
class CountryResource(resources.ModelResource):
    class Meta():
        model = Country

########################################################################################################    Resource para Format
class FormatResource(resources.ModelResource):
    class Meta():
        model = Format

########################################################################################################    Resource para ImageSize
class ImageSizeResource(resources.ModelResource):
    class Meta():
        model = ImageSize

########################################################################################################    Resource para Language
class LanguageResource(resources.ModelResource):
    class Meta():
        model = Language

########################################################################################################    Resource para Person
class PersonResource(resources.ModelResource):
    class Meta():
        model = Person

########################################################################################################    Resource para PersonImage
class PersonImageResource(resources.ModelResource):
    class Meta():
        model = PersonImage

########################################################################################################    Resource para PersonImageExtra
class PersonImageExtraResource(resources.ModelResource):
    class Meta():
        model = PersonImageExtra

########################################################################################################    Resource para PersonNickname
class PersonNicknameResource(resources.ModelResource):
    class Meta():
        model = PersonNickname

########################################################################################################    Resource para Quality
class QualityResource(resources.ModelResource):
    class Meta():
        model = Quality

########################################################################################################    Resource para Website
class WebsiteResource(resources.ModelResource):
    class Meta():
        model = Website

########################################################################################################    Resource para ContextApp
class ContextAppResource(resources.ModelResource):
    class Meta():
        model = ContextApp

########################################################################################################    Resource para Genre
class GenreResource(resources.ModelResource):
    class Meta():
        model = Genre

class RatingResource(resources.ModelResource):
    class Meta():
        model = Rating

class StatusResource(resources.ModelResource):
    class Meta():
        model = Status

class TypeResource(resources.ModelResource):
    class Meta():
        model = Type

