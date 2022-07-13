# Hybrid Intelligence

Lecture material for a Hybrid Intelligence Course

Lecture 8 - Logical Neural Networks




## Example output

```
***************************************************************************
                                LNN Model

AXIOM  ForAll: part_of_are_birthplaces ('x', 'a', 'b')          TRUE (1.0, 1.0)

OPEN   Implies: Implies_1('x', 'a', 'b') 

OPEN   And: And_1('x', 'a', 'b') 

AXIOM  ForAll: birthplaces_are_part_of ('x', 'a', 'b')          TRUE (1.0, 1.0)

OPEN   Implies: Implies_0('x', 'a', 'b') 

OPEN   Or: Or_0('a', 'b') 

OPEN   Predicate: partOf('x0', 'x1') 
('Ulm', 'Kingdom_of_Wuertemberg')                    APPROX_TRUE (0.6, 0.6)

OPEN   And: And_0('x', 'a', 'b') 

OPEN   Predicate: bornIn('x0', 'x1') 
('Albert', 'Ulm')                                           TRUE (1.0, 1.0)
('Albert', 'Germany')                                       TRUE (1.0, 1.0)

***************************************************************************

***************************************************************************
                                LNN Model

AXIOM  ForAll: part_of_are_birthplaces ('x', 'a', 'b')          TRUE (1.0, 1.0)

OPEN   Implies: Implies_1('x', 'a', 'b') 
('Albert', 'Ulm', 'Germany')                                TRUE (1.0, 1.0)
('Albert', 'Ulm', 'Ulm')                                    TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Germany')             TRUE (1.0, 1.0)
('Albert', 'Germany', 'Kingdom_of_Wuertemberg')             TRUE (1.0, 1.0)
('Albert', 'Germany', 'Germany')                            TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Ulm')                 TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Kingdom_of_Wuertemberg')          TRUE (1.0, 1.0)
('Albert', 'Ulm', 'Kingdom_of_Wuertemberg')                 TRUE (1.0, 1.0)
('Albert', 'Germany', 'Ulm')                                TRUE (1.0, 1.0)

OPEN   And: And_1('x', 'a', 'b') 
('Albert', 'Ulm', 'Ulm')                                 UNKNOWN (0.0, 1.0)
('Albert', 'Germany', 'Kingdom_of_Wuertemberg')          UNKNOWN (0.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Ulm')              UNKNOWN (0.0, 1.0)
('Albert', 'Ulm', 'Kingdom_of_Wuertemberg')          APPROX_TRUE (0.6, 0.6)
('Albert', 'Germany', 'Ulm')                             UNKNOWN (0.0, 1.0)
('Albert', 'Ulm', 'Germany')                             UNKNOWN (0.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Kingdom_of_Wuertemberg')       UNKNOWN (0.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Germany')          UNKNOWN (0.0, 1.0)
('Albert', 'Germany', 'Germany')                         UNKNOWN (0.0, 1.0)

AXIOM  ForAll: birthplaces_are_part_of ('x', 'a', 'b')          TRUE (1.0, 1.0)

OPEN   Implies: Implies_0('x', 'a', 'b') 
('Albert', 'Ulm', 'Germany')                                TRUE (1.0, 1.0)
('Albert', 'Ulm', 'Ulm')                                    TRUE (1.0, 1.0)
('Albert', 'Germany', 'Germany')                            TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Ulm')                 TRUE (1.0, 1.0)
('Albert', 'Ulm', 'Kingdom_of_Wuertemberg')                 TRUE (1.0, 1.0)
('Albert', 'Germany', 'Ulm')                                TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Kingdom_of_Wuertemberg')          TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Germany')             TRUE (1.0, 1.0)
('Albert', 'Germany', 'Kingdom_of_Wuertemberg')             TRUE (1.0, 1.0)

OPEN   Or: Or_0('a', 'b') 
('Ulm', 'Kingdom_of_Wuertemberg')                    APPROX_TRUE (0.6, 1.0)
('Kingdom_of_Wuertemberg', 'Ulm')                    APPROX_TRUE (0.6, 1.0)
('Ulm', 'Germany')                                          TRUE (1.0, 1.0)
('Germany', 'Ulm')                                          TRUE (1.0, 1.0)
('Ulm', 'Ulm')                                              TRUE (1.0, 1.0)
('Germany', 'Germany')                                      TRUE (1.0, 1.0)
('Kingdom_of_Wuertemberg', 'Kingdom_of_Wuertemberg') APPROX_UNKNOWN (0.2, 1.0)
('Germany', 'Kingdom_of_Wuertemberg')                APPROX_TRUE (0.6, 1.0)
('Kingdom_of_Wuertemberg', 'Germany')                APPROX_TRUE (0.6, 1.0)

OPEN   Predicate: partOf('x0', 'x1') 
('Ulm', 'Kingdom_of_Wuertemberg')                    APPROX_TRUE (0.6, 0.6)
('Kingdom_of_Wuertemberg', 'Ulm')                        UNKNOWN (0.0, 1.0)
('Germany', 'Ulm')                                       UNKNOWN (0.0, 1.0)
('Germany', 'Kingdom_of_Wuertemberg')                    UNKNOWN (0.0, 1.0)
('Ulm', 'Ulm')                                           UNKNOWN (0.0, 1.0)
('Kingdom_of_Wuertemberg', 'Kingdom_of_Wuertemberg')       UNKNOWN (0.0, 1.0)
('Ulm', 'Germany')                                       UNKNOWN (0.0, 1.0)
('Kingdom_of_Wuertemberg', 'Germany')                    UNKNOWN (0.0, 1.0)
('Germany', 'Germany')                                   UNKNOWN (0.0, 1.0)

OPEN   And: And_0('x', 'a', 'b') 
('Albert', 'Ulm', 'Germany')                                TRUE (1.0, 1.0)
('Albert', 'Germany', 'Germany')                            TRUE (1.0, 1.0)
('Albert', 'Ulm', 'Ulm')                                    TRUE (1.0, 1.0)
('Albert', 'Germany', 'Ulm')                                TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Ulm')          APPROX_TRUE (0.6, 1.0)
('Albert', 'Ulm', 'Kingdom_of_Wuertemberg')          APPROX_TRUE (0.6, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Kingdom_of_Wuertemberg') APPROX_UNKNOWN (0.2, 1.0)
('Albert', 'Kingdom_of_Wuertemberg', 'Germany')      APPROX_TRUE (0.6, 1.0)
('Albert', 'Germany', 'Kingdom_of_Wuertemberg')      APPROX_TRUE (0.6, 1.0)

OPEN   Predicate: bornIn('x0', 'x1') 
('Albert', 'Ulm')                                           TRUE (1.0, 1.0)
('Albert', 'Germany')                                       TRUE (1.0, 1.0)
('Albert', 'Kingdom_of_Wuertemberg')                 APPROX_TRUE (0.6, 1.0)

***************************************************************************
```