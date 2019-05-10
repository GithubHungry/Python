from flask import Flask, render_template, request, escape
import SearchFunctionForVowels

app = Flask(__name__)


# def hello() -> '302':
#     return redirect('/entry')  # Сообщает браузеру, что необходимо запросить альтернативный URL

def log_request(req: 'flask-request', res: str) -> None:  # В параметрах имя объекта request и строка результата
    with open('Search.log', 'a') as fi:
        print(req.form, req.remote_addr, req.user_agent, res, file=fi, sep='|')
        # print(req.form, file=fi, end='|')  # Сохраняет данные из формы в файл
        # print(req.remote_addr, file=fi, end='|')  # Сохраняет ip адрес пользователя
        # print(req.user_agent, file=fi, end='|')  # Сохраняет вид браузера пользователя
        # print(res, file=fi)  # Сохраняет результат отработки функции do_search


@app.route('/search4', methods=['POST'])  # Метод POST как и в форме
def do_search() -> 'html':
    phrase = request.form['phrase']  # Получаем данные из формы
    letters = request.form['letters']
    result = str(SearchFunctionForVowels.search_for_letters_v_2(phrase, letters))
    log_request(request, result)  # вызов функции журналирования
    return render_template('results.html', the_letters=letters, the_phrase=phrase, the_title='Here are your results!',
                           the_results=result)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> str:
    with open('Search.log') as fi:
        content = fi.readlines()  # Читает весь файл строками? , READ - читает весь файл в строку,readline построчно
    return escape(''.join(content))


if __name__ == '__main__':  # Оборачиваем .run() конструкцией if для PythonAnywhere
    app.run(debug=True)
