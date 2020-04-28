import cartas

b = cartas.crea_baraja()

print(cartas.invertir(b))

manos = cartas.repartir(b, 3, 5)

cartas.mezclar(b)

print(manos)
