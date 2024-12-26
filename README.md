SISTEMA DE GESTÃO DE CONSEQUÊNCIAS
================================

DESCRIÇÃO
---------
Sistema para gerenciamento de advertências e outras medidas disciplinares em ambiente empresarial.

FUNCIONALIDADES
--------------
* Registro de gestões disciplinares
* Tipos de gestão:
  - Orientação Escrita
  - Advertência Verbal
  - Advertência Escrita
  - Suspensão
  - Justa Causa
* Controle por colaborador
* Geração de relatórios em Excel e PDF
* Interface gráfica intuitiva
* Banco de dados local SQLite

REQUISITOS DO SISTEMA
--------------------
* Windows 7 ou superior
* 500MB de espaço em disco
* 2GB de RAM (recomendado)
* Privilégios de administrador para instalação

ESTRUTURA DO PROJETO
-------------------
gestao-projeto/
|
+-- assets/            (Recursos - ícones, imagens)
+-- src/              (Código fonte)
|   +-- main.py       (Ponto de entrada)
|   +-- interface.py  (Interface gráfica)
|   +-- database.py   (Gerenciamento do banco)
|   +-- relatorios.py (Geração de relatórios)
|
+-- data/             (Banco de dados)
+-- dist/             (Executável compilado)
+-- build/            (Arquivos de build)
+-- installer/        (Instalador compilado)
+-- venv/             (Ambiente virtual Python)

INSTALAÇÃO PARA DESENVOLVIMENTO
-----------------------------
1. Clone o repositório
2. Crie ambiente virtual:
   python -m venv venv
3. Ative o ambiente:
   .\venv\Scripts\activate
4. Instale dependências:
   pip install -r requirements.txt

COMPILAÇÃO
----------
1. Gerar executável:
   python build_exe.py
2. Compilar instalador:
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss

INSTALAÇÃO PARA USUÁRIO FINAL
----------------------------
1. Execute Sistema_Gestao_Setup.exe
2. Siga as instruções do instalador
3. O sistema iniciará automaticamente

BACKUP
------
Localização do banco de dados:
[Pasta de Instalação]\data\gestao.db

Recomenda-se fazer backup regular deste arquivo.

SOLUÇÃO DE PROBLEMAS
-------------------
1. Verifique permissões de administrador
2. Verifique se o antivírus está bloqueando
3. Confirme espaço em disco disponível
4. Verifique logs em:
   [Pasta de Instalação]\logs\

DESENVOLVIDO POR
---------------
Gerson Junior
Contato: (31) 97246-6905

SUPORTE TÉCNICO
--------------
Em caso de problemas técnicos:
1. Verifique a documentação acima
2. Entre em contato com o desenvolvedor

COPYRIGHT
---------
Copyright © 2024 - Todos os direitos reservados

NOTAS DE VERSÃO
--------------
Versão 1.0
- Lançamento inicial
- Sistema completo de gestão de consequências
- Geração de relatórios em Excel e PDF
- Interface gráfica intuitiva 