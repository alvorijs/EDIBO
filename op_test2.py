class PartyAnimal
   x = 0
   #_ init_metode tiks izpildita tikai vienu
   #reizi, veidojot (katru) instanci



   def __init__(self):
     print('I am constructed')
     x = 0
     
   def party(self) :
       self.x = self.x =1
       print("So far x property of objekt",\
             "is: ",self.x)
       print("Before an = PartyAnimal()")
       #print(vars())
       an = PartyAnimal()
       print("After an = PartyAnimal()")
       #print(vars())
       print("an data type or class:", type(an))
       print("an methods and properties:", dir(an))
       print("an x property data type:", type(an.x))
       print("an party method data type:", type(an.party))
       print(vars(an)) #objekts tikai izveidots {}?

       print("\nBefore first an.party()")
       an.party()
       print("After first an.party()")
       #print(vars(an)) # objekts "aiztikts"{"x": 1}
       an.x = 100
       print("\nBefore second an.party()")
       an.party()
       # ja klase ir bez _init_, tad{}
       # ja klase ir ar _init_, ar self.x = ...
       # tikai tad  {"x" : 0}, savadak ir {}
       
       
       
