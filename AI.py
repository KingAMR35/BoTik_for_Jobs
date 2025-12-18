import base64
from gigachat import GigaChat
import telebot
import sqlite3
from config import *


encoded_credentials = base64.b64encode(credentials.encode()).decode()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class MyTelegramBot2:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

        QUESTIONS = [
            "Какие виды деятельности приносят вам наибольшее удовольствие?",
            "Назовите вашу самую сильную сторону или талант.",
            "Хотите ли вы работать на себя или предпочитаете трудиться в коллективе?",
            "Каковы ваши ожидания по зарплате?",
            "Любите ли вы постоянные изменения и творческий подход или предпочитаете стабильность и привычность?"
        ]

        self.states = {}
        self.responses = {}

        @self.bot.message_handler(commands=['job_AIsearch'])
        def start(message):
            self.bot.send_message(message.chat.id, "Привет! Давайте пройдем небольшую анкету, чтобы подобрать вам подходящую профессию.\n\n" +
                                                  QUESTIONS[0])
            self.states[message.chat.id] = 0

        @self.bot.message_handler(func=lambda m: True)
        def collect_user_input(message):
            state = self.states.get(message.chat.id)
            if state is None:
                self.bot.send_message(message.chat.id, "Вам нужно начать заново, отправьте /job_AIsearch")
                return
                                                                            #написал код для ии поиска теперь буду заносить информацию о пользователе в базу данных
            if state == 0:
                self.responses[message.chat.id] = {"activity_preference": message.text}
            elif state == 1:
                self.responses[message.chat.id]["strengths"] = message.text
            elif state == 2:
                self.responses[message.chat.id]["work_style"] = message.text
            elif state == 3:
                self.responses[message.chat.id]["salary_expectation"] = message.text
            elif state == 4:
                self.responses[message.chat.id]["change_vs_stability"] = message.text

            next_state = state + 1
            if next_state >= len(QUESTIONS):
                self.predict_profession(message.chat.id)
                del self.states[message.chat.id]
            else:
                self.bot.send_message(message.chat.id, QUESTIONS[next_state])
                self.states[message.chat.id] = next_state

    def predict_profession(self, user_id):
        prompt = f"""
        Answered Questions:
        Activity Preference: {self.responses[user_id]['activity_preference']}
        Strengths: {self.responses[user_id]['strengths']}
        Work Style: {self.responses[user_id]['work_style']}
        Salary Expectation: {self.responses[user_id]['salary_expectation']}
        Change vs Stability: {self.responses[user_id]['change_vs_stability']}

        Учитывая эти предпочтения, пожалуйста, предложите одну или две наиболее подходящие профессии.
        """

        with GigaChat(credentials=encoded_credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(prompt)
            predicted_profession = response.choices[0].message.content.strip()

        self.bot.send_message(user_id, f"Ваша рекомендуемая профессия: {predicted_profession}")

    def run_bot(self):
        print("Бот запущен :)")
        self.bot.polling(none_stop=True)