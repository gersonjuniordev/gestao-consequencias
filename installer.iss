; Script do instalador - Sistema de Gestão de Consequências

[Setup]
AppName=Sistema de Gestão de Consequências
AppVersion=1.0
DefaultDirName={autopf}\Sistema de Gestao
DefaultGroupName=Sistema de Gestão
OutputDir=C:\Users\Gerson\gestao-projeto\installer
OutputBaseFilename=Sistema_Gestao_Setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
WizardStyle=modern
DisableDirPage=no
DisableProgramGroupPage=no
UninstallDisplayIcon={app}\Sistema de Gestao.exe

; Configurações em português
LanguageDetectionMethod=locale
ShowLanguageDialog=no

[Languages]
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Files]
; Arquivos do executável
Source: "C:\Users\Gerson\gestao-projeto\dist\Sistema de Gestao\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; Pasta data
Source: "C:\Users\Gerson\gestao-projeto\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs

[Dirs]
Name: "{app}\data"; Permissions: users-modify

[Icons]
Name: "{group}\Sistema de Gestão"; Filename: "{app}\Sistema de Gestao.exe"; WorkingDir: "{app}"
Name: "{commondesktop}\Sistema de Gestão"; Filename: "{app}\Sistema de Gestao.exe"; WorkingDir: "{app}"

[Run]
; Iniciar o programa após a instalação
Filename: "{app}\Sistema de Gestao.exe"; Description: "Iniciar Sistema de Gestão"; Flags: postinstall nowait shellexec

[UninstallDelete]
Type: filesandordirs; Name: "{app}"

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
var
  ResultCode: Integer;
begin
  if CurStep = ssPostInstall then
  begin
    // Ajustar permissões
    Exec('cmd.exe', Format('/c icacls "{app}\data" /grant Users:(OI)(CI)F /T', [ExpandConstant('{app}')]), 
         '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
  end;
end;

[Messages]
BeveledLabel=Sistema de Gestão de Consequências