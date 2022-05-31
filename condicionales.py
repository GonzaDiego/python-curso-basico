# Declaramos una variable
calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion) # Convertimos la variable a entero

# Preguntamos si la calificación es menor a 700
if calificacion < 700 :
    print("Sigue participando 🤷‍♂️") # Muestra esto si se cumple el primer if
elif calificacion > 1000 :
    print("Mientes! me haces daño y te luego arrepientes 😔")
else : # Si no se cumple el if anterior, pasa a esta línea
    print("Felicidades! Estás certificado 👍") # Se ejecuta si ninguno de los if se cumple 

# Verficador de mayoría de edad 
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 : 
    print("Bienvenido al patio mamitas 👯‍♀️")
elif edad > 100 :
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajer@ del tiempo")
else :
    print("Bienvenido a la choza de los pequeñines 👶")

# En Python no hay swith case