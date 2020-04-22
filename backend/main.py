from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/search")
def search():
    # data = request.args
    # print data
    # keyword = data["q"]
    # print keyword
    # jobs = []
    # results = search_monster(query = keyword)
    # jobs = [r for r in results]

    # return render_template("results.html", post_list = jobs)