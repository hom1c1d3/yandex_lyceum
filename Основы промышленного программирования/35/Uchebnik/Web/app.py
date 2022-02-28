from flask import Flask, request, make_response, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "abrgdfdv"


@app.route("/cookie_test")
def cookie_test():
    visit_count = int(request.cookies.get("visit_count", 0))
    if visit_count:
        resp = make_response(f"вы пришли на эту страницу {visit_count + 1} раз")
        resp.set_cookie("visit_count", str(visit_count + 1), max_age=60 * 60 * 23 * 365 * 2)
    else:
        resp = make_response(f"вы пришли на эту страницу 1 раз за последние два года")
        resp.set_cookie("visit_count", "1", max_age=60 * 60 * 23 * 365 * 2)
    return resp


@app.route("/session_test")
def session_test():
    visit_count = session.get("visit_count", 0)
    session["visit_count"] = visit_count + 1
    session.permanent = True
    if session["visit_count"] > 9:
        session.pop("visit_count")
    return make_response(f"вы пришли на эту страницу {visit_count + 1} раз")


def main():
    app.run(host="", port=8080)


if __name__ == '__main__':
    main()
