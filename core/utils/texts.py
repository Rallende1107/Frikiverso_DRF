from django.utils.translation import gettext_lazy as _

# Usuarios App
TITLE_USER_CREATE = _('Regístrate')
TITLE_USER_UPDATE = _('Editar Perfil')
TITLE_USER_LIST = _('Lista de usuarios')

TITLE_SUPER_USER_CREATE = _('Añadir super usuario')
TITLE_STAFF_USER_CREATE = _('Añadir usuario del equipo')

TITLE_LOGIN_PAGE = _('Iniciar Sesión')
MESSAGE_SUCCESS_REGISTRATION = _('¡Te has registrado exitosamente!')
MESSAGE_SUCCESS_USER_EDIT = _('¡Información actualizada exitosamente!')

MESSAGE_SUCCESS_LOGIN = _('¡Has iniciado sesión correctamente!')
MESSAGE_SUCCESS_LOGOUT = _('¡Has cerrado sesión correctamente!')
MESSAGE_ERROR_MESSAGE = _('Credenciales inválidas. Por favor, inténtalo de nuevo.')




# Mensajes Generales
ADD = _('Añadir')
HOME = _('Inicio')
NO_INFO = _('Sin Información')
ERROR_DELETE_IMG = _('Error al eliminar la imagen anterior')
WITHOUT_PERMISSION = _('¡No tienes los permisos para realizar esta acción!')


class Titles:
    class Common:
        home_title = _('General')

    class SectionsTitles:
            admin_title = _('Administración de Usuarios')


    class CardTitles:
        Users = _('Usuarios')

    class CardSubTitles:
        Users = _()




