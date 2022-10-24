from conversor import converter

caminho_origem = '/home/santosbpm/Vídeos/Teste/'
caminho_destino = '/home/santosbpm/Documentos/projetos_curso_python/03_conversorVideo/arquivos_convertidos/'
termo = 'teste'

if __name__ == "__main__":
    converter(caminho_origem, caminho_destino, termo)
