from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('8048227682:AAFn3P-SDO_60fuaX2nHVJC41Rm41HHTlbE')
CHAT_ID = os.environ.get('5850221453')

def send_sniper_alert(message):
    if not BOT_TOKEN or not CHAT_ID:
        return {'error': 'Missing BOT_TOKEN or CHAT_ID in environment variables'}, 500

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=data)

    # Log the response from Telegram for debugging
    print("Telegram API Response:", response.text)

    if response.status_code == 200:
        return {'status': 'success', 'telegram_response': response.text}, 200
    else:
        return {'status': 'failed', 'telegram_response': response.text}, 500

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        msg = f"📡 SNIPER ALERT:\n{data['message']}"
        return send_sniper_alert(msg)
    return {'status': 'failed', 'error': 'No message found in payload'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
