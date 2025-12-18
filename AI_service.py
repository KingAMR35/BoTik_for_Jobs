# ai_service.py
import base64
from gigachat import GigaChat
import os
from dotenv import load_dotenv

load_dotenv()
b = os.getenv("CREDENTIALS")
encoded_credentials = base64.b64encode(b.encode()).decode()

class MyTelegramBot2:
    def __init__(self):
        # Список вопросов анкеты
        self.QUESTIONS = [
            "Какие виды деятельности приносят вам наибольшее удовольствие?",
            "Назовите вашу самую сильную сторону или талант.",
            "Хотите ли вы работать на себя или предпочитаете трудиться в коллективе?",
            "Каковы ваши ожидания по зарплате?",
            "Любите ли вы постоянные изменения и творческий подход или предпочитаете стабильность и привычность?"
        ]

    def predict_profession(self, answers):
        prompt = f"""
        Answered Questions:
        Activity Preference: {answers['activity_preference']}
        Strengths: {answers['strengths']}
        Work Style: {answers['work_style']}
        Salary Expectation: {answers['salary_expectation']}
        Change vs Stability: {answers['change_vs_stability']}

        Based on these preferences, please suggest one or two suitable professions. Please answer in Russian
        """

        with GigaChat(credentials=encoded_credentials, verify_ssl_certs=False) as giga:
            response = giga.chat(prompt)
            predicted_profession = response.choices[0].message.content.strip()

        return predicted_profession