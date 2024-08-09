from flask import Flask, jsonify

app = Flask(__name__)

# Root endpoint
@app.route('/')
def hello():
    return "Hello, World! This is the Flask app running on EC2."

# Health check endpoint
@app.route('/health')
def health_check():
    response = {
        "status": "healthy"
    }
    return jsonify(response), 200

# Another example endpoint
@app.route('/api/data')
def get_data():
    data = {
        "message": "Here is some data from the Flask API!"
    }
    return jsonify(data)

if __name__ == "__main__":
    # Make sure to listen on all IP addresses and use port 80
    app.run(host='0.0.0.0', port=80)