from flask import render_template, request

from gdtot import app


@app.route("/")
def home_page():
    custom_cookies = bool(
        request.cookies.get("crypt") and request.cookies.get("PHPSESSID")
    )

    return render_template("home.html", custom_cookies=custom_cookies)
