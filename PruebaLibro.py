from Libro import Libro

libro1 = Libro()
libro1.nombre = "Sombras"
libro1.paginas = 200
libro1.setColor("Rojo")
libro2 = Libro("Sin teclado", 100, "Verde")

print(libro1.__str__())
print(libro2.__str__())