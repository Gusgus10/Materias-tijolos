def  tijolo():
  
  PCM = int(input('Digite a proporção de cimento: ')) #PCM = PROPORÇÃO DE CIMENTO
  PCL = int(input('Digite a proporção de cal: ')) #PCL = PROPORÇÃO DE CAL
  PAR = int(input('Digite a proporção de areia: ')) #PAR = PROPORÇÃO DE AREIA
  LJT = float(input('Digite a largura da junta: ')) #LJT = LARGURA DA JUNTA
  LTJ = float(input('Digite a largura do tijolo: ')) #LTJ = LARGURA DO TIJOLO
  HTJ = float(input('Digite a altura do tijolo: ')) #HTJ = ALTURA DO TIJOLO
  CTJ = float(input('Digiteo o comprimento do tijolo: ')) #CTJ = COMPRIMENTO DO TIJOLO
  APD = float(input('Digite a área da parede: ')) #APD = ÁREA DA PAREDE 

  qar = LJT*LTJ*((2*HTJ)+CTJ)(1.07/((HTJ+1.5)(CTJ+1.5)/10000))*APD/1000000*1.05
  qcl = ((qar/PAR)*(PCL*670))/20
  qcm = (qar/PAR)*1400/50
  qtj = 1.07/((HTJ+1.5)*(CTJ+1.5)/10000)*APD
  return ('CIMENTO: {:.2f} sacos de 50kg CAL: {:.2f} sacos de 20kg AREIA {:.2f}m³ TIJOLOS: {:.2f} unidades'.format(qcm,qcl,qar,qtj))

def chapisco():

  PCM = int(input('Digite a proporção de cimento: ')) #PCM = PROPORÇÃO DE CIMENTO
  PAR = int(input('Digite a proporção de areia: ')) #PAR = PROPORÇÃO DE AREIA
  ECP = float(input('Digite a espessura do emboço: ')) #ECP = ESPESSURA DO CHAPISCO
  ACP = float(input('Digite a área do emboço: ')) #ACP = ÁREA DO CHAPISCO

  qar =  ACP*ECP*1.05/1000
  qcm = (qar/PAR)*1400/50

  return ('CIMENTO: {:.2f} sacos de 50kg AREIA {:.2f}m³'.format(qcm,qar))

def reboco():

  PCM = int(input('Digite a proporção de cimento: ')) #PCM = PROPORÇÃO DE CIMENTO
  PCL = int(input('Digite a proporção de cal: ')) #PCL = PROPORÇÃO DE CAL
  PAR = int(input('Digite a proporção de areia: ')) #PAR = PROPORÇÃO DE AREIA
  EEB = float(input('Digite a espessura do emboço: ')) #EEB = ESPESSURA DO EMBOÇO
  AEB = float(input('Digite a área do emboço: ')) #AEB = ÁREA DO EMBOÇO

  qar =  AEB*EEB*1.05/100
  qcl = ((qar/PAR)*(PCL*670))/20
  qcm = (qar/PAR)*1400/50

  return ('CIMENTO: {:.2f} sacos de 50kg CAL: {:.2f} sacos de 20kg AREIA {:.2f}m³'.format(qcm,qcl,qar))

def cerebro():
  
  print('1 - Materiais para assentamento de tijolo furado')
  print('2 - Quantidade de materiais para chapisco')
  print('3 - Quantidade de materiais para emboço/reboco')
  op = int(input())

  if op == 1:
    print(tijolo())
    continuar()
  elif op == 2:
    print(chapisco())
    continuar()
  elif op == 3:
    print(reboco())
    continuar()

def continuar():
  x = input('Quer continuar? ')
  if x == 'sim':
    cerebro()
    

cerebro()
  