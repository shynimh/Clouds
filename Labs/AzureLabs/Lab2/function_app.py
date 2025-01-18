import azure.functions as func
import logging
import math
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def numerical_integration(lower, upper, N):
    delta_x = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * delta_x
        total_area += abs(math.sin(x)) * delta_x
    return total_area

@app.route(route="integrate", methods=['GET'])
def numintfunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        lower = float(req.params.get('lower'))
        upper = float(req.params.get('upper'))

        N_values = [10, 100, 1000, 10000, 100000, 1000000]
        results = {}

        for N in N_values:
            result = numerical_integration(lower, upper, N)
            results[N] = result

        return func.HttpResponse(
            json.dumps(results),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(
            f"Error: {str(e)}",
            status_code=400
        )