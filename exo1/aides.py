def demo_chaines():
  print("Demo chaines".center(40))
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for num, caractere in enumerate(alphabet):
    print(f"Caractère {num + 1}: {caractere}")

def demo_liste():
  print("Demo liste".center(40))
  nombres = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42, 613, 942, -3213, 18, 3.5]
  print("Liste dans l'ordre:", nombres)
  print("Liste à l'envers:", nombres[::-1])
  print("Troisième élément de la liste (indexation à partir de 0):", nombres[2])
  print("Quatrième élément de la liste à l'envers:", nombres[::-1][3])

if __name__ == '__main__':
  demo_chaines()
  demo_liste()
