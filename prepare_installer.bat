@echo off
echo Preparando arquivos para o instalador...

REM Criar diretórios necessários
mkdir instalador_files 2>nul
mkdir instalador_files\python-3.11.8-embed-amd64 2>nul

REM Baixar Python embarcado se não existir
if not exist "instalador_files\python-embedded.zip" (
    echo Baixando Python embarcado...
    curl -L "https://www.python.org/ftp/python/3.11.8/python-3.11.8-embed-amd64.zip" -o "instalador_files\python-embedded.zip"
)

REM Extrair Python embarcado
echo Extraindo Python...
powershell -command "Expand-Archive -Path 'instalador_files\python-embedded.zip' -DestinationPath 'instalador_files\python-3.11.8-embed-amd64' -Force"

REM Baixar get-pip.py
echo Baixando get-pip.py...
curl -L "https://bootstrap.pypa.io/get-pip.py" -o "instalador_files\python-3.11.8-embed-amd64\get-pip.py"

REM Modificar python311._pth para habilitar site-packages
echo Configurando Python...
(
echo python311.zip
echo .
echo import site
) > "instalador_files\python-3.11.8-embed-amd64\python311._pth"

REM Instalar pip no Python embarcado
echo Instalando pip...
"instalador_files\python-3.11.8-embed-amd64\python.exe" "instalador_files\python-3.11.8-embed-amd64\get-pip.py" --no-warn-script-location

REM Instalar dependências no Python embarcado
echo Instalando dependências...
"instalador_files\python-3.11.8-embed-amd64\python.exe" -m pip install --no-warn-script-location -r requirements.txt

echo.
echo Arquivos preparados com sucesso!
echo Agora você pode compilar o installer.iss
pause 