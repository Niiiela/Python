#Criar variáveis com todas as disciplina de seu curso em seguida mostrar as notas  de cada disciplina e a soma de total das notas, por fim, calcula a média geral.





soma= 0
media = 0
Inovacao= float (input ('Qual sua nota em Inovação?  '))
Programacao = float (input('Qual sua nota em Programação?  '))
Rede= float (input ('Qual a sua nota em Rede?  '))
Informatica= float (input ('Qual sua nota em Informática?  '))
Estrutura=  float (input ('Qual sua nota em Estruta?  '))

soma = (soma + Inovacao + Programacao + Rede + Informatica + Estrutura) 
media = soma / 5 

print ('Sua nota em Inovação é:  ', Inovacao, ', sua nota em Programação é:  ', Programacao,
       ', sua  nota em Rede é:  ' , Rede, ', sua nota em Informática é:  ', Informatica,
       ', sua nota em Estrutura é:  ' , Estrutura,  ', a soma de todas as minhas disciplina é:   '  , soma,   ',  A média geral é:   ' , media)
