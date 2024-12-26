import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import datetime

class GeradorRelatorios:
    def __init__(self):
        pass

    def gerar_excel(self, dados, caminho):
        # Converter os dados para o formato brasileiro
        dados_formatados = []
        for registro in dados:
            data_banco = datetime.strptime(registro[2], "%Y-%m-%d")
            data_br = data_banco.strftime("%d/%m/%Y")
            
            dados_formatados.append([
                registro[0],  # ID
                registro[1],  # Colaborador
                data_br,      # Data (formato brasileiro)
                registro[3],  # Hora
                registro[4],  # Tipo
                registro[5],  # Motivo
                registro[6],  # Descrição
                registro[7],  # Quantidade
                registro[8]   # Criado em
            ])
            
        df = pd.DataFrame(dados_formatados, 
                         columns=['ID', 'Colaborador', 'Data', 'Hora',
                                'Tipo', 'Motivo', 'Descrição', 'Quantidade', 'Criado em'])
        df.to_excel(caminho, index=False)

    def gerar_pdf(self, dados, caminho):
        doc = SimpleDocTemplate(caminho, pagesize=letter)
        elementos = []

        # Converter dados para formato adequado com data brasileira
        dados_tabela = [['Colaborador', 'Data', 'Tipo', 'Motivo', 'Quantidade']]
        for registro in dados:
            data_banco = datetime.strptime(registro[2], "%Y-%m-%d")
            data_br = data_banco.strftime("%d/%m/%Y")
            
            dados_tabela.append([
                registro[1],  # Colaborador
                data_br,      # Data (formato brasileiro)
                registro[4],  # Tipo
                registro[5],  # Motivo
                str(registro[7])  # Quantidade
            ])

        # Criar tabela
        tabela = Table(dados_tabela)
        tabela.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        elementos.append(tabela)
        doc.build(elementos) 