from flask import Flask
import SearchFunctionForVowels

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'


@app.route('/search4')
def do_search() -> str:
    return str(SearchFunctionForVowels.search_for_letters_v_2('life, the universe, and everything!', 'eiru,!'))


app.run()
