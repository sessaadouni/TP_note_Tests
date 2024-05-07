# exemple timeit.timeit
import timeit
from time import sleep

def hello(name: str):
  sleep(0.001)
  return f"Hello {name}"

def goodbye(name: str):
  sleep(0.001)
  return f"Goodbye {name}"

def exemple_timeit():
  time_hello = timeit.timeit(lambda: hello("Toto"), number=10000)
  time_goodbye = timeit.timeit(lambda: goodbye("Tutu"), number=10000)
  print("Durée de hello:", time_hello)
  print("Durée de goodbye:", time_goodbye)

if __name__ == '__main__':
  exemple_timeit() # a supprimer pour le rendu