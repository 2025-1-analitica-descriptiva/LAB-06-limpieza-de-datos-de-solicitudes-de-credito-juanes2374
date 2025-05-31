"""
Exponemos el sub-módulo `homework.pregunta_01` como atributo para que
`from homework import pregunta_01 as pregunta` funcione tal como lo
requiere el autograder.
"""
from importlib import import_module as _imp
pregunta_01 = _imp(__name__ + ".pregunta_01")   # noqa: F401
