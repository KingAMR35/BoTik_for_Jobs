from AI_service import *
from dotenv import load_dotenv

import sqlite3

DATABASE = ('survey.db')

class DB_service():

    def __init__(self, database):
        self.database = database



    def create_table_if_not_exists(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS survey_data (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def add_survey_entry(self, chat_id, question, answer):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            self.cursor.execute(
            "INSERT INTO survey_data (chat_id, question, answer) VALUES (?, ?, ?)",
            (chat_id, question, answer)
            )
            self.conn.commit()

    def close_connection(self):
        self.conn.close()


