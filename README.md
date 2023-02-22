# Web-приложение ToDo на FastAPI
[![Python Version](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://python.org)

Простой ToDo менеджер, реализованный на веб-фреймворке FastAPI 
В качестве веб-интерфейса использован фреймворк Semantic UI https://semantic-ui.com/

![ToDo на FastAPI](/todo_img.png)

Клонируем репо

```bash
git clone https://github.com/ajax3101/todo.git
```

Устанавливаем и активируем виртуальное окружение
```bash
    python3 -m venv venv
    . venv/bin/activate
 ```

Устанавливаем модули

```bash
    pip install fastapi uvicorn sqlalchemy jinja2
    pip install python-multipart python-dotenv
```
Или установить полный fastapi, включающий jinja2, python-multipart, uvicorn

```bash
    pip install fastapi[all] sqlalchemy
```
Или загружаем файл с зависимостями проекта

```bash
pip install -r requirements.txt
```
Запус приложения
```bash
python main.py
```
**Внимание!**
Файл .env должен быть указан в файле .gitignore чтобы ваши настройки не улетели в репозиторий, но для данного примера я его
исключил из файла игнора

База данных должна быть в файле .gitignore, но для этого примера я ее оттуда удалил, чтобы был пример ToDo задач

Чтобы автоматически создать структуру проекта запустите в консоли файл

    structure_project.bat