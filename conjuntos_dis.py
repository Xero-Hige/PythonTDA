END = None

class Conjuntos_dis(object):
	def __init__ (self):
		self.number_of_elements=0
		self.elements={}
	
	def contar(self):
		return self.number_of_elements

	def pertenece_a(self,elemento):
		conjunto=self.elementos.get(elemento,False)
		if(not conjunto):
			raise ValueError,"No es un elemento existente valido"
		if (conjunto == END):
			return elemento
		conjunto=self.pertenece_a(conjunto)
		self.elementos[elemento]=conjunto
		return conjunto
	
	def agregar(self,id_elemento,conjunto=END):
		if(not id_conjunto):
			self.elementos[elemento]=elemento
		else:
			self.elementos[elemento]=conjunto
		self.cant_elem+=1
		
	def unir_conjuntos(self,id_elementoA,id_elementoB):
		conjunto_A = self.pertenece_a(elementoA)
		conjunto_B = self.pertenece_a(elementoB)
		self.elementos[conjunto_A]=conjunto_B