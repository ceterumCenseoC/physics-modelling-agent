from sympy.physics.units import Dimension, length, time, mass
from sympy.physics.units import dimension_system
from sympy import symbols

def VariableObject():
    def __init__(self, symbol : str, dimension : str, stringRep : str):
        self.symbol : sympy.symbols = symbols(symbol)
        unit = []
        lastCharIndex : int = 0
        i : int = 0
        while i < len(dimension):
            if dimension[i] == "*" or dimension[i] == "/":
                if len(unit) > 0:
                    unit.append(dimension)
                
                else:
                    unit.append(dimension[lastCharIndex:i-1].strip())
                
            i += 1

        self.dimension : str = dimension
        self.stringRep : str = stringRep

def dimensionalAnalysis(equation : str, dimensions : dict[str, str]):
    """
    Perform dimensional analysis on the given equation.

    Parameters:
    equation (sympy expression): The equation to analyze.
    variables (list of sympy symbols): The variables in the equation.
    dimensions (dict): A dictionary mapping each variable to its dimension.

    Returns:
    bool: True if the equation is dimensionally consistent, False otherwise.
    """
    # Calculate the dimensions of each term in the equation
    allVariables = []
    allDiemnsions = []
    mapDiemnsions = {}
    i : int = 0
    while i < len(dimensions):
        
    
        var = variables[i]
        dim = dimensions[var]
        allDiemnsions.append(dim)
        mapDiemnsions[var] = dim
        i += 1
    terms = equation.as_ordered_terms()
    term_dimensions = []
    
    for term in terms:
        term_dim = 1
        for var in variables:
            if var in term.free_symbols:
                term_dim *= dimensions[var] ** term.count(var)
        term_dimensions.append(term_dim)
    
    # Check if all terms have the same dimension
    return all(dim == term_dimensions[0] for dim in term_dimensions)