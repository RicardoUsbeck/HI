
from lnn import Predicate, Variable, Implies, ForAll, Model, World, TRUE, And, Or, Join


def example():
    model = Model()

    born_in = Predicate('bornIn', arity=2)
    part_of = Predicate('partOf', arity=2)

    x = Variable('x', ctype='person')
    a = Variable('a', ctype='place')
    b = Variable('b', ctype='place')

    model["birthplaces_are_part_of"] = ForAll(x,
                                              a,
                                              b,
                                              Implies(
                                                  And(born_in(x, a), born_in(x, b), join=Join.OUTER),
                                                  Or(part_of(a, b), part_of(b, a), join=Join.OUTER),
                                                  join=Join.OUTER,
                                                  ),
                                              join=Join.OUTER,
                                              world=World.AXIOM)

    model["part_of_are_birthplaces"] = ForAll(x,
                                              a,
                                              b,
                                              Implies(
                                                  And(born_in(x, a), part_of(a, b), join=Join.OUTER),
                                                  born_in(x, b),
                                                  join=Join.OUTER),
                                              join=Join.OUTER,
                                              world=World.AXIOM)

    model.add_facts({
        born_in.name: {
            ('Albert', 'Ulm'): TRUE,
            ('Albert', 'Germany'): TRUE
        },
        part_of.name: {
            ('Ulm', 'Kingdom_of_Wuertemberg'): (0.6, 0.6)}
    }
    )

    model.print()

    model.infer()

    model.print()


example()
