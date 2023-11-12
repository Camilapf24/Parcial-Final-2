def registrar_compra(cliente, varita):
  with open('registro_varita.txt', 'a') as archivo:
    archivo.write(f'{cliente} compro la varita de {varita}\n')
    
def main():
  while True:
    nombre_cliente = input("Ingrese el nombre del cliente(o 'salir'para terminar):")
    if nombre_cliente =='salir':
      break
      
    print("Opciones de varitas:")
    print("1. varita de saúco")
    print("2. varita de espino")
    print("3. varita de sauce")
    print("4. varita de acebo")
    
opcion_varita = input("Ingrese el numero de la varita que el cliente compro:")
opciones = {
  '1': 'Sueco',
  '2': 'Espino',
  '3':'Sauce',
  '4':'Acebo',
}
if opcion_varita in opciones:
  varita_elegida = opciones[opcion_varita]
  registrar_compra (nombre_cliente, varita_seleccionada)
  print(f"registro completado para {nombre_cliente} y la varita de {varita_elegida}.")
  
else:
  print("Opcion incorrecta. Por favor ingresa un numero valido (1,2,3 o 4).")
  if __name__ == '__main__':
  main()
  
