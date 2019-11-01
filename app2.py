import json
import time
import numpy as np
from datetime import datetime
from flask import Flask, render_template, Response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index2.html')


@app.route('/chart-data')
def chart_data():
    def generador_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'value': np.random.rand()}
            )
            yield f"data:{json_data}\n\n"
            time.sleep(1)
    return Response(generador_random_data(),mimetype='text/event-stream')
    #return render_template('index2.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
 