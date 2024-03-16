import random
palavras1 = ['luz','fogo','ar','banco','cem','computador','sim', 'cobra','violão']
palavras2 = ['mar','teclado', 'livro', 'bacteria', 'arvore','sanba', 'viado','reguar','correndo']
palavras3 = ['matematica','palavras','leao','não','irmão','quente','frio','bebendo','pulando']
with open ('textoalea.txt', 'w') as texto:
    for a in range(1000):
        n1 = random.randint(0,8)
        n2 = random.randint(0,8)
        n3 = random.randint(0,8)
        print(n1,n2,n3)
        if n3 >3:
            texto.write(f'{palavras1[n3]} {palavras2[n2]} {palavras3[n1]} ')
        else : 
            texto.write(f'{palavras1[n3]} {palavras2[n2]} {palavras3[n1]}\n')