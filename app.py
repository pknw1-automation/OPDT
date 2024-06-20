from flask import Flask, request, render_template
import base64
import configparser
from urllib.parse import urlparse

app = Flask(__name__,
        static_url_path='/static',
        static_folder='web/static',
        template_folder='web/templates')

config = configparser.ConfigParser()
config.read('config.ini')



urls = [ 'www.pknw1.co.uk', 'www.pknw1.co.uk','www.pknw1.co.uk','www.pknw1.co.uk','www.pknw1.co.uk']

def encoded_image(url):
  data = open(url, 'rb').read()
  data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
  data_base64 = data_base64.decode()    # convert bytes to string
  logo = 'data:image/png;base64,'+str(data_base64)
  return logo

@app.route("/")
def config_categories():
  categories = config.get('DEFAULT', 'categories').split('\n')
  applist = []
  for each_section in config.sections():
    applist.append({"name" : config[each_section]['name'], "category" : config[each_section]['category'], "summary" : config[each_section]['summary'], "link" : config[each_section]['link'], "search" : config[each_section]['search'], "info" : config[each_section]['info']})
  logo = encoded_image('web/static/images/logo.png')
  product = encoded_image('web/static/images/OPDT.png')
  return render_template('index.html', base_url=request.base_url, product=product, logo=logo, categories=categories, applist=applist)



@app.route("/home")
def home():
    parsed = urlparse(request.base_url)
    base_url='http://'+str(parsed.netloc)+'/'
    return render_template('home.html', base_url=base_url)


@app.route("/frame")
def frame():
    parsed = urlparse(request.base_url)
    base_url='http://'+str(parsed.netloc)+'/'
    return render_template('frame.html', urls=urls, base_url=base_url)

@app.route("/info/<app>")
def info(app=None):
    info = render_template('info/'+app+'.html')
    parsed = urlparse(request.base_url)
    base_url='http://'+str(parsed.netloc)+'/'
    return render_template('infowindow.html', base_url=base_url, info=info)


if __name__ == "__main__":
    app.run(debug=True)

