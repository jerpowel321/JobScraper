from flask import Flask, request

from search import search_monster

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/search")
def search():
    # data = request.args
    # print(data)
    keyword = data["q"]
    city = data["city"]
    #location = data["location"]
    print(keyword)
    jobs = []
    results = search_monster(query = keyword, location = city)
    # results = search_monster()
    jobs = [r for r in results]
    print(jobs)
    return jobs
    # return render_template("results.html", post_list = jobs)