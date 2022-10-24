import os

def localiza(caminho, termo):
    for raiz, diretorios, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if termo in arquivo:
                try:
                    caminho_completo = os.path.join(raiz, arquivo)
                    nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                    tamanho = os.path.getsize(caminho_completo)

                    print()
                    print('Encontrei o arquivo:', arquivo)
                    print('Caminho:', caminho)
                    print('Nome:', nome_arquivo)
                    print('Extensão:', ext_arquivo)
                    print('Tamanho', tamanho) 
                except PermissionError:
                    print('Sem permissão!')
                except FileNotFoundError:
                    print('Arquivo não encontrado.')
                except Exception:
                    print('Erro desconhecido!')
