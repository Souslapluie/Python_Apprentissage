


class Personne(): 
  
    def __init__(self, Name, Age, Passion) :
    	self.Name = Name
    	self.Age = Age
    	self.Passion = Passion
		

    def affiche(self) :
    	print(self.Name)
		

Paul = Personne("McCartney", 666, "Mécanique")
John = Personne("Lennon", 80, "Philosophie")

Paul.affiche()


# ------ AU DESSUS = MATIN ------ #
# ------ EN DESSOUS = APREM ----- #


class Vecteur() :

	def __init__(self, a, b) :
		self.a = a
		self.b = b

	def __str__(self) :
		# Représentation textuelle de l'objet courant.
		return "(" + str(self.a) + ";" + str(self.b) + ")"
	"""
	def additionner(a2, b2) :
		x = a2.a + b2.a
		y = a2.b + b2.b
		res = Vecteur(x, y)
		return res


	def aff(self) :
		print()



v1 = Vecteur(3, 4)
v2 = Vecteur(1, 2)
v3 = res
print(v3, res)

res.affiche
"""

# ----------- En dessous = Super class ----------- #


class Point2D() :

	def __init__(self, a, b) :
		self.z = a
		self.n = b

	def __str__(self) :
		return "Point2D(();())".format(self.z, self.n)

	"""
	def affiche2D(self) :
		print(self.a, self.b)
	"""

class Point3D(Point2D) :

	def __init__(self, a, b, c) :
		
		super().__init__(a, b)
		self.v = c

	def __str__(self) :
		return "Point3D(();();())".format(self.z, self.n, self.v)
	"""	
	def affiche3D(self) :
		print(self.a, self.b, self.c)
	"""


Point2 = Point2D(55, 1969)
Point1 = Point3D(12, 21, 2021)

Point1.__str__() 
Point2.__str__()





