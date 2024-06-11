bellavista = "no puede ir"
italia = "no puede ir"
valpo = "no puede ir"
after = "no puede ir"
happy = "no puede ir"

dia = input("ingrese dia: ")
edad = int(input("ingrese su edad: "))
dinero = int(input("ingrese su dinero: "))

if dinero >= 1000 and edad >= 18:
    bellavista = "puede ir"
    print("a pistearrrrr")

if dinero >= 4000 and edad >= 18 and dia in "jue vie sab dom":
    italia = "puede ir"
    print("tamo de la italiani")

if dinero > 500 and edad >= 18 and dia in "sab dom":
    valpo = "puede ir"
    print("valpo ql feo")

if dinero >= 6000 and edad >= 25 and dia in "jue vie sab dom":
    after = "puede ir"
    print("after siii casa nooo")

if dinero >= 1000 and edad >= 13:
    happy = "puede ir"
    print("vamo a felicidlandia")