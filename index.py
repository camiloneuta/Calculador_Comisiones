print("================================================")
print("CALCULADOR DE COMISIONES - CARNICERÍA HUILENSE")
print("================================================")
print("")

nom_vendedor = input(">> Ingrese el nombre del vendedor: ")
cant_ventas = float((input(">> Ingrese la cantidad de ventas: ")))

comisiones = round(cant_ventas * 0.13)

print("")
print("================================================")
print("")
print(f"Desde la CARNICERÍA HUILENSE, {nom_vendedor} ,te queremos felicitar"
      f"\nEres el vendedor #1 de esta semana, vendiste {cant_ventas} de nuestros productos"
      f"\nY tus comisiones son de {comisiones} esta semana."
      f"\nSigue así y podrás alcanzar tus metas en nuestra empresa!.")
print("")
print("================================================")
