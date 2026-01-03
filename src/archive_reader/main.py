import zipfile
import pathlib

caminho = input ("qual o caminho do arquivo?").strip('"\'')
caminho = pathlib.Path(caminho)

while not zipfile.is_zipfile(caminho):
   caminho = input("Arquivo invalido. Insira o caminho do arquivo: ")

with zipfile.ZipFile(caminho, "r")  as zip_file:
   for item in zip_file.infolist():
      nome = item.filename
      tamanho = item.file_size
      tipo = "PASTA" if item.is_dir() else "ARQUIVO"

      print(f"{tipo}, {nome}, {tamanho} bytes")


