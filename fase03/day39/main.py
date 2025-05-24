from flask import Flask, render_template, request, redirect
import mamanger_db

app = Flask(__name__)


@app.route('/')
def home():
    tweets = mamanger_db.get_all_tweets()
    return render_template("index.html", tweets=tweets)


@app.route('/tweet', methods=["POST"])
def post_tweet():
    new_tweet = request.form.get("contenido")
    mamanger_db.add_tweet(new_tweet)
    return redirect("/")


@app.route('/delete/<int:id>', methods=["POST"])
def delete_tweet(id):
    mamanger_db.delete_tweet(id)
    return redirect("/")


if __name__ == "__main__":
    mamanger_db.create_db()
    app.run(debug=True)
