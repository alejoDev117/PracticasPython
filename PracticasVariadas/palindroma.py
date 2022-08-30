#rectifica si una palabra o numero es palindroma y tal

var = input("Ingrese la palabra o numero que desea evaluar\n")
suma = ""
for i in range(1 , len(var)+1):
      suma = suma + var[-i]

if var == suma :
    print("La palabra/numero es palindromo :\n ",suma)
else:
    print("No es palindromo\n")
