# Django imports
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _

# Local app imports - models and forms
from apps.common.models import (
    Country, Format, ImageSize, Language, Person, PersonImage,
    PersonImageExtra, PersonNickname, Quality, Website
)
from apps.common.forms import (
    CountryForm, FormatForm, ImageSizeForm, LanguageForm, PersonForm, PersonImageForm,
    PersonImageExtraForm, PersonNicknameForm, QualityForm, WebsiteForm
)

# Project-level imports - mixins and utilities
from core.utils.mixins import PermissionRequiredMessageMixin
from core.utils.constants import Templates, URLS, CSSBackground, JSConstants, ImageCards, KeyMap
from core.utils.utils import delete_previous_media