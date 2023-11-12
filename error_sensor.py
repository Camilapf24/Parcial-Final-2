def mai():
  lecturas_correctas = []
  lecturas_fuera_rango = 0
  
while True:
  lectura = input ("Ingresa lectura del sensor (0 'fin´para terminar):")
  if lectura.lower() == 'fin':
    break
    
  try:
    valor_temperatura = float(lectura)
    if 10<= valor_temperatura <= 40:
      lecturas_corrctas.append(valor_temperatura)
    else:
      lecturas_fuera_rango += 1
      print(f"Lectura incorrecta fuera de rango: {valor_temperatura}")
      
  except ValueError:
    print("Entrads no válida.Ingresa un valor numérico.")
    
porcentaje_error = (lecturas_fuera_rango / len(lecturas_correctas + lecturas_fuera_rango)) * 100
print(f"Porcentaje de lecturas fuera de rango. {porcentaje_error:.2f}%")

if __name__ == "__main__":
 main()
