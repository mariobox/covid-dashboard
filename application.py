from covid import Covid
from flask import Flask, redirect, render_template, request

# Configure app
app = Flask(__name__)

covid = Covid()

# list of objects from Covid python package: https://pypi.org/project/covid/
d = covid.get_data()

# sort list in descending order of deaths
d.sort(key=lambda x: x.get('deaths'), reverse=True)

# format selected numeric fields to thousands with comma
for country in d:
    country['confirmed'] = format(country['confirmed'], ",")
    country['deaths'] = format(country['deaths'], ",")

# define our home page route passing the data from our imported covid package
@app.route("/")
def index():
  return render_template("index.html", data=d)


