class Chat:
  def __init__(self, name: str):
    self.name = name

  def __str__(self):
    return '''
                     /)
Bonjour     /\___/\ ((
mon nom est \`@_@'/  )) %s!
            {_:Y:.}_//
 -----------{_}^-'{_}----------
Bon courage pour le contrôle!
''' % (self.name,)



if __name__ == '__main__':
  guigui = Chat('Guigui')
  print(str(guigui))