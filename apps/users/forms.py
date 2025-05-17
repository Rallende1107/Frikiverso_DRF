from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
import datetime


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name',  'email',
            'phone', 'birth_date', 'password1', 'password2', 'acepto_terminos'
            )

    username = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuario',
                'id': 'username',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres. Únicamente letras, dígitos y @ . + - _',
        error_messages={
            'required': 'Debe ingresar su nombre.',
            'min_length': 'El Username no cumple con el largo mínimo.',
            'max_length': 'El Username excede lo permitido.',
        }
    )

    first_name = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=3,
        max_length=50,
        label='Nombres',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombres',
                'id': 'first_name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 3 caracter, máximo 50 caracteres.',
        error_messages={
            'required': 'Debe ingresar su nombre.',
            'min_length': 'El Nombre no cumple con el largo mínimo.',
            'max_length': 'El Nombre excede lo permitido.',
        }
    )

    last_name = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=3,
        max_length=50,
        label='Apellidos',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos',
                'id': 'last_name',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 3 caracter, máximo 50 caracteres',
        error_messages={
            'required': 'Debe ingresar su apellido.',
            'min_length': 'El Apellido no cumple con el largo mínimo.',
            'max_length': 'El Apellido excede lo permitido.',
        }
    )

    email = forms.EmailField(
        required=True,
        disabled=False,
        min_length=10,
        max_length=50,
        label='Correo Electrónico',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'id': 'email',
                'type': 'email',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Ejemplo Correo@Correo.correo',
        error_messages={
            'required': 'Debe ingresar su correo electrónico.',
            'min_length': 'El Email no cumple con el largo mínimo.',
            'max_length': 'El Email excede lo permitido.',
        }
    )

    phone = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=8,
        max_length=20,
        label='Teléfono',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'id': 'phone',
                'type': 'number',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Solo números',
        error_messages={
            'required': 'Debe ingresar su número de teléfono.',
            'min_length': 'El número de teléfono no cumple con el largo mínimo.',
            'max_length': 'El número de teléfono excede lo permitido.',
        }
    )

    birth_date = forms.DateField(
        required=True,
        disabled=False,
        label='Fecha de Nacimiento',
        widget=forms.DateInput(
        format='%Y-%m-%d',  # Formato visual para el usuario
            attrs={
                'class': 'form-control',
                'placeholder': 'Fecha de Nacimiento',
                'id': 'birth_date',
                'type': 'date',
                'autocomplete': 'off'
            }),
        help_text='Formato: DD-MM-YYYY',
        error_messages={
            'required': 'Debe ingresar su fecha de nacimiento.'
        }
    )

    password1 = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'id': 'password1',
                'type': 'password',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres.',
        error_messages={
            'required': 'Debe ingresar una contraseña.',
            'min_length': 'Su contraseña no cumple con el largo mínimo.',
            'max_length': 'Su contraseña excede lo permitido.',
        }
    )

    password2 = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirma Contraseña',
                'id': 'password2',
                'type': 'password',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres.',
        error_messages={
            'required': 'Debe confirmar la contraseña.',
            'min_length': 'La confirmación de su contraseña no cumple con el largo mínimo.',
            'max_length': 'La confirmación de su contraseña excede lo permitido.',
        }
    )

    acepto_terminos = forms.BooleanField(
        required=True,
        disabled=False,
        initial=False,
        label='Acepto los Términos y Condiciones',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'placeholder': 'Acepto los Términos y Condiciones',
                'id': 'acepto_terminos',
                'type': 'checkbox',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        error_messages={
            'required': 'Debe aceptar los términos y condiciones.',
        }
    )

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date > datetime.date.today():
            raise forms.ValidationError(
                'La fecha de nacimiento no puede ser mayor que la fecha actual.')
        return birth_date

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Este correo electrónico ya está registrado.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class SuperUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1']

    username = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuario',
                'id': 'username',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres. Únicamente letras, dígitos y @ . + - _',
        error_messages={
            'required': 'Debe ingresar su nombre.',
            'min_length': 'El Username no cumple con el largo mínimo.',
            'max_length': 'El Username excede lo permitido.',
        }
    )

    password1 = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'id': 'password1',
                'type': 'password',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres.',
        error_messages={
            'required': 'Debe ingresar una contraseña.',
            'min_length': 'Su contraseña no cumple con el largo mínimo.',
            'max_length': 'Su contraseña excede lo permitido.',
        }
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user

class StaffUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1']

    username = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuario',
                'id': 'username',
                'type': 'text',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres. Únicamente letras, dígitos y @ . + - _',
        error_messages={
            'required': 'Debe ingresar su nombre.',
            'min_length': 'El Username no cumple con el largo mínimo.',
            'max_length': 'El Username excede lo permitido.',
        }
    )

    password1 = forms.CharField(
        required=True,
        strip=True,
        disabled=False,
        min_length=4,
        max_length=35,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña',
                'id': 'password1',
                'type': 'password',
                'required': 'required',
                'autocomplete': 'off',
            }
        ),
        help_text='Mínimo 4 caracter, máximo 35 caracteres.',
        error_messages={
            'required': 'Debe ingresar una contraseña.',
            'min_length': 'Su contraseña no cumple con el largo mínimo.',
            'max_length': 'Su contraseña excede lo permitido.',
        }
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_staff = True
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'email', 'phone',
            'birth_date', 'avatar', 'address'
        )

    first_name = forms.CharField(
        required=True, strip=True, disabled=False, min_length=3, max_length=50, label='Nombres',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Nombres', 'id': 'first_name',
            'type': 'text', 'required': 'required', 'autocomplete': 'off'
        }),
        help_text='Mínimo 3 caracteres, máximo 50 caracteres.',
        error_messages={
            'required': 'Debe ingresar su nombre.', 'min_length': 'El Nombre no cumple con el largo mínimo.',
            'max_length': 'El Nombre excede lo permitido.'
        }
    )

    last_name = forms.CharField(
        required=True, strip=True, disabled=False, min_length=3, max_length=50, label='Apellidos',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Apellidos', 'id': 'last_name',
            'type': 'text', 'required': 'required', 'autocomplete': 'off'
        }),
        help_text='Mínimo 3 caracteres, máximo 50 caracteres',
        error_messages={
            'required': 'Debe ingresar su apellido.', 'min_length': 'El Apellido no cumple con el largo mínimo.',
            'max_length': 'El Apellido excede lo permitido.'
        }
    )

    email = forms.EmailField(
        required=True, disabled=False, min_length=10, max_length=50, label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Correo electrónico', 'id': 'email',
            'type': 'email', 'required': 'required', 'autocomplete': 'off'
        }),
        help_text='Ejemplo Correo@Correo.correo',
        error_messages={
            'required': 'Debe ingresar su correo electrónico.', 'min_length': 'El Email no cumple con el largo mínimo.',
            'max_length': 'El Email excede lo permitido.'
        }
    )

    phone = forms.CharField(
        required=True, strip=True, disabled=False, min_length=8, max_length=20, label='Teléfono',
        widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': 'Teléfono', 'id': 'phone',
            'type': 'number', 'required': 'required', 'autocomplete': 'off'
        }),
        help_text='Solo números',
        error_messages={
            'required': 'Debe ingresar su número de teléfono.', 'min_length': 'El número de teléfono no cumple con el largo mínimo.',
            'max_length': 'El número de teléfono excede lo permitido.'
        }
    )

    birth_date = forms.DateField(
        required=False, disabled=False, label='Fecha de Nacimiento',
        # input_formats=['%d-%m-%Y', '%Y-%m-%d'],  # Formatos aceptados
        widget=forms.DateInput(
        format='%Y-%m-%d',  # Formato visual para el usuario
            attrs={
                'class': 'form-control',
                'placeholder': 'Fecha de Nacimiento',
                'id': 'birth_date',
                'type': 'date',
                'autocomplete': 'off'
            }),
        help_text='Formato: DD-MM-YYYY',
        error_messages={
            'required': 'Debe ingresar su fecha de nacimiento.'
        }
    )

    avatar = forms.ImageField(
        required=False, label='Avatar',
        widget=forms.FileInput(attrs={
            'class': 'form-control', 'placeholder': 'Avatar', 'id': 'avatar'
        })
    )

    address = forms.CharField(
        required=False, strip=True, disabled=False, max_length=250, label='Dirección',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Dirección', 'id': 'address',
            'type': 'text'
        }),
        help_text='Máximo 250 caracteres.',
        error_messages={
            'max_length': 'La Dirección excede lo permitido.'
        }
    )

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date and birth_date > datetime.date.today():
            raise forms.ValidationError(
                'La fecha de nacimiento no puede ser mayor que la fecha actual.')
        return birth_date

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_user = self.instance  # Obtiene la instancia actual del usuario

        if CustomUser.objects.filter(email=email).exclude(pk=current_user.pk).exists():
            raise forms.ValidationError(
                'Este correo electrónico ya está en uso por otro usuario.')

        return email


