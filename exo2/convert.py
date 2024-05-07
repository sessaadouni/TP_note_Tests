import math
from exception import BadNumber

def convert_float(s: str) -> float:
  """
  Convertit une chaîne de caractères en nombre à virgule flottante.

  Args:
    s (str): La chaîne de caractères à convertir.

  Returns:
    float: Le nombre à virgule flottante correspondant à la chaîne de caractères.
  """
  if not isinstance(s, str): raise BadNumber("Input must be a string.")
  try: return float(s)
  except ValueError: raise BadNumber("Input string is not a valid float.")

def convert_int(s : str) -> int:
  """
  Convertit une chaîne de caractères en nombre entier.

  Args:
    s (str): La chaîne de caractères à convertir.

  Returns:
    int: Le nombre entiers correspondant à la chaîne de caractères.
  """
  if not isinstance(s, str): raise BadNumber("Input must be a string.")
  try: return int(float(s))
  except ValueError: raise BadNumber("Input string is not a valid integer.")
