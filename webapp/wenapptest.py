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
    logReq = log_request(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

@app.route ('/entry')
def entry_page()-> 'html':
    return render_template('entry.html',the_title = 'welcome to search4letters page')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        # print(str(dir(req)), "Letters Found : "+res, "Given phrase : "+phrase, "Letters to be Found : "+letters, file=log)
        # print(req.form, file=log, end='|')           # get the data from the HTML form
        # print(req.remote_addr, file=log, end='|')    # get the IP Address
        # print(req.user_agent, file=log, end='|')     # Browser details
        # print(res, file=log)                         # Response

        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/viewLog')
def view_log() -> 'html':
    content = []
    with open('vsearch.log') as log:
        for line in log:
            content.append([])
            for lineSplit in line.split('|'):
                content[-1].append(escape(lineSplit))
    formHdrs = ['Form Data', 'Remote_addr', 'User_agent', 'Results']
    return render_template('viewlog.html',
                           the_title='View logs Here',
                           the_row_titles=formHdrs,
                           the_data=content,)

# app.run(debug=True, host='192.168.0.108')

# if __name__ == '__main__':
app.run(debug=True)
