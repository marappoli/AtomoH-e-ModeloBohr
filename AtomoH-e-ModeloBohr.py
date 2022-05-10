import numpy as np 
#variavel para indicar o tipo de exercicio
para = int
#menu em loop
while (para != 5): 
 #constantes
 pi = 3.14159265359
 c = 3*10**8
 h = 4.14e-15
 #colinha para auxiliar nos exercicios
 #obs: a colinha sempre será printada, então para visualizar a resposta, rolar pra cima
 print("***************** Colinha *****************")
 print("Modelo de Bohr: Energia do foton n1 = -13.6")
 print("Modelo de Bohr: Energia do foton n2 = -3.4")
 print("Modelo de Bohr: Energia do foton n3 = -1.51")
 print("Modelo de Bohr: Energia do foton n4 = -0.85")
 print("Modelo de Bohr: Energia do foton n5 = -0.54")
 print("Modelo de Bohr: Energia do foton n6 = -0.38")
 print("Modelo de Bohr: Energia do foton n7 = -0.28")
 print("\n")
 print("Lyman: ni = 1")
 print("Balmer: ni = 2")
 print("Paschen: ni = 3")
 print("Brackett: ni = 4")
 print("Pfund: ni = 5")
 print("\n")

  
#menu para inidicar qual o tipo de exercicio
 print('\\\\MENU//')
 print("(1) Valores para elétron")
 print("(2) Valores para fóton")
 print("(3) Nível Final")
 print("(4) Nível Inicial")
 print("(5) Sair do programa")
 para = int(input("Insira o exercício: "))

  
#condições que executam o exercicio pedido
 if(para == 1):
   n = int(input("Insira o valor de n: "))
   r = n**2*5.29e-11
   rnm = r * 1e9
   v = (2.187e6)/n
   k = 13.6/n**2
   U = -27.2/n**2
   E = k*(-1)
   lambida = (6.626e-34)/(9.10938291e-31*v)
   lambnm = lambida * 1e9
   print("\n")
   print("Raio da órbita: ")
   print(np.format_float_scientific(r, unique= False, 
 precision = 2),"m")
   print(np.format_float_scientific(rnm, unique= 
 False, precision = 2),"nm")
   print("\n")
   print("Velocidade: ")
   print(np.format_float_scientific(v, unique= False, 
 precision = 2),"m/s")
   print("\n")
   print("Energia cinética: ")
   print(np.format_float_scientific(k, unique= False, 
 precision = 2),"eV")
   print("\n")
   print("Energia potencial: ")
   print(np.format_float_scientific(U, unique= False, 
 precision = 2),"eV")
   print("\n")
   print("Energia total: ")
   print(np.format_float_scientific(E, unique= False, 
 precision = 2),"eV")
   print("\n")
   print("Comprimento de onda: ")
   print(np.format_float_scientific(lambida, unique= 
 False, precision = 2),"m")
   print(np.format_float_scientific(lambnm, unique= 
 False, precision = 2),"nm")
   print("\n")

   
 elif (para == 2):
   ni = float(input("Insira o valor de ni: \n"))
   nf = float(input("Insira o valor de nf: \n"))
   Ei = -13.6/ni**2
   Ef = -13.6/nf**2
   E = Ei - Ef
   Eabs = Ef - Ei
   lambida = 4.14e-15*c/E
   lambnm = lambida * 1e9
   frequencia = E/4.14e-15
   fT = frequencia * 1e-12
   print("\n")
   print("Lâmbida: ")
   print(np.format_float_scientific(lambida, unique= 
 False, precision = 2),"m")
   print(np.format_float_scientific(lambnm, unique= 
 False, precision = 2),"nm")
   print("\n")
   print("Energia do fóton: ")
   print(np.format_float_scientific(E, unique= False, 
 precision = 2),"eV")
   print("\n")
   print("Energia absorvida: ")
   print(np.format_float_scientific(Eabs, unique= 
 False, precision = 2),"eV")
   print("\n")
   print("Frequência: ")
   print(np.format_float_scientific(frequencia, 
 unique= False, precision = 2),"Hz")
   print(np.format_float_scientific(fT, unique= 
 False, precision = 2),"THz")
   print("\n")

   
 elif (para == 3):
   entrada = int(input("Lambida(1)   Frequência(2)\n"))
   if (entrada == 1):
     ni = int(input("Insira o valor de ni: "))
     lambida = float(input("Insira o valor de lambida: "))
     Eabs = h*c/lambida
     Ef = (-13.6/ni**2)+Eabs
     nf = (-13.6/Ef)**(1/2)
     print("\n")
     print("nf: ")
     print(np.format_float_scientific(nf, unique= 
 False, precision = 2))
     print("\n")
   elif(entrada == 2):
     ni = int(input("Insira o valor de ni: "))
     frequencia = float(input("Insira o valor da frequência: "))
     Eabs = h*frequencia
     Ef = (-13.6/ni**2)+Eabs
     nf = (-13.6/Ef)**(1/2)
     print("nf: ")
     print(np.format_float_scientific(nf, unique= 
 False, precision = 2))
     print("\n")

     
 elif (para == 4):
   entrada = int(input("Lambida(1)   Frequência(2)\n"))
   if (entrada == 1):
     nf = int(input("Insira o valor de nf: "))
     lambida = float(input("Insira o valor de lambida: "))
     Eabs = h*c/lambida
     if (Eabs > 13.6):
      print("O átomo é ionizado")
     else:
       Ei = (-13.6/nf**2)-Eabs
       ni = (-13.6/Ei)**(1/2)
       print("nf: ")
       print(np.format_float_scientific(ni, unique= False, precision = 2))
     print("\n")
   elif(entrada == 2):
     nf = int(input("Insira o valor de nf: "))
     frequencia = float(input("Insira o valor da frequência: "))
     Eabs = h*frequencia
     if (Eabs > 13.6):
      print("O átomo é ionizado") 
     else:
       Ei = (-13.6/nf**2)+Eabs
       ni = (-13.6/Ei)**(1/2)
       print("nf: ")
       print(np.format_float_scientific(ni, unique= False, precision = 2))
       print("\n")