from flask import Flask, render_template

# Scripts\activate
# flask --app server run
# Use this to run

# flask --app server --debug run
# Use this to run with debugger 
# This allows for changes to be seen
# on refresh

app = Flask(__name__)

@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)

@app.route("/about")
def about():
    return render_template('./about.html')

@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog.</p>"