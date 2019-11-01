import numpy as np
import bokeh.plotting as plt
from bokeh.embed import components
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  
  x = np.linspace(0,500,100)
  y = np.sin(x)
  p = plt.figure(title= 'algo')
  p.line(x,y,line_width=2)
  script, div = components(p)
  return render_template('index.html', the_div=div, the_script=script)



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 