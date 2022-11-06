from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Modelos.Resultado import Resultado
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorResultado():
    def __init__(self):
        print("Creando ControladorResultado")
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todos los resultados")
        return self.repositorioResultado.findAll()

    """
        Asignacion mesa y candidato a Resultado
    """
    def create(self, infoResultado, id_mesa, id_candidato):
        print("crear un resultado")
        nuevoResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato = elCandidato
        return self.repositorioResultado.save(nuevoResultado)

    def show(self, id):
        print("mostrando un resultado:", id)
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    """
        Modificar Resultado (candidato y mesa)
    """
    def update(self, id, infoResultado, id_candidato, id_mesa):
        print("Actualizando resultado: ", id)
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_mesas = infoResultado["numero_mesas"]
        resultadoActual.cedula_candidato = infoResultado["cedula_candidato"]
        resultadoActual.numero_votos = infoResultado["numero_resultado"]
        laMesa =Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultadoActual.mesa = laMesa
        resultadoActual.candidato = elCandidato
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        print("Eliminando Resultado: ", id)
        return self.repositorioResultado.delete(id)

    "Obtener todos los resultados de un candidato"

    def listarResultadosDeCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoResultadosDeCandidato(id_candidato)
