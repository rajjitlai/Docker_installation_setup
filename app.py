from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Docker Python Server!',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'python-docker-server'
    })

@app.route('/info')
def info():
    return jsonify({
        'python_version': os.sys.version,
        'hostname': os.environ.get('HOSTNAME', 'unknown'),
        'environment': os.environ.get('ENV', 'development')
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

