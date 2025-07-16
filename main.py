from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('8048227682:AAFn3P-SDO_60fuaX2nHVJC41Rm41HHTlbE')
CHAT_ID = os.environ.get('5850221453')

def send_sniper_alert(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    res = requests.post(url, data=data)
    return res.status_code

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        msg = f"📡 SNIPER ALERT:\n{data['message']}"
        status = send_sniper_alert(msg)
        return {'status': 'sent', 'code': status}, 200
    return {'status': 'failed'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
