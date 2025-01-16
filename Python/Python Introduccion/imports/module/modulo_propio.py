"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
Correo electrónico: danielperezdev@proton.me 
"""
from typing import Tuple, Dict, Set, Union, List

def id_valor(*, valor: Union[str, int, float, bool, List, Tuple, Dict, Set]) -> str: return f"id {valor=} es " + str(id(valor)) 