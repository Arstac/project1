import termcolor

from logic import *

senyorita_escarlata = Symbol("SrEscarlata")
coronel_mostaza = Symbol("CorMostaza")
senyora_blanco = Symbol("SraBlanco")
reverendo_verde = Symbol("RevVerde")
senyora_pavoreal = Symbol("SraPavoreal")
profesor_ciruela = Symbol("PfrCiruela")
characters = [senyorita_escarlata, coronel_mostaza, senyora_blanco, reverendo_verde, senyora_pavoreal, profesor_ciruela]

cocina = Symbol("cocina")
comedor = Symbol("comedor")
salon_baile = Symbol("salon_baile")
escaleras = Symbol("escaleras")
pasillo = Symbol("pasillo")
terraza = Symbol("terraza")
sala_billar = Symbol("sala_billar")
biblioteca = Symbol("biblio")
estudio = Symbol("estudio")
sala = Symbol("sala")
rooms = [cocina, comedor, salon_baile, escaleras, pasillo, terraza, sala_billar, biblioteca, estudio, sala]

cuchillo = Symbol("knife")
pistola = Symbol("revolver")
candelabro = Symbol("candelabro")
tuberia = Symbol("tuberia")
herramienta = Symbol("herramienta")
cuerda = Symbol("cuerda")
weapons = [cuchillo, pistola, candelabro, tuberia, herramienta, cuerda]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(senyorita_escarlata, coronel_mostaza, senyora_blanco, reverendo_verde, senyora_pavoreal, profesor_ciruela),
    Or(cocina, comedor, salon_baile, escaleras, pasillo, terraza, sala_billar, biblioteca, estudio, sala),
    Or(cuchillo, pistola, candelabro, tuberia, herramienta, cuerda)
)

# Initial cards
knowledge.add(And(
    #Not(mustard), Not(kitchen), Not(revolver)
))

# Unknown card
knowledge.add(Or(
    #Not(scarlet), Not(library), Not(wrench)
))

# Known cards
#knowledge.add(Not(plum))
#knowledge.add(Not(ballroom))

check_knowledge(knowledge)
