import pytest

def test_palindrome():
  """
  Test unitaire pour la fonction palindrome.
  - Tester que avec un mot simple, en majuscules et sans accents, la fonction retourne True si le mot est un palindrome, False sinon.
  """
  from palindrome import palindrome

  with pytest.raises(ValueError): palindrome("12321")

  with pytest.raises(ValueError): palindrome("BLA3BLA")

  assert palindrome("KAYAK") == True
  assert palindrome("RADAR") == True
  assert palindrome("BONJOUR") == False