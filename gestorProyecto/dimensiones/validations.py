def validate_nombre(nombre):
    if len(nombre) < 3:
        raise ValueError("El nombre debe tener al menos 3 caracteres.")
