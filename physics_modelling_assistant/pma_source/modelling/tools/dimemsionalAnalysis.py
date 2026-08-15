# sympy is what actually does the dimensional analysis
from sympy.physics.units import Dimension, Quantity
from sympy import symbols
import sympy

# this is for putting the tool into the crewAi framework, it is not used in the actual dimensional analysis
from typing import Optional, Type, List
import os
import json
from pathlib import Path
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class DimensionalAnalysisInput(BaseModel):
    equation: str = Field(..., description="The equation to analyze, represented as a string. Do not use sympy special symbols like, 'E', 'e', 'I', 'pi', 'I'. Allowed operators: '+', '-', '*', '/', '**'. Example: 'F = m * a'.")
    dimensions: dict[str, str] = Field(..., description="A dictionary containing variable names as keys and their corresponding dimensions as values, providing all properties in the 7 SI base units is preferred. Example: {'x': 'length', 'v': 'length/time'}.")
    unitList: str = Field(..., description="A string containing all the units to be used in the analysis, separated by a specified separator. Example: 'length, time, mass'.")
    separator: str = Field(default=",", description="The separator used in the unitList string. Default is ','.")

class DimensionalAnalysis(BaseTool):
    name: str = "dimensional_analysis"
    description: str = "Perform dimensional analysis on a given equation."
    args_schema: Type[BaseModel] = DimensionalAnalysisInput

    def _run(self, equation : str, dimensions : dict[str, str], unitList : str, separator : str = ","):
        """
        Perform dimensional analysis on the given equation.

        Parameters:
        equation (str): The equation to analyze, represented as a string.
        dimensions (dict[str, str]): A dictionary containing variable names as keys and their corresponding dimensions as values.

        Returns: unit_missmatch (str): A string with the units needed to be addded to the right hand side of the equation to achieve unit consistency
        """

        #build the unit registry
        unitRegistry = unitLister(unitList = unitList, separator = separator).getUnits()

        # calculate the units of each variable
        allVariables : list[VariableObject] = [] # list containing all the variables found
        
        for var in dimensions.keys():
            units = dimensions[var]
            allVariables.append(VariableObject(variable=var, dimension=units, stringRep=var, unitRegistry=unitRegistry))

        # now plug the units into the equation and check if the units on both sides are the same
        equationHanderInstace : EquationHandler = EquationHandler(equation=equation, variables=allVariables)
        leftUnit, rightUnit, proposedCorrection = equationHanderInstace.check_units()
        return proposedCorrection


class unitLister():
    """
    class that stores all the possible units and their string representation
    """
    def __init__(self, unitList : str, separator : str = ","):
        """ extract the units from the list and make them available as a list of sympy units"""
        self.units : dict = {} # dictionary of sympy units and their string representation
        for unit in unitList.split(separator):
            self.units[unit.strip()] = Quantity(unit.strip()) # quantity stores the real unit better, Dimensions wraps it
    
    def getUnits(self):       
        return self.units

    def getDimension(self, unit : str):
        return self.units.get(unit.strip())


class VariableObject():
    def __init__(self, variable : str, dimension : str, stringRep : str, unitRegistry : dict):
        """
        creates a variable object which stores the varable with its properties

        Parameters:
        symbol (sympy.Symbol): the variable as a sympy symbol, used for calculations
        dimensions (list[]): a string contating all the units with "*", "/", "**"
        stringRep (str): the variable as a string, used for printing
        """
        self.variable : sympy.Symbol = symbols(variable) # the variable as a sympy symbol, usable for calculations
        self.unitRegistery : dict = unitRegistry # the unit registry, used for parsing the dimensions
        self.unit : sympy.physics.units.Quantity = self.parse_unit(expression = dimension)
        self.stringRep : str = stringRep # the variable as a string, used for printing
    
    def parse_unit(self, expression: str):
        # Only allow names that exist in the registry
        # registry are the units previously defined in the unitLister class

        allowed = {name: obj for name, obj in self.unitRegistery.items()}
        return sympy.sympify(expression, locals=allowed)

class EquationHandler():
    def __init__(self, equation : str, variables : list[VariableObject]):
        self.equation : str = equation
        self.variables : list[VariableObject] = variables

    def substitute_units(self, expr, var_units, unit_registry):
        subs = {}
        for var, unit_str in var_units.items():
            subs[symbols(var)] = self.variables[var].parse_unit(unit_str)
        return expr.subs(subs)
    
    def substitute_units(self, expression : sympy.Expr):
        subs = {self.variables[i].variable: self.variables[i].unit for i in range(len(self.variables))}
        return expression.subs(subs)

    def check_units(self):
        # split the equation into left and right side
        leftSide, rightSide = self.equation.split("=")
        leftSideSympy : sympy.Expr = sympy.sympify(leftSide.strip())
        rightSideSympy : sympy.Expr = sympy.sympify(rightSide.strip())

        # replace the variables in the equation with their units
        leftUnits = self.substitute_units(leftSideSympy)
        rightUnits = self.substitute_units(rightSideSympy)
        #print(f"Left side units: {leftUnits}, Right side units: {rightUnits}")

        # divide left units by right units; right side needs to be multiplied by correction to get consistent units
        proposedCorrection = sympy.simplify(leftUnits / rightUnits)

        return leftUnits, rightUnits, proposedCorrection

def testFunction():
    # this is a test method for manual testing
    # sympy has some problems with special symbols like 'E', 'I', 'pi', 'I', so we need to use different symbols for the variables in the equation
    input_data = DimensionalAnalysisInput(
        equation="M = muB * eL * tau / (2 * pi) * m * alpha * E",
        dimensions={"M": "A/m", "muB": "kg/(s**2 * A)", "eL": "C", "tau": "s", "m": "kg", "alpha": "kg* m**2 /s**2 *m", "E": "kg * m**2/s**3/A/m"},
        unitList="A, kg, s, m, C",
        separator=","
    )

    dimensionalAnalysisInstance = DimensionalAnalysis()
    result = dimensionalAnalysisInstance._run(**input_data.dict())
    print(f"Proposed correction for the equation '{input_data.equation}': {result}")

if __name__ == "__main__":
    testFunction()