import os
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

DASHBOARD_API = os.getenv('DASHBOARD_API_URL', '').strip()
SALES_API = os.getenv('SALES_API_URL', '').strip()


def fetch_json(url):
    if not url:
        return {'error': 'API URL is not configured.'}
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {'error': f'Unable to load data: {e}'}


@app.get('/')
def home():
    return render_template('dashboard.html', data=fetch_json(DASHBOARD_API))


@app.get('/dashboard')
def dashboard():
    return render_template('dashboard.html', data=fetch_json(DASHBOARD_API))


@app.get('/sales-report')
def sales_report():
    return render_template('sales_report.html', data=fetch_json(SALES_API))


@app.get('/api/dashboard')
def dashboard_api():
    return jsonify(fetch_json(DASHBOARD_API))


@app.get('/api/sales-report')
def sales_report_api():
    return jsonify(fetch_json(SALES_API))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
