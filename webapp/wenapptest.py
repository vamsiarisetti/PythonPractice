from flask import Flask,render_template, request
# from custom_module import Search_module
from Search_module import search4Letters

app = Flask (__name__)

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
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route ('/entry')
def entry_page()-> 'html':
    return render_template('entry.html',the_title = 'welcome to search4letters page')
app.run()

