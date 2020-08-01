from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    And(Or(Not(AKnight),Not(AKnave)),Or(AKnave,AKnight)),
    Or(Or(Not(AKnave),Not(AKnight)),Or(AKnave,AKnight)),
    Or(AKnave,Not(AKnight))
    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(Not(AKnight),Not(BKnight)),Or(BKnight,AKnight)),
    And(Or(Not(AKnave),Not(BKnave)),Or(BKnave,AKnave)),
    And(Or(Not(AKnight),Not(AKnave)),Or(AKnave,AKnight)),
    And(Or(Not(BKnight),Not(BKnave)),Or(BKnave,BKnight)),
    Or(Not(BKnave),AKnave)
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(Not(AKnight),Not(BKnight)),Or(BKnight,AKnight)),
    And(Or(Not(AKnave),Not(BKnave)),Or(BKnave,AKnave)),
    And(Or(Not(AKnight),Not(AKnave)),Or(AKnave,AKnight)),
    And(Or(Not(BKnight),Not(BKnave)),Or(BKnave,BKnight)),
    Implication(Or(And(AKnave,BKnave),And(AKnight,BKnight)),AKnave),
    Implication(And(Or(AKnave,BKnave),Or(AKnight,BKnight)),BKnight)
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(Not(AKnight),Not(BKnight)),Or(BKnight,AKnight)),
    And(Or(Not(AKnave),Not(BKnave)),Or(BKnave,AKnave)),
    And(Or(Not(AKnight),Not(AKnave)),Or(AKnave,AKnight)),
    And(Or(Not(BKnight),Not(BKnave)),Or(BKnave,BKnight)),
    And(Or(Not(CKnight),Not(CKnave)),Or(CKnave,CKnight)),
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
