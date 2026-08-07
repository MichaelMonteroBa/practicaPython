class estudiante:
  def __init__(self, nombre , edad, grado) :
    self.nombre = nombre
    self.edad = edad
    self.grado = grado

  def estudiar(self):
    print(f"El estudiante {self.nombre} esta estudiando")

estudiante1 = estudiante ('michael', 18, 'primero')

print(f'el estudiante se llama {estudiante1.nombre}')
print(f'Y su curso es {estudiante1.grado} de bachiller')