import json
import logging
import os
import urllib
from flask import Flask, render_template, request, url_for, send_file
from werkzeug.utils import redirect
import requests
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
#
# sentry_sdk.init(
#     dsn="https://edd4e417467e4b06981d6ac08f52f8f8@o433362.ingest.sentry.io/5388300",
#     integrations=[FlaskIntegration()],
#     send_default_pii=True,
#     request_bodies="always"
# )

app = Flask(__name__)

@app.route("/")
def home():
    app.logger.info("logging log")
    return 'Hello, World'

@app.route('/loaderio-b32166ec8e8a73c17593f059c9f887ca.txt')
def verify_load_test():
    return send_file('loaderio.txt')


@app.route('/lead', methods=['POST'])
def lead():
    print("Lead webhook")
    logging.warn("Lead webhookm warn")

    logging.warn(str(request.data))
    j = request.json
    data = json.loads(j["data.json"])

    student = data["nome_do_aluno"][0]
    student_first_name = student.split()[0].lower().capitalize()
    student_age = data["age"][0]

    parent = data['nome'][0]
    parent_first_name = parent.split()[0].lower().capitalize()
    phone = "55" + data['telefone_com_ddd'][0]

    text = f'''Oi {parent_first_name}! Somos da Build, uma escola de programação para adolescentes! 🖥️

Recebemos o cadastro do(a) {student_first_name} e vamos estar te ajudando nessa jornada! 😁

O próximo passo é informar sua disponibilidade nesse site aqui pra marcarmos a aula do seu filho(a):
https://bit.ly/AulasDeProgramacao

E para mais informações sobre o curso, basta acessar:
https://www.aulasdeprogramacao.com.br

Qualquer dúvida, pode me chamar!'''
    text = urllib.parse.quote(text)
    whats_link = "https://wa.me/" + phone
    whats_link_intro = whats_link + "?text=" + text

    description = f"Um novo cadastro foi feito!"

    url = os.getenv('SLACK_MKT_WEBHOOK', "")
    if url == "":
        print("No webhook supplied")
    res = requests.post(url, json={
        'text': description,
        'blocks': [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": description
                }
            },
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Contexto",
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Responsável*: {parent}"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Aluno*: {student}"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Idade*: {student_age}"
                    }
                ]
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"<{whats_link_intro}|Iniciar Conversa>\n"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"<{whats_link}|Ver mensagens>\n"
                }
            },
        ]
    })
    print(res)
    return ''

