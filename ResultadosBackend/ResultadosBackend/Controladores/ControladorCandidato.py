from Modelos.Partido import Partido
from Modelos.Candidato import Candidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todos los Candidato")
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        print("Crear un Candidato")
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        print("Mostrar el candidato con id ", id)
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        print("Actualizando el candidato con id ", id)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        print("Elimiando el candidato con id ", id)
        return self.repositorioCandidato.delete(id)

    """
    Relación candidato y partido
    """
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)