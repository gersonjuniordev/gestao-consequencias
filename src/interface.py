import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import datetime
from database import GestaoDatabase
from relatorios import GeradorRelatorios
from tksheet import Sheet
import os

class GestaoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Gestão de Consequências")
        self.geometry("1200x800")
        
        # Configurações de tema
        self.configure(fg_color="#f0f0f0")
        ctk.set_appearance_mode("light")
        
        self.db = GestaoDatabase()
        self.gerador_relatorios = GeradorRelatorios()
        
        self.criar_widgets()
        self.atualizar_tabela()

    def criar_widgets(self):
        # Frame principal com dois painéis
        self.frame_principal = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Painel esquerdo para entrada de dados
        self.painel_entrada = ctk.CTkFrame(self.frame_principal, corner_radius=15)
        self.painel_entrada.pack(side="left", fill="y", padx=(0, 10))
        
        # Título do formulário
        titulo = ctk.CTkLabel(self.painel_entrada, 
                            text="Registro de Gestão",
                            font=("Roboto", 20, "bold"))
        titulo.pack(pady=20)
        
        self.criar_campos_entrada()
        self.criar_botoes()
        
        # Painel direito para tabela
        self.painel_tabela = ctk.CTkFrame(self.frame_principal, corner_radius=15)
        self.painel_tabela.pack(side="right", fill="both", expand=True)
        
        # Título da tabela
        titulo_tabela = ctk.CTkLabel(self.painel_tabela,
                                   text="Registros de Gestão",
                                   font=("Roboto", 20, "bold"))
        titulo_tabela.pack(pady=20)
        
        self.criar_tabela()

    def criar_campos_entrada(self):
        campos_frame = ctk.CTkFrame(self.painel_entrada, fg_color="transparent")
        campos_frame.pack(fill="x", padx=20, pady=10)

        # Colaborador
        ctk.CTkLabel(campos_frame, text="Colaborador:").pack(anchor="w")
        self.entry_colaborador = ctk.CTkEntry(campos_frame, width=300)
        self.entry_colaborador.pack(pady=(0, 10))

        # Data
        ctk.CTkLabel(campos_frame, text="Data:").pack(anchor="w")
        self.entry_data = DateEntry(campos_frame, width=12, background='darkblue',
                                  foreground='white', borderwidth=2,
                                  date_pattern='dd/mm/yyyy',  # Formato brasileiro
                                  locale='pt_BR')  # Localização brasileira
        self.entry_data.pack(pady=(0, 10), anchor="w")

        # Hora
        ctk.CTkLabel(campos_frame, text="Hora:").pack(anchor="w")
        self.entry_hora = ctk.CTkEntry(campos_frame, width=300, 
                                     placeholder_text="HH:MM")
        self.entry_hora.pack(pady=(0, 10))

        # Tipo de Advertência
        ctk.CTkLabel(campos_frame, text="Tipo:").pack(anchor="w")
        self.combo_tipo = ctk.CTkOptionMenu(campos_frame,
                                          values=["Orientação Escrita", 
                                                 "Advertência Verbal",
                                                 "Advertência Escrita", 
                                                 "Suspensão", 
                                                 "Justa Causa"],
                                          width=300)
        self.combo_tipo.pack(pady=(0, 10))

        # Motivo
        ctk.CTkLabel(campos_frame, text="Motivo:").pack(anchor="w")
        self.entry_motivo = ctk.CTkEntry(campos_frame, width=300)
        self.entry_motivo.pack(pady=(0, 10))

        # Descrição
        ctk.CTkLabel(campos_frame, text="Descrição:").pack(anchor="w")
        self.text_descricao = ctk.CTkTextbox(campos_frame, width=300, height=100)
        self.text_descricao.pack(pady=(0, 10))

        # Quantidade
        ctk.CTkLabel(campos_frame, text="Quantidade de Alertas:").pack(anchor="w")
        self.entry_quantidade = ctk.CTkEntry(campos_frame, width=300)
        self.entry_quantidade.insert(0, "1")  # Valor padrão
        self.entry_quantidade.pack(pady=(0, 10))

    def criar_botoes(self):
        frame_botoes = ctk.CTkFrame(self.painel_entrada, fg_color="transparent")
        frame_botoes.pack(fill="x", padx=20, pady=20)

        # Botão Salvar
        self.btn_salvar = ctk.CTkButton(frame_botoes, 
                                       text="Salvar",
                                       command=self.salvar_gestao,
                                       fg_color="#28a745",
                                       hover_color="#218838")
        self.btn_salvar.pack(fill="x", pady=(0, 5))

        # Botão Relatório Excel
        self.btn_excel = ctk.CTkButton(frame_botoes, 
                                      text="Gerar Excel",
                                      command=self.gerar_excel,
                                      fg_color="#007bff",
                                      hover_color="#0056b3")
        self.btn_excel.pack(fill="x", pady=5)

        # Botão Relatório PDF
        self.btn_pdf = ctk.CTkButton(frame_botoes, 
                                    text="Gerar PDF",
                                    command=self.gerar_pdf,
                                    fg_color="#dc3545",
                                    hover_color="#c82333")
        self.btn_pdf.pack(fill="x", pady=5)

    def criar_tabela(self):
        # Frame para a tabela
        self.frame_tabela = ctk.CTkFrame(self.painel_tabela, fg_color="transparent")
        self.frame_tabela.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Frame para botões de ação da tabela
        self.frame_acoes = ctk.CTkFrame(self.frame_tabela, fg_color="transparent")
        self.frame_acoes.pack(fill="x", pady=(0, 10))

        # Botão Excluir
        self.btn_excluir = ctk.CTkButton(self.frame_acoes, 
                                        text="Excluir Selecionado",
                                        command=self.excluir_gestao,
                                        fg_color="#dc3545",
                                        hover_color="#c82333",
                                        width=200)
        self.btn_excluir.pack(side="left", padx=5)

        # Criar tabela usando tksheet
        self.sheet = Sheet(self.frame_tabela,
                          headers=['ID', 'Colaborador', 'Data', 'Hora',
                                 'Tipo', 'Motivo', 'Descrição', 'Quantidade'],
                          theme="light blue",
                          show_x_scrollbar=False,
                          height=400)
        self.sheet.pack(fill="both", expand=True)
        
        # Configurar colunas
        self.sheet.headers(['ID', 'Colaborador', 'Data', 'Hora',
                          'Tipo', 'Motivo', 'Descrição', 'Quantidade'])
        self.sheet.column_width(column=0, width=50)
        self.sheet.column_width(column=1, width=150)
        self.sheet.column_width(column=2, width=100)
        self.sheet.column_width(column=3, width=80)
        self.sheet.column_width(column=4, width=120)
        self.sheet.column_width(column=5, width=150)
        self.sheet.column_width(column=6, width=200)
        self.sheet.column_width(column=7, width=80)  # Coluna de quantidade
        
        # Habilitar seleção de linhas
        self.sheet.enable_bindings("single_select")

    def atualizar_tabela(self):
        # Buscar dados do banco
        registros = self.db.buscar_gestoes()
        
        # Preparar dados para a tabela
        dados_tabela = []
        for registro in registros:
            # Converter a data do formato do banco para o formato brasileiro
            data_banco = datetime.strptime(registro[2], "%Y-%m-%d")
            data_br = data_banco.strftime("%d/%m/%Y")
            
            dados_tabela.append([
                registro[0],  # ID
                registro[1],  # Colaborador
                data_br,      # Data (formato brasileiro)
                registro[3],  # Hora
                registro[4],  # Tipo
                registro[5],  # Motivo
                registro[6],  # Descrição
                registro[7]   # Quantidade
            ])
        
        # Atualizar dados na tabela
        self.sheet.set_sheet_data(data=dados_tabela)

    def salvar_gestao(self):
        try:
            colaborador = self.entry_colaborador.get()
            # Converter a data do formato brasileiro para o formato do banco
            data_br = self.entry_data.get()  # Obtém no formato dd/mm/yyyy
            data_obj = datetime.strptime(data_br, "%d/%m/%Y")
            data = data_obj.strftime("%Y-%m-%d")  # Converte para formato do banco
            
            hora = self.entry_hora.get()
            tipo = self.combo_tipo.get()
            motivo = self.entry_motivo.get()
            descricao = self.text_descricao.get("1.0", "end-1c")
            
            # Obter quantidade (com validação)
            try:
                quantidade = int(self.entry_quantidade.get())
                if quantidade < 1:
                    raise ValueError("A quantidade deve ser maior que zero")
            except ValueError as e:
                self.mostrar_mensagem("Erro", "Quantidade inválida. Use apenas números maiores que zero.")
                return

            self.db.adicionar_gestao(colaborador, data, hora, tipo, motivo, descricao, quantidade)
            self.atualizar_tabela()
            self.limpar_campos()
            
            self.mostrar_mensagem("Sucesso", "Registro salvo com sucesso!")
            
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Erro ao salvar: {str(e)}")

    def limpar_campos(self):
        self.entry_colaborador.delete(0, "end")
        self.entry_hora.delete(0, "end")
        self.entry_motivo.delete(0, "end")
        self.text_descricao.delete("1.0", "end")
        self.entry_quantidade.delete(0, "end")
        self.entry_quantidade.insert(0, "1")  # Resetar para valor padrão
        self.combo_tipo.set("Orientação Escrita")

    def mostrar_mensagem(self, titulo, mensagem):
        dialog = ctk.CTkInputDialog(text=mensagem, title=titulo)
        dialog.geometry("300x150")
        if titulo == "Aviso" or titulo == "Erro":
            dialog.configure(fg_color="#dc3545")
        elif titulo == "Sucesso":
            dialog.configure(fg_color="#28a745")

    def gerar_excel(self):
        try:
            caminho = os.path.join(os.path.expanduser("~"), "Desktop", 
                                 f"gestao_consequencias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
            dados = self.db.buscar_gestoes()
            self.gerador_relatorios.gerar_excel(dados, caminho)
            self.mostrar_mensagem("Sucesso", f"Relatório Excel gerado em:\n{caminho}")
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Erro ao gerar Excel: {str(e)}")

    def gerar_pdf(self):
        try:
            caminho = os.path.join(os.path.expanduser("~"), "Desktop", 
                                 f"gestao_consequencias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
            dados = self.db.buscar_gestoes()
            self.gerador_relatorios.gerar_pdf(dados, caminho)
            self.mostrar_mensagem("Sucesso", f"Relatório PDF gerado em:\n{caminho}")
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Erro ao gerar PDF: {str(e)}")

    def excluir_gestao(self):
        try:
            # Obter a linha selecionada
            selecao = self.sheet.get_currently_selected()
            if not selecao:
                self.mostrar_mensagem("Aviso", "Por favor, selecione um registro para excluir.")
                return
            
            # Obter o ID do registro selecionado
            linha_selecionada = selecao.row
            id_gestao = self.sheet.get_cell_data(linha_selecionada, 0)
            
            # Confirmar exclusão
            dialog = ctk.CTkInputDialog(text=f"Tem certeza que deseja excluir o registro {id_gestao}?\n\nDigite 'CONFIRMAR' para excluir:", 
                                      title="Confirmar Exclusão")
            resposta = dialog.get_input()
            
            if resposta == "CONFIRMAR":
                # Excluir do banco de dados
                self.db.excluir_gestao(id_gestao)
                
                # Atualizar a tabela
                self.atualizar_tabela()
                
                self.mostrar_mensagem("Sucesso", "Registro excluído com sucesso!")
            else:
                self.mostrar_mensagem("Aviso", "Exclusão cancelada.")
                
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Erro ao excluir: {str(e)}") 