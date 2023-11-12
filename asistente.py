def detectar_Alexa(Texto):
  palabras = texto.split()
  vaces_Alexa = palabras.count('Camila')
  
  if veces_Alexa > 1:
    return "Tranquilo, solo di mi nombre una vez"
elif veces_Alexa == 1:
  return "¡Hola! En que puedo ayudarte?"
else:
  return "No mencionaste mi nombre"

texto_ingresado = input("Ingresa tu texto:")
resultado = detectar_Alexa(texto_ingresado)
print(resultado)
