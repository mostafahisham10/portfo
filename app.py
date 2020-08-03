from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


# Open web page depending on url
@app.route('/')
@app.route('/<string:page_name>')
def html_page(page_name="index.html"):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", "a") as database:
        # Check if database.csv exists, if not add headers from fieldnames
        if database.tell() == 0:
            fieldnames = ['Email', 'Name', 'Message']
            write_header = csv.DictWriter(database, fieldnames=fieldnames)
            write_header.writeheader()
        # Unpacking the data from the dictionary
        email = data["email"]
        subject = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Adds the data entered from user
        csv_writer.writerow([email, subject, message])


# When contact is submitted
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # fetch data and convert it to dictionary
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("thankyou.html")
    else:
        return "something went wrong, try again"


# An example for passing a variable to the HTML file
# @app.route('/<username>/<int:post_id>')
# def user_name(username=None, post_id=None):
#     return render_template("index2.html", name=username, id_num=post_id)
