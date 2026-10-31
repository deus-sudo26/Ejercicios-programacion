'''
La jugueteia El MUNDO DE CHARLY nos encarga un programa para conocer quecantidad de materiales se necesita para la fabricacion dedistintos juguetes.

CONFECCIoN DE UN COMETA: 

AB = Diagonal mayor

DC = Diagonal menor

BD y BC = lados menores

AD y AC = lados mayores

El usuario ingresara las medidas  BC, CD y DA.

Detalles de construccion

Debemos tener en cuenta que la estructura del cometa estara dada por un perimetro de varillas de plastico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

El cometa estara construido con papel de alta resistencia. La cola del mismo se construira con el mismo papel que el cuerpo y representara un 10% adicional del necesario para el cuerpo.

Necesitamos saber cuantos Mts de varillas de plastico y cuantos de papel son necesarios para la construccion en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.



'''
#DIAGONAL MAYOR AB |
#DIAGONAL MENOR DC -
#LADO MAYOR AD Y AC
#LADO MENOR BD Y BC

#DATOS

ladomenor_bc = int(input("ingrese el lado menor BC en cm :"))

diagonalmenor_dc = int(input("ingrese el lado de la diagonal DC en cm: "))

ladomayor_da = int(input("ingrese el lado mayor DA en cm: "))

#la diagonal mayor la divido en dos partes ,punto a B Y punto a A
punto_a_B = (ladomenor_bc**2 - (diagonalmenor_dc/2)**2)**0.5
punto_a_A = ((diagonalmenor_dc/2)**2 - (ladomayor_da)**2)**0.5

diagonal_mayor = punto_a_B + punto_a_A

#total de cm de varillas
total_varillas = (ladomenor_bc*2 + ladomayor_da*2 + diagonalmenor_dc + diagonal_mayor)

#total de papel
papel_cometa = (diagonalmenor_dc * punto_a_B) / 2 + (diagonalmenor_dc * punto_a_A)/2
cola_cometa = papel_cometa * 0.1
total_papel_cometa = cola_cometa + papel_cometa

#Cuantos cometas quiero realizar?
Total_cometas = int(input("ingrese la cantidad de cometas a realizar: "))
papel_cometa_masa = total_papel_cometa * Total_cometas
varillas_cometa_masa = total_varillas * Total_cometas

#SALIDAS
print("El total en cm de varillas para un cometa es:" , total_varillas , "cm")
print("El total de cm de papel para un cometa es: ", total_papel_cometa , "cm")
print(f"Para la produccion en masa de {Total_cometas} cometas necesito {varillas_cometa_masa} cm de varillas y {papel_cometa_masa} cm de papel")