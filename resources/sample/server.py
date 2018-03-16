from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/orderinfo', methods=['POST','GET'])
def orderinfo():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            address = request.form['address']
            message = request.form['message']

            msg = "All done, {}!".format(name)
        except:
            msg = "But, Order has problem.."
        finally:
            return render_template("success.html", msg=msg)
    else:
        return render_template("orderinfo.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1')
