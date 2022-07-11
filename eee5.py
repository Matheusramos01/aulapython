#crie dois vetores com nome e notas de 4 alunos
# mostre o nome e a nota dos alunos acima da médias da turma
nomes = ['Ana', 'Pedro', 'José', 'Maria']
notas = [9.0,8.0,7.0,6.0]
#média da turma
soma = 0
for nota in notas:
    soma += nota
media = soma/len(notas)
print('Média da turma:', media)
for i in range (len(notas)):
    if notas [i]> media:
        print('Aluno(os) com nota acima da média:', nomes[i], "Nota:", notas[i])    
