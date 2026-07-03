import re

def validate_email(email: str) -> bool:
    """Valida formato de correo electrónico."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Valida formato de teléfono (acepta código de área)."""
    pattern = r"^\+?[0-9\s\-]{8,15}$"
    return bool(re.match(pattern, phone))
