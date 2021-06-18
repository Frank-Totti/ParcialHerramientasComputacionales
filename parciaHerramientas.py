#dict = Dictionary(Python Files) of products and their prices
# iD = Identificaction Number of person
# Proc = Student or Teacher / For student (Sale = 50%); for teacher (Sale = 20%)
# d = list with twist of tuples, in each tuple in position 0 "Product" position 1 "Price"


def pricesSale(dic,iD,proc,d):
    for i in dic:
        for j in range(len(d)):
            if proc == "Estudiante" or proc == "estudiante":
            #for j in range(len(d)):
                if d[j][0] == dic[i][0]:
                    dic[i][1] *= d[j][1]
                    gom = dic[i][1] * 0.5
                    dic[i][1] -= gom
                    #dic[i][1] += dic[i][1]
                    print("El "+proc+" con número de identificación: "+iD+","+" debe pagar un total de "+ str(dic[i][1]) + " por la compra de: "+d[j][0])
                
            elif proc == "Profesor" or proc == "profesor":
                if d[j][0] == dic[i][0]:
                    dic[i][1] *= d[j][1]
                    gam = dic[i][1] * 0.2
                    dic[i][1] -= gam
                    print("El "+proc+" con número de identificación: "+iD+","+" debe pagar un total de "+ str(dic[i][1])+ " por la compra de: "+d[j][0])

            else:
                if d[j][0] == dic[i][0]:
                    dic[i][1] *= d[j][1]
                    print("Con número de identificación: "+iD+","+" debe pagar un total de "+ str(dic[i][1])+ " por la compra de: "+d[j][0])
# first input(), information of person

def written(dic):
    proc = input("¿Es profesor o estudiante?  ")
    iD = input("Ingrese su número de cedula o identificación  ")
    while len(iD) < 8 or len(iD) > 10:
        print("Entrada no valida")
        iD = input("Ingrese su número de cedula o identificación  ")
    t = 0
    cal = int(input("¿Cuantos productos va a llevar?"))
    print("A continuación ingrese el el producto espacio y luego la cantidad")
    d = []
    while t < cal:
        prog = input().split()
        gim = prog[0]
        val = int(prog[1])
        tup = (gim,val)
        d.append(tup)
        print(d)
        t += 1
    pricesSale(dic,iD,proc,d)
    
    
    
def boxin():
    dic = eval(input("Ingrese diccionario con códigos, productos y valores \n"))
    print(dic)
    written(dic)

boxin()

        
        
    
    



















