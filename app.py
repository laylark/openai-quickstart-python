import base64
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(topic),
            temperature=0,
            max_tokens=200,
        )
        result = base64.urlsafe_b64encode(response.choices[0].text.encode())
        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    if result != None:
        result = base64.urlsafe_b64decode(result).decode()

    return render_template("index.html", result=result)


def generate_prompt(topic):
    return """Write a short summary of the topic with humor.

Topic: Legos
Summary: Legos: Where imagination and plastic unite to create small-scale architectural masterpieces or that one thing you stepped 
on in the middle of the night.
Topic: Toilets
Summary: Toilets: The porcelain throne where we leave our problems behind, and our poop in front of.
Topic: {}
Summary: """.format(
        topic.capitalize()
    )
