def test_if_fibo_i_is_correct():
  """
  Test unitaire pour les fonctions fibo_r et fibo_i.
  - Tester que les deux fonctions donnent le même résultat pour les indices de la suite de Fibonacci 
  """

  from fibo import fibo_r, fibo_i

  n = 0
  while True:
    fib_r = fibo_r(n)
    fib_i = fibo_i(n)
    assert fib_r == fib_i, f"Erreur à l'index {n}: fibo_r donne {fib_r}, fibo_i donne {fib_i}"
    if fib_r > 23788:
      print(f"Le premier n où F(n) > 23788 est {n}, F(n) = {fib_r}")
      break
    n += 1