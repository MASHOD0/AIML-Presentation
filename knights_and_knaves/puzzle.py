from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
 

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

general_knowledge = And(
    # general rules for solving the puzzle
    # each person is either a knight or a knave
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # no person can be both Knight and a knave
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
)
 

knowledge0 = And(
    general_knowledge,

    # The statement given 
    Implication(AKnight, And(AKnight, AKnave))
)


knowledge1 = And(
    general_knowledge,
    # The statement given
    Biconditional(AKnight, And(AKnave, BKnave))
)


knowledge2 = And(
    general_knowledge,
    # the given statements
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))
    
)


knowledge3 = And(
    general_knowledge,
    
    # the given statements
    Biconditional(AKnight, Biconditional(AKnight, Not(AKnave))),
    Biconditional(BKnight, And(Implication(AKnave, BKnight), CKnave)),
    Biconditional(CKnight, AKnight)
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
