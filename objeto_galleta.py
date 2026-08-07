# Clase del aula 27/07/26
class galleta:
  def __init__(self, tipo, forma, sabor, tamano):
    self.tipo = tipo
    self.forma = forma
    self.sabor = sabor
    self.tamano = tamano

  def comprar (self):
      print('comprando galleta')

  def comer(self):
      print('comiendo...')

# Instacias
galleta1 = galleta('dulce','redonda','chocolate','13cm')
galleta2 = galleta('salada','rectangular','salada','13cm')

# Resultados
print(f'Tengo una galleta de {galleta1.sabor}')
comer = input('comer galleta ? (si/no) ')
if comer.lower() == 'si':
  galleta1.comer()
elif comer.lower() == 'no':
  print('mejor no')