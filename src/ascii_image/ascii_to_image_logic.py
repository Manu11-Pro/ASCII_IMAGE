from utils import file_to_upload

def char_to_use(val):
    if val > 230:
        return " "
    elif val > 200:
        return "."
    elif val > 180:
        return ":"
    elif val > 160:
        return "-"
    elif val > 140:
        return "="
    elif val > 120:
        return "+"
    elif val > 100:
        return "*"
    elif val > 80:
        return "#"
    elif val > 60:
        return "%"
    elif val > 40:
        return "@"
    else:
        return "$"