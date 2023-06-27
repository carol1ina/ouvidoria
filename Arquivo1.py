from operacoesbd import *
opcao = 1
manifestacoes = []
conexao = abrirBancoDados('localhost','root','12345','ouvidoria1')

while opcao != 8:
    print ()
    print('====== Bem-vindo(a) ao sistema de ouvidoria ======')
    print ()
    print('[1] Listar das manifestações')
    print('[2] Listar de manifestações por Tipo')
    print('[3] Criar uma nova manifestações')
    print('[4] Exibir quantidade de manifestações')
    print('[5] Pesquisar uma manifestação por código')
    print('[6] Alterar o título e/ou descrição de uma manifestação')
    print('[7] Excluir uma manifestação pelo Código')
    print('[8] Sair do Sistema')
    print()
    opcao = int(input('Digite a opção desejada: '))