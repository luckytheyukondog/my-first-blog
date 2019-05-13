
from flask import Flask, request
from calculator import calc


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        a = None
        d = None
        try:
            a = float(request.form["a"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["a"])
        try:
            d = float(request.form["d"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["d"])
        if a is not None and d is not None:
            result = calc(a, d)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)
    return '''
        <html>
        <head>
            <title>LuckytheDog</title>
        </head>
            <body>
            {errors}
                <h1>True Thickness Calculator</h1>
                <p>Angle to core axis:
                <form method="post" action=".">
                    <p><input name="a" /></p>

                <p>Downhole thickness:

                    <p><input name="d" /></p>
                    <p><input type="submit" value="Calculate" /></p>
                </form>
            </body>

        </html>
    '''.format(errors=errors)

