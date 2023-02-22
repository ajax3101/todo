# todo
Web-приложение ToDo на FastAPI
Простой ToDo менеджер, реализованный на веб-фреймворке FastAPI 
В качестве веб-интерфейса использован фреймворк Semantic UI https://semantic-ui.com/

![Image alt](https://todo_img.png?size=1200x720&quality=96&type=album)


Устанавливаем и активируем виртуальное окружение

    python3 -m venv venv
    . venv/bin/activate

Устанавливаем модули

    pip install fastapi uvicorn sqlalchemy jinja2
    pip install python-multipart python-dotenv

Или установить полный fastapi, включающий jinja2, python-multipart, uvicorn

    pip install fastapi[all] sqlalchemy

Или создаем файл с зависимостями проекта

    pip freeze > requirements.txt

Запус приложения
python main.py

**Внимание!**
Файл .env должен быть указан в файле .gitignore чтобы ваши настройки не улетели в репозиторий, но для данного примера я его
исключил из файла игнора

База данных должна быть в файле .gitignore, но для этого примера я ее оттуда удалил, чтобы был пример ToDo задач

Чтобы автоматически создать структуру проекта запустите в консоли файл

    structure_project.bat