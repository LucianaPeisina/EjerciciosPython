#saludo inicial

print("Bienvenidos a la calculadora de fraccciones")

respuesta=input("¿Quiere Usar la calculadora?\n si no")

#calculadora

if(respuesta=="si"):

    numerador1=int(input("ingrese un numerador "))

    denominador1=int(input("ingrese denominador "))

    print(numerador1,"/",denominador1, ">fraccion1")

    numerador2=int(input("ingrese un numerador "))

    denominador2=int(input("ingrese denominador "))

    print(numerador2,"/",denominador2, ">fraccion2")

    #Menu

    print("puede elegir 1 de las siguientes operaciones\nsuma\nresta\nmult\ndiv")

    operacion=input("ingrese opcion aqui ")

    if(operacion=="suma"):

        suma=((denominador2*numerador1)+(denominador1*numerador2))/(denominador1*denominador2)

        print("la suma es ",suma)

    if(operacion=="resta"):

        resta=((numerador1*denominador2)-(denominador1*numerador2))/(denominador1*denominador2)

        print("la resta es ",resta)

    if(operacion=="mult"):

        mult=(numerador1*numerador2)/(denominador1*denominador2)

        print("el resultdo es " ,mult)

    if(operacion=="div"):

        div=(numerador1*denominador2)/(denominador1*numerador2)

        print("el resultado es ",div)

print ("gracias por usar la app")