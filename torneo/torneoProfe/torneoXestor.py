from equipo import Equipo
from torneo import Torneo


class TorneoXestor:

    def __init__(self, nomeTorneo, numEquipos, listaNomeEquipos):
        self.torneo = Torneo(nomeTorneo, numEquipos)
        for nomeEquipo in listaNomeEquipos:
            self.torneo.add_equipo(Equipo(nomeEquipo))

    def buclePrincipal(self):
        opcion = 0
        while (opcion != 5):
            self.mostrar_menu()
            opcion = int (input ("Elixe unha opción"))
            match (opcion):
                case 1:
                    encontro_resultado = input ("Escribe o resultado do encontro (Equipo1-Equipo2 n1-n2)")
                    self.torneo.rexistrar_encontro(encontro_resultado)
                case 2:
                    equiposOrdeados = self.torneo.get_clasificacion()
                    for i, equipo in enumerate(equiposOrdeados):
                        print (f"{i+1}º clasificado: {equipo.nome}, {equipo.get_puntos()} puntos")
                case 3:
                    nome_equipo = input ("Escribe o nome do equipo")
                    for equipo in self.torneo.get_equipos():
                        if equipo.nome == nome_equipo:
                            print (equipo)
                            break
                case 4:
                    print ("Os equipos participantes son: " + str(len(self.torneo.get_equipos())))
                    for equipo in self.torneo.get_equipos():
                        print (f"O número de partidos de {equipo.nome} é {equipo.get_encontros_xogados()}")


    def mostrar_menu(self):
        print ("1. Rexistrar resultado")
        print ("2. Mostrar cl2asificación")
        print ("3. Consultar equipo")
        print ("4. Estatísticas do torneo")
        print ("5. Saír")


if __name__ == "__main__":
    t = TorneoXestor ("Campionato Castelao", 4, ['Dam1','Dam2', 'Asir', 'Smr'])
    t.buclePrincipal()
