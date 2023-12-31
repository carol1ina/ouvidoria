from operacoesbd import *
opcao = 1
manifestacoes = []
conexao = abrirBancoDados('localhost','root','12345','ouvidoria1')
#cod menu
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
# cod listar
    if opcao == 1:
        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        print('Listagem de manifestações:')
        consultaListagem = 'select * from manifestacao'
        manifestacoes = listarBancoDados(conexao,consultaListagem)
        if len(manifestacoes) > 0:
            for manifestacao in manifestacoes:
                print('Código', manifestacao[0], '-', manifestacao[1], '-', manifestacao[3], '-', manifestacao [5] )
        else:
            print('Nenhuma manifestação encontrada.')
        conexao.close()
#cod listar por tipo
    elif opcao == 2:
        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        def listarManifestacoesPorTipo(conexao):
            print('')
            manifestacao = input(
                'Digite o tipo de manifestação que deseja listar:\n [1] Reclamação  [2] Elogio  [3] Sugestão): ')

            if manifestacao.lower() not in ['1', '2', '3']:
                print('Tipo de manifestação inválido.')
                exit()

            cursor = conexao.cursor()

            sqlListagem = 'select * from manifestacao where tipo = %s'

            if manifestacao.lower() == 'reclamacao':
                tipo = 'reclamacao'
            elif manifestacao.lower() == 'elogio':
                tipo = 'elogio'
            else:
                tipo = 'sugestao'

            valores = (tipo,)
            cursor.execute(sqlListagem, valores)
            manifestacoes = cursor.fetchall()

            if len(manifestacoes) > 0:
                print(f'Listagem das Manifestacoes do tipo {manifestacao.capitalize()}:\n')
                for manifestacao in manifestacoes:
                    codigo = manifestacao[0]
                    titulo = manifestacao[1]
                    autor = manifestacao[3]
                    print(f'• Código {codigo} – {titulo} – {autor}')
            else:
                print(f'Não há manifestações do tipo {manifestacao.capitalize()}.')
            cursor.close()
        listarManifestacoesPorTipo(conexao)
        conexao.close()
    elif opcao == 3:
        print('')
        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        titulo = input('Digite o título da manifestação: ')
        detalhe = input('Digite a descrição da manifestação: ')
        autor = input('Digite o nome do reclamante: ')
        data = input('Digite a data da reclamação: ')
        tipo = input('Digite o tipo da manifestação (reclamação, sugestão ou elogio): ')

        sqlInsercao = 'insert into manifestacao (titulo, detalhe, autor, data, tipo) values (%s, %s, %s, %s, %s)'
        valores = (titulo, detalhe, autor, data, tipo)
        insertNoBancoDados(conexao, sqlInsercao, valores)
        print('Manifestação criada com sucesso!')
        encerrarBancoDados(conexao)
    elif opcao == 4:
        import mysql.connector

        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        def obterQuantidadeManifestacoes(conexao):
            sql = """
                SELECT 
                    COUNT(*) as quantidade,
                    Tipo
                FROM 
                    manifestacao
                GROUP BY 
                    Tipo
            """
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        def exibirQuantidadeManifestacoes(resultados):
            print("Quantidade de Manifestações:")
            total_manifestacoes = 0
            for resultado in resultados:
                tipo = resultado['Tipo']
                quantidade = resultado['quantidade']
                print(f"Quantidade de {tipo.capitalize()}: {quantidade}")
                total_manifestacoes += int(quantidade)
            print(f"Total de Manifestações: {total_manifestacoes}\n")
        resultados = obterQuantidadeManifestacoes(conexao)
        exibirQuantidadeManifestacoes(resultados)
        conexao.close()
    elif opcao == 5:
        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        codigo = input('Digite o código da reclamação: ')
        consultaListagem = 'SELECT * FROM manifestacao WHERE codigo = ' + codigo
        manifestacoes = listarBancoDados(conexao, consultaListagem)
        if len(manifestacoes) > 0:
            for manifestacao in manifestacoes:
                print('Código:', manifestacao[0])
                print('Titulo:', manifestacao[1])
                print('Descrição:', manifestacao[2])
                print('Autor:', manifestacao[3])
                print('Data:', manifestacao[4])
        else:
            print('Nenhuma manifestação encontrada com o código fornecido.')
        conexao.close()
    elif opcao == 6:
        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        codigo = input('Digite o código: ')
        novoTitulo = input('Digite o novo título: ')
        novadetalhe = input('Digite a nova descrição: ')
        sqlAtualizar = 'update manifestacao set titulo = %s, detalhe = %s where codigo = %s'
        valores = (novoTitulo, novadetalhe, codigo)
        print('Manifestação alterada com sucesso!')
        atualizarBancoDados(conexao, sqlAtualizar, valores)
        encerrarBancoDados(conexao)

    elif opcao == 7:
        conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria1')
        def excluirManifestacao(conexao):
            codigo = input("Digite o código da manifestação que deseja excluir: ")
            cursor = conexao.cursor()
            sqlExclusao = "delete from manifestacao where Codigo = %s"
            valores = (codigo,)
            cursor.execute(sqlExclusao, valores)
            conexao.commit()
            if cursor.rowcount > 0:
                print("Manifestação excluída com sucesso!")
            else:
                print("Manifestação não encontrada!")
            cursor.close()
        excluirManifestacao(conexao)
        encerrarBancoDados(conexao)
print('Obrigado pelo feedback.')
print('saindo do sistema')
