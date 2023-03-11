print ("Bienvenido al Sistema de notas")
respuesta= input("Desea conocer su Promedio y estatus academico?, Ingrese Si O No: ")
if (respuesta=="Si"):
    nota1= int(input ("Ingrese Calificación 1: "))
    nota2= int(input ("Ingrese Calificación 2: "))
    nota3= int(input ("Ingrese Calificación 3: "))
    promedio=(nota1+nota2+nota3)/3

    if (promedio== 6):
        print ("Tu promedio es: ",promedio,"Usted esta Aprobado nivel Basico")
    if (promedio<6):
        print("Tu promedio es: ",promedio,"Usted esta desaprobado")
    if (promedio>6):
     print("Tu promedio es: ",promedio,"Usted esta Aprobado Nivel Avanzado")
print ("Gracias por Consultar nuestra Apps")