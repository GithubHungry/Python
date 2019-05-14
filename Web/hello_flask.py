from flask import Flask, render_template, request, escape
import SearchFunctionForVowels
from DBcm import UseDatabase

app = Flask(__name__)

# def hello() -> '302':
#     return redirect('/entry')  # Сообщает браузеру, что необходимо запросить альтернативный URL
app.config['dbconfig'] = {'host': '127.0.0.1',  # app.config -встр.механизм конфигурации flask
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB'}  # На выходе получается словарь словарей


def log_request(req: 'flask-request', res: str) -> None:  # В параметрах имя объекта request и строка результата
    """Журналирует веб-запрос и возвращает результаты"""
    # conn = mysql.connector.connect(**dbparam)  # Создание соединения с параметрами
    # cur = conn.cursor()  # Создание курсора
    with UseDatabase(app.config['dbconfig']) as cur:
        _SQL = """insert into log (phrase,letters,ip,browser,results) values (%s,%s,%s,%s,%s)"""
        # Подготовленный запрос
        cur.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))
        # Выполнение запроса с подставкой данных из формы и тд и тп

    # conn.commit()  # Принудительная запись в БД
    # cur.close()  # Закрываем курсор
    # conn.close()  # Закрываем соединение

    # with open('Search.log', 'a') as fi:
    #     print(req.form, req.remote_addr, req.user_agent, res, file=fi, sep='|')
    # print(req.form, file=fi, end='|')  # Сохраняет данные из формы в файл
    # print(req.remote_addr, file=fi, end='|')  # Сохраняет ip адрес пользователя
    # print(req.user_agent, file=fi, end='|')  # Сохраняет вид браузера пользователя
    # print(res, file=fi)  # Сохраняет результат отработки функции do_search


@app.route('/search4', methods=['POST'])  # Метод POST как и в форме
def do_search() -> 'html':
    """Непосредственно сам поиск с выводом в html"""
    phrase = request.form['phrase']  # Получаем данные из формы
    letters = request.form['letters']
    result = str(SearchFunctionForVowels.search_for_letters_v_2(phrase, letters))
    log_request(request, result)  # вызов функции журналирования
    return render_template('results.html', the_letters=letters, the_phrase=phrase, the_title='Here are your results!',
                           the_results=result)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Страница приветствия"""
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_log() -> 'html':
    """Читает записи из (текстового файла) MySQL"""

    # contents = []
    # with open('Search.log') as log:
    #     for line in log:
    #         contents.append([])  # Создается подсписок списка 0(0),0(1),0(2) и т.д.
    #         for item in line.split('|'):  # Для подстроки в логе
    #             contents[-1].append(escape(item))  # В список списка добавляется элемент(сначала это 0(0) потом 0(1))

    with UseDatabase(app.config['dbconfig']) as cur:
        _SQL = """Select Phrase,Letters,ip,browser,results from log"""
        cur.execute(_SQL)
        contents = cur.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View log', the_row_titles=titles, the_data=contents)


if __name__ == '__main__':  # Оборачиваем .run() конструкцией if для PythonAnywhere
    app.run(debug=True)
