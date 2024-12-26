import PyInstaller.__main__
import os
import sys
import shutil

# Obtém o diretório do projeto
projeto_dir = os.path.abspath(os.path.dirname(__file__))

# Define os caminhos
icon_path = os.path.join(projeto_dir, 'assets', 'icon.ico')
main_path = os.path.join(projeto_dir, 'src', 'main.py')

# Garante que as pastas necessárias existem
os.makedirs('dist', exist_ok=True)
os.makedirs('build', exist_ok=True)

# Define os argumentos do PyInstaller
args = [
    main_path,  # Seu script principal
    '--name=Sistema de Gestao',  # Nome do executável
    '--onedir',  # Criar um diretório com o executável e dependências
    '--noconsole',  # Não mostrar console
    '--clean',  # Limpar cache antes de buildar
    '--add-data=src;src',  # Incluir arquivos do src
    '--hidden-import=babel.numbers',
    '--hidden-import=tksheet',
    '--hidden-import=customtkinter',
    '--hidden-import=tkcalendar',
    '--hidden-import=PIL',
    '--hidden-import=PIL._tkinter_finder',
    '--hidden-import=sqlite3',
    '--collect-all=customtkinter',
    '--collect-all=tksheet',
    '--collect-all=tkcalendar',
    '--collect-all=PIL',
    f'--distpath={os.path.join(projeto_dir, "dist")}',  # Pasta de saída
    f'--workpath={os.path.join(projeto_dir, "build")}',  # Pasta de trabalho
    '--noconfirm',  # Não confirmar sobrescrita
    '--add-binary=venv/Lib/site-packages/customtkinter;customtkinter',
]

try:
    print("Iniciando build do executável...")
    
    # Se o ícone existir, adiciona ao executável
    if os.path.exists(icon_path):
        print("Ícone encontrado, adicionando ao executável...")
        args.append(f'--icon={icon_path}')
    
    # Limpar diretórios anteriores
    if os.path.exists('dist'):
        print("Limpando pasta dist anterior...")
        shutil.rmtree('dist')
    if os.path.exists('build'):
        print("Limpando pasta build anterior...")
        shutil.rmtree('build')
    
    # Executar o PyInstaller
    PyInstaller.__main__.run(args)
    
    # Copiar o requirements.txt para a pasta dist
    dist_path = os.path.join(projeto_dir, 'dist', 'Sistema de Gestao')
    if os.path.exists(os.path.join(projeto_dir, 'requirements.txt')):
        print("Copiando requirements.txt...")
        shutil.copy2(
            os.path.join(projeto_dir, 'requirements.txt'),
            dist_path
        )
    
    print("\nBuild concluído com sucesso!")
    print(f"O executável está em: {dist_path}")

except Exception as e:
    print(f"\nErro durante o build: {str(e)}")
    sys.exit(1) 