from flask import Flask, render_template, request
import SearchFunctionForVowels

app = Flask(__name__)


# def hello() -> '302':
#     return redirect('/entry')  # Сообщает браузеру, что необходимо запросить альтернативный URL


@app.route('/search4', methods=['POST'])  # Метод POST как и в форме
def do_search() -> 'html':
    phrase = request.form['phrase']  # Получаем данные из формы
    letters = request.form['letters']
    result = str(SearchFunctionForVowels.search_for_letters_v_2(phrase, letters))
    return render_template('results.html', the_letters=letters, the_phrase=phrase, the_title='Here are your results!',
                           the_results=result)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run(debug=True)
