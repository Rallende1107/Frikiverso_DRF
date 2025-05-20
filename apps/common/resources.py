from core.resources import BaseFullResource
from .models import Country, Format, ImageSize, Language, Person, PersonImage, PersonImageExtra, PersonNickname, Quality, Website
# Register your models here.
########################################################################################################    Resource para Country
class CountryResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Country

########################################################################################################    Resource para Format
class FormatResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Format

########################################################################################################    Resource para ImageSize
class ImageSizeResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = ImageSize

########################################################################################################    Resource para Language
class LanguageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Language

########################################################################################################    Resource para Person
class PersonResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Person

########################################################################################################    Resource para PersonImage
class PersonImageResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = PersonImage

########################################################################################################    Resource para PersonImageExtra
class PersonImageExtraResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = PersonImageExtra

########################################################################################################    Resource para PersonNickname
class PersonNicknameResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = PersonNickname

########################################################################################################    Resource para Quality
class QualityResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Quality

########################################################################################################    Resource para Website
class WebsiteResource(BaseFullResource):
    class Meta(BaseFullResource.Meta):
        model = Website