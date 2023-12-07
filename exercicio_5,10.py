#Modifique  o progrma anterior(programa da pagina 88) para que aceite respostas com letras maiúscula e minúscula em todas questoes.

pontos = 0
questao = 1

while questao <= 3 :
    resposta =input(f'Resposta da questão {questao}').strip().lower()
    if questao == 1 and resposta == 'b':
        pontos = pontos +1
    if questao == 2 and resposta == 'a':
        pontos = pontos+1
    if questao == 3 and resposta == 'd':
        pontos = pontos +1        
    questao += 1
print(f'o aluno fez {pontos} ponto(s)')        