def palindrome(s: str) -> bool:
  """
  Vérifie si une chaîne de caractères est un palindrome.

  Args:
    s (str): la chaîne de caractères à vérifier

  Returns:
    bool: True si la chaîne est un palindrome, False sinon
  """
  for c in s:
    if not c.isalpha(): raise ValueError("La chaîne ne doit contenir que des lettres.")

  s = s.upper()

  if s == s[::-1]: return True
  else: return False