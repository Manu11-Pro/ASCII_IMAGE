from .utils import path_of_file_to_upload ,output

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

with open(path_of_file_to_upload, "rb") as i:
    i.seek(18)
    width = int.from_bytes(i.read(4), "little")
    height = int.from_bytes(i.read(4), "little")
    padding = (4 -(width * 3 % 4))% 4

    print(width, height, padding)

    i.seek(54)

    every_rows = []

    for h in range(height):
        string_row = ""

        for w in range(width):
            pixel_data = i.read(3)

            B = pixel_data[0]
            G = pixel_data[1]
            R = pixel_data[2]

            val = ((0.299 * R) + (0.587 * G) + (0.114 * B))
            string_row += char_to_use(val)

        i.read(padding)
        every_rows.append(string_row)

with open(output, "w") as j:
    for row in reversed (every_rows):
        j.write(row + "\n")