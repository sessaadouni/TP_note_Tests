import pytest
from exception import BadNumber

def test_convert_int():
  """
  Test unitaire pour la fonction convert_int.
  - Tester que la fonction convertit correctement une chaîne de caractères en nombre entier.
  - Tester que la fonction lève une exception BadNumber si la chaîne de caractères n'est pas un nombre valide.
  """
  from convert import convert_int

  assert convert_int("1500") == 1500
  assert convert_int("1.5E3") == 1500
  assert convert_int("31416.0e-4") == 3

  with pytest.raises(BadNumber): convert_int("3.14.15")
  with pytest.raises(BadNumber): convert_int("xyz")
  with pytest.raises(BadNumber): convert_int(None)

def test_convert_float():
  """
  Test unitaire pour la fonction convert_float.
  - Tester que la fonction convertit correctement une chaîne de caractères en nombre à virgule flottante.
  - Tester que la fonction lève une exception BadNumber si la chaîne de caractères n'est pas un nombre valide.
  """
  from convert import convert_float

  assert convert_float("0.31416e1") == 3.1416
  assert convert_float("31416.0e-4") == 3.1416
  assert convert_float("1.5E3") == 1500.0

  with pytest.raises(BadNumber): convert_float("abc")
  with pytest.raises(BadNumber): convert_float("123.456.789")
  with pytest.raises(BadNumber): convert_float(None)