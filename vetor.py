estojo = []
print ("Olá, você quer colocar algo no estojo?")
objeto = " "
while objeto != 0:
  objeto = int(input("Deseja colocar um objeto? (1 para Sim e 0 para Não)"))
  if objeto ==1:
    item= input("Digite qual item você quer colocar:")
    estojo.append (item)
    for item in estojo:
      print (item)
  else:
    print ("Pronto! Aqui estão seus itens:")
    for item in estojo:
      print (item)
