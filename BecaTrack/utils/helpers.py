import datetime

def format_date(date_obj: datetime.date) -> str:
    """Formatea objetos fecha a un formato legible por el usuario."""
    if not date_obj:
        return "N/A"
    return date_obj.strftime("%d/%m/%Y")
