import sqlite3
from datetime import datetime
import os

class GestaoDatabase:
    def __init__(self):
        # Obtém o diretório do projeto
        projeto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Define o caminho do banco de dados
        db_path = os.path.join(projeto_dir, 'data', 'gestao.db')
        
        # Garante que o diretório data existe
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Conecta ao banco de dados
        self.conn = sqlite3.connect(db_path)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS gestoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador TEXT NOT NULL,
            data DATE NOT NULL,
            hora TIME NOT NULL,
            tipo_advertencia TEXT NOT NULL,
            motivo TEXT NOT NULL,
            descricao TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        self.conn.commit()

    def adicionar_gestao(self, colaborador, data, hora, tipo_advertencia, motivo, descricao):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO gestoes (colaborador, data, hora, tipo_advertencia, motivo, descricao)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (colaborador, data, hora, tipo_advertencia, motivo, descricao))
        self.conn.commit()

    def buscar_gestoes(self, filtros=None):
        cursor = self.conn.cursor()
        query = "SELECT * FROM gestoes"
        if filtros:
            # Implementar filtros aqui
            pass
        return cursor.execute(query).fetchall()

    def get_estatisticas(self):
        cursor = self.conn.cursor()
        return cursor.execute('''
        SELECT 
            colaborador,
            tipo_advertencia,
            COUNT(*) as total
        FROM gestoes
        GROUP BY colaborador, tipo_advertencia
        ''').fetchall()

    def excluir_gestao(self, id_gestao):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM gestoes WHERE id = ?', (id_gestao,))
        self.conn.commit() 