from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def numerical_integration(lower, upper, N):
    delta_x = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * delta_x
        total_area += abs(math.sin(x)) * delta_x
    return total_area

@app.route('/integrate', methods=['GET'])
def integrate():
    try:
        lower = float(request.args.get('lower'))
        upper = float(request.args.get('upper'))
        N_values = [10, 100, 1000, 10000, 100000, 1000000]
        results = {}
        for N in N_values:
            result = numerical_integration(lower, upper, N)
            results[N] = result
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
