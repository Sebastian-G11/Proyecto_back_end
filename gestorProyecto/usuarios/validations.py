
def validate_nombre(nombre):
    if not nombre.isalpha():
        raise ValueError("El nombre debe contener solo letras.")
    if len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")

def validate_apellido(apellido):
    if not apellido.isalpha():
        raise ValueError("El apellido debe contener solo letras.")
    if len(apellido) < 3:
        raise ValueError("El apellido debe tener al menos 3 caracteres.")

def validate_email(email):
    if '@' not in email:
        raise ValueError("El correo electrónico no es válido.")

def validate_rol(rol):
    valid_roles = ['Usuario', 'Administrador']
    if rol not in valid_roles:
        raise ValueError(f"El rol debe ser uno de los siguientes: {', '.join(valid_roles)}")
