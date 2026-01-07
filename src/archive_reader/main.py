import zipfile
import pathlib

# ---- entrada do caminho ----
caminho = input ("qual o caminho do arquivo?").strip('"\'')
caminho = pathlib.Path(caminho)

while not zipfile.is_zipfile(caminho):
   caminho = input("Arquivo invalido. Insira o caminho do arquivo: ")
   caminho = pathlib.Path(caminho)

# ---- leitura do conteudo  do zip ----
with zipfile.ZipFile(caminho, "r")  as zip_file:
   for item in zip_file.infolist():
      nome = item.filename
      tamanho = item.file_size
      tipo = "PASTA" if item.is_dir() else "ARQUIVO"
      print(f"{tipo}, {nome}, {tamanho} bytes")

# ---- escolha do local de extração ---- 

   escolha = input("Escolha o caminho da extração (1) ou se vai criar uma nova pasta (2): ")

   while escolha != "1" and escolha != "2":
      escolha = input("Entrada invalida, escolha um numero entre 1 e 2")

   if escolha == "1":
      destino = input (" escreva caminho desejado: ").strip('"\'')
      destino = pathlib.Path(destino)
   else:
      destino =caminho.parent / caminho.stem
      destino.mkdir(exist_ok=True)

   zip_file.extractall(destino)
