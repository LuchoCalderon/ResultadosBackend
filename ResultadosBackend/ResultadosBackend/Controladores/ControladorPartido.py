from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorPartido():
    def __init__(self):
        print("creando controlador partido")
        self.repositorioPartido = RepositorioPartido()


    def index(self):
        print("listar todos los partidos")
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        print("crear un partido")
        nuevoPartido= Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        print("mostrando un partido con codigo id:", id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        print("actualizando un partido con id:", id)
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        print("elimininando un partido con id:", id)
        return self.repositorioPartido.delete(id)