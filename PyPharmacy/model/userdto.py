import sirope
import flask_login
import werkzeug.security as safe


class UserDto(flask_login.UserMixin):
    def __init__(self, username, password, nombre, apellidos):
        self._usenarme = username
        self._password = safe.generate_password_hash(password)
        self._nombre = nombre
        self._apellidos = apellidos

    def __getattr__(self, item):
        if item == "username" or item == "id":
            return self._usenarme
        elif item == "nombre":
            return self._nombre
        elif item == "apellidos":
            return self._apellidos
        elif item == "nombre_completo":
            return str.format("{} {}", self._nombre, self._apellidos)

        raise AttributeError(item)
    
    @property
    def id(self):
        return self._usenarme
    
    def chk_password(self, pswd):
        return safe.check_password_hash(self._password, pswd)

    @staticmethod
    def current_user():
        usr = flask_login.current_user
        if usr.is_anonymous:
            flask_login.logout_user()
            usr = None
        return usr

    @staticmethod
    def find(s: sirope.Sirope, username: str) -> "UserDto":
        return s.find_first(UserDto, lambda u: username == username)
    
   

