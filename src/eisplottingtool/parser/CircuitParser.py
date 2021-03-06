import re
from typing import Callable, Tuple

import numpy as np

from eisplottingtool.parser.CircuitComponents import circuit_components
from eisplottingtool.utils.Parameter import Parameter


def parse_circuit(
    circ: str,
) -> Tuple[list[Parameter], Callable[[dict, np.array], np.array]]:
    """EBNF parser for a circuit string.

    Implements an extended Backus–Naur form to parse a string that descirbes
    a circuit.
    Already implemented circuit elements are locacted in CircuitComponents.py

    To put elements in series connect them through -
    Parallel elements are created by p(Elm1, Elm2,...)

    The syntax of the EBNF is given by:
        - circuit = element | element-circuit
        - element = component | parallel
        - parallel = p(circuit {,circuit})
        - component = a circuit component

    From this a formuilation is generated and evaluated.

    Parameters
    ----------
    circ : str
        String that descirbes a circuit

    Returns
    -------
    param_info: list[Parameter]
        list of used parameter. for more information about parameters look in circuit_components
    calculate: Callable[[dict, np.array], np.array]
        Evaluating function of the impedance of the given circuit

    """

    param_info: list[Parameter] = []

    def component(c: str):
        """process component and remove from circuit string c

        Parameters
        ----------
        c : str
            circuit string

        Returns
        -------

        """
        # get and remove the name of the component from the circuit string
        match = re.match(r"([a-zA-Z]+)_?\d?", c)
        index = match.end()
        name = c[:index]
        c = c[index:]

        # get the symbol of the component and check if the component exists
        symbol = re.match("[A-Za-z]+", name).group()

        for key, comp in circuit_components.items():
            if comp.get_symbol() == symbol:
                break
        else:
            return c, 1

        # append the parameter to param info
        param_info.extend(comp.get_parameters(name))

        # return the circuit string and return a string for later evaluation
        return c, key + rf".calc(param,'{name}', omega)"

    def parallel(c: str):
        c = c[2:]
        tot_eq = ""
        while not c.startswith(")"):
            if c.startswith(","):
                c = c[1:]
            c, eq = circuit(c)
            if tot_eq:
                tot_eq += " + "
            tot_eq += f"1.0 / ({eq})"
        c = c[1:]
        return c, f"1.0 / ({tot_eq})"

    def element(c: str):
        if c.startswith("p("):
            c, eq = parallel(c)
        else:
            c, eq = component(c)
        return c, eq

    def circuit(c: str):
        if not c:
            return c, ""
        c, eq = element(c)
        tot_eq = f"{eq}"
        if c.startswith("-"):
            c, eq = circuit(c[1:])
            tot_eq += f" + {eq}"
        return c, tot_eq

    __, equation = circuit(circ.replace(" ", ""))

    calculate = eval("lambda param, omega: " + equation, circuit_components.copy())
    return param_info, calculate
