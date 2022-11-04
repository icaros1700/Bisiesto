
def bisiesto(año):
    if not año % 4 and (año % 100 or not año % 400):
        print("Este año es Bisiesto")
    else:
        print("Este año no es Bisiesto")


bisiesto(2022)
