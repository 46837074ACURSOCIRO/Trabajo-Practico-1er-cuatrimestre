class Biblioteca:
    def __init__ (self):
        self.Miembros=[]
        self.Libros=[]
    def agregarMiembro(self, nombre, dni):
        miembro = Miembros(nombre, dni)
        self.Miembros.append(miembro)
    def prestarlibro (self, dni,isbn):
        # recorrer lista libros hasta que q coincida con el isbn
        for l in self.Libros:
            if l.ISBN == isbn:
                if l.estaDisponible():
                    l.prestarLibros()
                    l.regitrarLibroPrestado(l.Isbn)

class Libros:
    def __init__ (self,titulo, autor , ISBN):
        self.titulo =titulo
        self.autor =autor
        self.estadoprestado = False
        self.ISBN =ISBN

class Miembros:
    def __init__ (self,nombre , dni):
        self.nombre =nombre
        self.dni =dni
        self.librosPrestados=[]


def main ():
    biblioteca= Biblioteca()
    while True:

        print("0- Salir")
        print("1- Agregar Miembro")
        print("2- Agregar Libro")
        print("3- Prestar Libro")
        print("4- Devolver Libro")
        print("5- Consultar Estado del Libro")
        print("6- Consultar estado de miembro")  

        opcion = input("Ingrese una opcion")


        if opcion == "1":
            nombre = input("Ingrese el nombre del miembro: ")
            dni = input("Ingrese el dni del miembro: ")
            biblioteca.agregarMiembro(nombre, dni)
            
        elif opcion =="3":
            dni = input("Ingrese el dni del miembro: ")
            isbn= input("Ingrese el isbn del libro: ")
            biblioteca.prestarlibro(dni,isbn)