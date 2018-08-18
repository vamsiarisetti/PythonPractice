from flask import Flask,render_template, request
# from custom_module import Search_module
from Search_module import search4Letters
from flask import escape

app = Flask (__name__)

# def log_request(req: 'flask_request', res: str) -> None:
#  with open('vsearch.log', 'a') as log:
#  print(req, res, file=log)

@app.route('/')
def hello() -> str:
    return 'Helloworld flask'

@app.route('/search4letters', methods=['POST'])
def do_searchLtr() -> str:
    return str(search4Letters('life, the universe, and everything!','eiru,!'))
    # return rtnset

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4Letters(phrase, letters))
    logReq = log_request(request,results,phrase, letters)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route ('/entry')
def entry_page()-> 'html':
    return render_template('entry.html',the_title = 'welcome to search4letters page')

def log_request(req: 'flask_request', res: str,phrase, letters) -> None:
    with open('vsearch.log','a') as log:
        print(req, "Letters Found : "+res, "Given phrase : "+phrase, "Letters to be Found : "+letters, file=log)

@app.route('/viewLog')
def view_log() -> str:
    with open('vsearch.log') as log:
        content = escape(log.read());
    return "===>"+content

# app.run(debug=True, host='192.168.0.108')
app.run(host='192.168.0.102')
