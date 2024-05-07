import timeit
from time import sleep

from fibo import fibo_r, fibo_i

def _test_performance():
  n = 0
  while fibo_r(n) <= 23788:
    n += 1

  # Mesurer les performances
  setup_code = "from __main__ import fibo_r, fibo_i"
  test_r_code = f"fibo_r({n})"
  test_i_code = f"fibo_i({n})"

  time_r = timeit.timeit(test_r_code, setup=setup_code, number=1000)
  time_i = timeit.timeit(test_i_code, setup=setup_code, number=1000)

  print(f"Temps pour fibo_r({n}) sur 1000 itérations : {time_r} secondes")
  print(f"Temps pour fibo_i({n}) sur 1000 itérations : {time_i} secondes")

if __name__ == "__main__":
  _test_performance()