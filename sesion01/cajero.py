
billetes = [100, 50, 20, 10, 5, 1]
contraseña = 1090
saldoactual = 1000
intentos =  0
billetesentregados = []
i = 0
print("BIENVENIDO A TU CAJERO")


while intentos  < 3:
  clave = int(input("ingrese la clave "))
  if clave == contraseña:
      print('''ELIJA LA OPCION QUE DESEA
        1) Consultar saldo 
        2) Retirar
        ESCRIBA CUALQUIER OTRO NUMERO PARA SALIR''')
      opcion = int(input()) 
      if opcion == 1:
         print(f" Su saldo es: {saldoactual}")
         break
      elif opcion == 2:
         monto_a_retirar = int(input("¿Cuanto desea retirar?: "))
         while monto_a_retirar != 0:
            if monto_a_retirar <= saldoactual:
               if monto_a_retirar >= billetes[i]:
                  billetesentregados.append(billetes[i])
                  monto_a_retirar = monto_a_retirar- billetes[i]
               else:
                  i+=1
            else:
               print(f"No puede retirar ese valor, su saldo actual es de {saldoactual}")
               break
         print(f"Entregando billetes {billetesentregados}")

         
  else:
       print(f"clave incorrecta\nTiene {2 - intentos} intentos restantes antes de que su cuenta quede bloqueada")
       intentos+=1
       if intentos == 2:
          print("su cuenta esta bloqueada")
          break
          

    
      

