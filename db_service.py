from AI_service import *
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
DATABASE = os.getenv('DATABASE')

class DB_service():
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id TEXT UNIQUE NOT NULL,
                            chat_id TEXT NOT NULL,
                            job_title TEXT DEFAULT '',
                            experience INTEGER DEFAULT 0,
                            current_state TEXT DEFAULT '')''')
            
            cur.execute('''CREATE TABLE IF NOT EXISTS questions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            question_text TEXT NOT NULL)''')
            
            cur.execute('''CREATE TABLE IF NOT EXISTS answers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id TEXT NOT NULL,
                            question_id INTEGER NOT NULL,
                            user_answer TEXT NOT NULL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    def create_user(self, user_id, chat_id, job_title='', experience=0):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO users (user_id, chat_id, job_title, experience) 
                         VALUES (?, ?, ?, ?)''', (user_id, chat_id, job_title, experience))
            conn.commit()

    def get_current_state(self, user_id):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''SELECT current_state FROM users WHERE user_id = ?''', (user_id))
            result = cur.fetchone()
            return result[0] if result else None

    def update_user_state(self, user_id, new_state):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''UPDATE users SET current_state = ? WHERE user_id = ?''', (new_state, user_id))
            conn.commit()

    def add_new_question(self, question_text):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO questions (question_text) VALUES (?)''', (question_text,))
            conn.commit()

    def bulk_add_questions(self, questions_list):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.executemany('''INSERT INTO questions (question_text) VALUES (?)''', [(q,) for q in questions_list])
            conn.commit()

    def register_answer(self, user_id, question_id, user_answer):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO answers (user_id, question_id, user_answer) 
                         VALUES (?, ?, ?)''', (user_id, question_id, user_answer))
            conn.commit()
            
    def answer_questions(self, user_id, user_answer, question_text):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO answers (user_id, question_id, user_answer) 
                         VALUES (?, ?, ?)''', (user_id, question_text, user_answer))
            conn.commit()
        
    def get_user_answers(self, user_id):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''SELECT question_id, user_answer FROM answers WHERE user_id = ?''', (user_id,))
            return cur.fetchall()
        
    def save_user_answer(self, user_id, question_id, user_answer):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.execute('''INSERT INTO answers (user_id, question_id, user_answer) 
                         VALUES (?, ?, ?)''', (user_id, question_id, user_answer))
            conn.commit()
            
    def add_questions(self, questions):
        with sqlite3.connect(self.database) as conn:
            cur = conn.cursor()
            cur.executemany('''INSERT INTO questions (question_text) VALUES (?)''', [(q,) for q in questions])
            conn.commit()

if __name__ == '__main__':
    db = DB_service(DATABASE)
    db.create_tables()