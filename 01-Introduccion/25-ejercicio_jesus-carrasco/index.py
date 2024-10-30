import base64

# Tu cadena codificada en Base64
encoded_text = "RWwgdGV4dG8gcXVlIGRlYmVzIHN1YmlyIGEgQ2xhc3NSb29tIGVzOiAiKioqIEtldmluIE1pdG5pY2sgLSBIYWNrZXIgKioqIg"

# Agregar relleno si es necesario
while len(encoded_text) % 4 != 0:
    encoded_text += '='

# Decodificación
decoded_text = base64.b64decode(encoded_text).decode('utf-8')
print(decoded_text)
