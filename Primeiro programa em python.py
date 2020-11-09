# Criar variavéis com todas as diciplina de seu curso em seguida mostrar as notas  de cada
#diciplina e  depois calcula a média geral.

media = 0
Inovacao= float (input ('Qual sua nota em Inovação?  '))
Programacao = float (input('Qual sua nota em Programação?  '))
Rede= float (input ('Qual a sua nota em Rede?  '))
Informatica= float (input ('Qual sua nota em Informática?  '))
Estrutura=  float (input ('Qual sua nota em Estruta?  '))

media = ( Inovacao + Programacao + Rede + Informatica + Estrutura) / 5

print ('Sua nota em Inovação é:  ', Inovacao, ', sua nota em Programação é:  ', Programacao,
       ', sua  nota em Rede é:  ' , Rede, ', sua nota em Informática é:  ', Informatica,
       ', sua nota em Estrutura é:  ' , Estrutura, '  ,   A média geral é:   ' , media)
