from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorMesa():
    def __init__(self):
        print("Creando Controlador mesa")
        self.repostorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todos las mesas")
        return self.repostorioMesa.findAll()

    def create(self, infoMesa):
        print("Crear una mesa")
        laMesa = Mesa(infoMesa)
        return self.repostorioMesa.save(laMesa)

    def show(self, id):
        print("Mostrar la mesa con id ", id)
        laMesa = Mesa(self.repostorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        print("Actualizando la mesa con id ", id)
        laMesa = Mesa(self.repostorioMesa.findById(id))
        laMesa.numero = infoMesa["numero"]
        laMesa.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repostorioMesa.save(laMesa)

    def delete(self, id):
        print("Elimiando la mesa con id ", id)
        return self.repostorioMesa.delete(id)