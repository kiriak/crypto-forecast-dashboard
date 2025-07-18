from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    images = [
        "bitcoin_forecast.png",
        "ethereum_forecast.png",
        "solana_forecast.png"
    ]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8501)
