from flask import Flask, request
from datetime import datetime

app = Flask("My first server")

@app.route('/')
def index():
    return 'Hello, this is the first web server I am building'

@app.route('/nyandikira')
def contact_page():
    return "Contact me at nseirene3@gmail.com or 078833892"

@app.route('/with_html')
def with_html():
    return """
    <h1>Irene coldsober</h1>
    <p>Hello there,<br>
    I am trying to make things easier
    </p>
            """

@app.route("/list")
def do_list():
    return """
            <ol>
            <li>Apple</li>
            <li>Mango</li>
            <li>Lemon</li>
            <li>CITRUS</li>
            <li>Apple</li>
            </ol>
            """

@app.route('/date')
def datePage():
    date = datetime.now()
    return f"""Today's date is <h1>{date}</h1>"""

@app.route('/advanced')
def advanced():
    return """
    <form>
        <label>Name:</label>
        <input type="text" name="name" value="">
        <br><br>
 
        <label>E-mail:</label>
        <input type="email" name="emailaddress">
        <br><br>
 
        <label>Password: </label>
        <input type="password" name="password">
        <br><br>
 
        <input type="submit">
 
    </form>
            """
@app.route('/birthday', methods = ['POST', 'GET'])
def calcBirthDay():
    if request.method == 'POST': # USER SUBMITTING OR POSITING HIS INFORMATION
        return f"""
        <form action = "/birthday" method = "POST"> 
                <input type = "number" name = "year" placeholder = "Birthyear e.g 2022">
                <input type = "submit" value = "Submit">
        </form>
        birth year is <strong><mark>{request.form.get('year')}</mark></strong> and your age is: <h2>{2022 - int(request.form.get('year'))}</h2>
        """
    elif request.method == 'GET': # USER ASKING FOR THE FORM
        return """
                <form action = "/birthday" method = "POST">
                <input type = "number" name = "year" placeholder = "Birthyear e.g 2022">
                <input type = "submit" value = "Submit">
                </form>
                """


if __name__=="__main__":
    app.run()