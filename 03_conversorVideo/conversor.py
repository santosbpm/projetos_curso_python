import os, fnmatch 

comand_ffmeg = 'ffmpeg'
codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'


def converter(origem, destino, termo):
    for raiz, diretorios, arquivos in os.walk(origem):
        for arquivo in arquivos:
            if termo in arquivo and fnmatch.fnmatch(arquivo, '*mkv'):
                try: 
                    caminho_completo = os.path.join(raiz, arquivo)
                    arquivo_saida = f'{destino}/{arquivo}'
                    comando = f'{comand_ffmeg} -i "{caminho_completo}" {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} "{arquivo_saida}"' 
                    
                    os.system(comando)

                except PermissionError:
                    print('Sem permissão!')
                except FileNotFoundError:
                    print('Arquivo não encontrado.')
                except Exception:
                    print('Erro desconhecido!')

