from os import (
    mkdir,
    system
)
from sys import argv


def make_python_dir(name: str, path="") -> None:
    """
    Make python directory.
    :param name: name of directory.
    :param path: path of directory.
    :return:
    """
    mkdir(f".{path}/{name}")
    open(f".{path}/{name}/__init__.py", "x")
    print(f'astframe: Python directory .{path}/{name} created.')


def make_dir(name: str, path="") -> None:
    """
    Make python directory.
    :param name: name of directory.
    :param path: path of directory.
    :return:
    """
    mkdir(f".{path}/{name}")
    print(f'astframe: Directory .{path}/{name} created.')


def make_gitignore() -> None:
    """
    Make gitignore.
    """
    file = open(".gitignore", "w")
    file.write("/config/\n")
    file.write("/venv/\n")
    file.write("/migrations/\n")
    file.write("/app/tests/*.txt\n")
    file.close()
    print(f'astframe: .gitignore created.')


def make_requirements() -> None:
    """
    Make requirements.
    """
    file = open("requirements.txt", "w")
    file.write("aiohttp==3.7.3\n"
               "aiohttp-apispec==2.2.3\n"
               "aiosmtplib==1.1.6\n"
               "alembic==1.7.7\n"
               "apispec==3.3.2\n"
               "async-timeout==3.0.1\n"
               "asyncpg==0.25.0\n"
               "attrs==21.4.0\n"
               "certifi==2021.10.8\n"
               "gino==1.0.1\n"
               "marshmallow==3.15.0\n"
               "multidict==6.0.2\n"
               "packaging==21.3\n"
               "psycopg2-binary==2.9.3\n"
               "pyparsing==3.0.8\n"
               "PyYAML==6.0\n"
               "requests==2.27.1\n"
               "SQLAlchemy==1.3.24\n"
               "typing_extensions==4.1.1\n"
               "urllib3==1.26.9\n"
               "webargs==5.5.3\n"
               "httpx==0.22.0\n")
    file.close()
    print(f'astframe: requirements.txt created.')


def make_file(name: str, path="", text="") -> None:
    """
    Make file with text.
    :param name: name of file.
    :param path: path of file.
    :param text: text of file.
    :return:
    """
    file = open(f".{path}/{name}", "w")
    file.write(text)
    file.close()
    print(f'astframe: File .{path}/{name} created.')


def append_to_file(name: str, path="", text="") -> None:
    """
    Append text into exist file.
    :param name: name of file.
    :param path: path of file.
    :param text: text of file.
    :return:
    """
    file = open(f".{path}/{name}", "a")
    file.write(text)
    file.close()
    print(f'astframe: Text has been appended in file .{path}/{name}.')


def append_import_to_file(name: str, path="", importing="") -> None:
    """
    Append import to file.
    :param name: name of file.
    :param path: path of file.
    :param importing: importing header.
    :return:
    """
    file = open(f".{path}/{name}", "r")
    text = file.read()
    file.close()

    file = open(f".{path}/{name}", "w")
    file.write(f"{importing}\n{text}")
    file.close()
    print(f'astframe: Import has been appended in file .{path}/{name}.')


def append_text_to_file_after_specified_string(name: str, specify_string: str, path="", text=""):
    """
    Append text to file after specified string.
    :param name: name of file.
    :param specify_string: specified string.
    :param path: path of file.
    :param text: text of file.
    :return:
    """
    file = open(f".{path}/{name}", "r")
    text_of_file = file.read().replace('pass', '')
    file.close()

    begin_of_text = text_of_file[0:text_of_file.find(specify_string) + len(specify_string)]
    end_of_text = text_of_file[text_of_file.find(specify_string) + len(specify_string) + 1:]

    count_of_space = 0
    while end_of_text[count_of_space] == ' ':
        count_of_space += 1

    file = open(f".{path}/{name}", "w")
    file.write(f"{begin_of_text}\n{' ' * count_of_space}{text}\n{end_of_text}")
    file.close()
    print(f'astframe: Text has been appended in file .{path}/{name} after specified string.')


def init(argv: argv) -> None:
    """
    Initialize project structure
    :return:
    """
    make_python_dir('app')
    make_dir('config')

    make_python_dir('source', '/app')

    make_python_dir('store', '/app')

    make_python_dir('views', '/app/source')
    make_python_dir('tests', '/app/source')

    make_python_dir('database', '/app/store')

    make_gitignore()
    make_requirements()
    system('pip install --upgrade pip')
    system('pip install -r requirements.txt')

    make_file(
        'models.py',
        path='/app/store/database',
        text="from gino import Gino\n\n"
             "db = Gino()\n"
    )

    make_file(
        'accessor.py',
        path='/app/store/database',
        text="from aiohttp import web\n"
             "\n"
             "\n"
             "class PostgresAccessor:\n"
             "    def __init__(self):\n"
             "        # Make model in /app/source/models.py and append it here.\n"
             "        # from app.source.models import Model\n"
             "\n"
             "        # self.model_name = Model\n"
             "\n"
             "        self.db = None\n"
             "\n"
             "    def setup(self, application: web.Application) -> None:\n"
             "        application.on_startup.append(self._on_connect)\n"
             "        application.on_cleanup.append(self._on_disconnect)\n"
             "\n"
             "    async def _on_connect(self, application: web.Application):\n"
             "        from app.store.database.models import db\n"
             "\n"
             "        self.config = application['config']['postgres']\n"
             "        await db.set_bind(self.config['database_url'])\n"
             "        self.db = db\n"
             "\n"
             "    async def _on_disconnect(self, _) -> None:\n"
             "        if self.db is not None:\n"
             "            await self.db.pop_bind().close()\n"
             "\n"

    )

    make_file(
        'config.yaml',
        path='/config',
        text="common:\n"
             "  port: 8080 # порт, на котором будет работать сервер\n"
             "postgres:\n"
             "  database_url: postgres://admin:admin@localhost # адрес базы данных\n"
             "  require_ssl: false # стоит ли шифровать соединение с базой\n"
    )

    make_file(
        'settings.py',
        path='/app',
        text="import pathlib\n"
             "import yaml\n"
             "\n"
             "BASE_DIR = pathlib.Path(__file__).parent.parent\n"
             "config_path = BASE_DIR / 'config' / 'config.yaml'\n"
             "\n"
             "\n"
             "def get_config(path):\n"
             "    with open(path) as f:\n"
             "        parsed_config = yaml.safe_load(f)\n"
             "        return parsed_config\n"
             "\n"
             "\n"
             "config = get_config(config_path)\n"
    )

    make_file(
        'models.py',
        path='/app/source',
        text="from sqlalchemy.dialects.postgresql import UUID\n"
             "from uuid import uuid4\n"
             "\n"
             "from app.store.database.models import db\n"
    )

    make_file(
        'routes.py',
        path='/app/source',
        text=""
             "\n"
             "\n"
             "def setup_routes(app):\n"
             "    pass\n"
    )

    make_file(
        'schemas.py',
        path='/app/source/views',
        text="from marshmallow import Schema, fields\n"
             "\n"
             "\n"
             "class Error(Schema):\n"
             "    status = fields.Str()\n"
             "    error = fields.Str()\n"
             "\n"
             "\n"
             "class Identifier(Schema):\n"
             "    id = fields.Int()\n"
             "\n"
             "\n"
             "class Status(Schema):\n"
             "    status = fields.Str()\n"
    )

    make_file(
        'README.md',
        text=f'# {argv[2]}\n' if len(argv) > 2 else '# aiohttp_based_microservice\n'
    )

    make_file(
        'main.py',
        text="from aiohttp import web\n"
             "from aiohttp_apispec import setup_aiohttp_apispec\n"
             "\n"
             "from app.settings import config\n"
             "from app.store.database.accessor import PostgresAccessor\n"
             "\n"
             "\n"
             "def setup_accessors(application):\n"
             "    application['db'] = PostgresAccessor()\n"
             "    application['db'].setup(application)\n"
             "\n"
             "\n"
             "def setup_config(application):\n"
             "    application['config'] = config\n"
             "\n"
             "\n"
             "def setup_routes(application):\n"
             "    from app.source.routes import setup_routes as imported_routes\n"
             "    imported_routes(application)\n"
             "\n"
             "\n"
             "def setup_documentation(application):\n"
             "    setup_aiohttp_apispec(\n"
             "        app=application,\n"
             f"        title='{argv[2] if len(argv) > 2 else 'Aiohttp based microservice.'}',\n"
             "        version='v1',\n"
             "        url='/api/docs/swagger.json',\n"
             "        swagger_path='/' # Адресс, на котором будет доступна документация\n"
             "    )\n"
             "\n"
             "\n"
             "def setup_app(application):\n"
             "    setup_documentation(application)\n"
             "    setup_config(application)\n"
             "    setup_routes(application)\n"
             "    setup_accessors(application)\n"
             "\n"
             "\n"
             "app = web.Application()\n"
             "\n"
             "if __name__ == '__main__':\n"
             "    setup_app(app)\n"
             "    try:\n"
             "        web.run_app(app, port=config['common']['port'])\n"
             "    except OSError:\n"
             "        print('База данных не подключена! "
             "В файле /config/config.yaml необходимо указать адресс базы данных.')\n"
    )

    system("alembic init migrations")

    file = open("./alembic.ini", "r")
    text = file.read().replace("driver://user:pass@localhost/dbname", "None")
    file.close()

    file = open("./alembic.ini", "w")
    file.write(text)
    file.close()

    make_file(
        "env.py",
        path="/migrations",
        text="from logging.config import fileConfig\n"
             "\n"
             "from alembic import context\n"
             "from sqlalchemy import create_engine\n"
             "\n"
             "from app.settings import config as app_config\n"
             "from app.store.database.accessor import PostgresAccessor\n"
             "from app.store.database.models import db\n"
             "\n"
             "config = context.config\n"
             "fileConfig(config.config_file_name)\n"
             "target_metadata = db\n"
             "\n"
             "\n"
             "def run_migrations_online():\n"
             "    # Alembic видит только те модели, которые импортированы в момент генерации миграции.\n"
             "    # PostgresAccessor инстанцируется и импортит все нужные модели, тем самым позволяя автогенерировать миграции\n"
             "    PostgresAccessor()\n"
             "    connectable = create_engine(app_config['postgres']['database_url'])\n"
             "    with connectable.connect() as connection:\n"
             "        context.configure(connection=connection, target_metadata=target_metadata)\n"
             "        with context.begin_transaction():\n"
             "            context.run_migrations()\n"
             "\n"
             "\n"
             "run_migrations_online()\n"
    )


def append_model(name: str, **attributes) -> None:
    """
    Method for append model to model.py file.
    :param name: name of model.
    :param attributes: model attrebutes.
    :return:
    """
    file = open("./app/source/models.py", "a")
    file.write(
        "\n"
        f"class {name.capitalize()}(db.Model):\n"
        f"    __tablename__ = '{name.lower()}'\n"
        "    id = db.Column(db.Integer, primary_key=True)\n"
    )


def make_object(name: str, idempotent=False) -> None:
    """
    Make object with CRUD methods of rest api.
    :param idempotent: is create method of current object idempotent?
    :param name: name of object.
    :return:
    """
    make_python_dir(
        name.lower(),
        path='/app/source/views'
    )

    make_python_dir(
        'methods',
        path=f'/app/source/views/{name.lower()}'
    )

    make_python_dir(
        'delete',
        path=f'/app/source/views/{name.lower()}/methods'
    )

    make_python_dir(
        'get',
        path=f'/app/source/views/{name.lower()}/methods'
    )

    make_python_dir(
        'patch',
        path=f'/app/source/views/{name.lower()}/methods'
    )

    make_python_dir(
        'put' if idempotent else 'post',
        path=f'/app/source/views/{name.lower()}/methods'
    )

    make_file(
        'schemas.py',
        path=f'/app/source/views/{name.lower()}',
        text="from marshmallow import Schema, fields\n"
             "\n"
             "\n"
             f"class {name.capitalize()}(Schema):\n"
             "    id = fields.Int()\n"
             "    title = fields.Str()\n"
             "    description = fields.Str()\n"
    )

    make_file(
        'document.py',
        path=f'/app/source/views/{name.lower()}/methods/get',
        text="from aiohttp_apispec import docs\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods import name\n"
             "\n"
             "\n"
             "def swagger_extension(method):\n"
             "    @docs(\n"
             "        tags=[name],\n"
             "        summary='Список',\n"
             "        description='''Метод для получения списка.''',\n"
             "        # parameters=[{\n"
             "        #     'in': 'header',\n"
             "        #     'name': 'Authorization',\n"
             "        #     'description': 'Токен пользователя.',\n"
             "        #     'schema': {'type': 'string'},\n"
             "        #     'required': 'true'\n"
             "        # }],\n"
             "        responses={\n"
             "            200: {\n"
             "                # 'schema': {},\n"
             "                'description': 'Список.'\n"
             "            }\n"
             "        }\n"
             "    )\n"
             "    def extension(*args, **kwargs):\n"
             "        return method(*args, **kwargs)\n"
             "\n"
             "    return extension\n"
    )

    make_file(
        'document.py',
        path=f'/app/source/views/{name.lower()}/methods/{"put" if idempotent else "post"}',
        text="from aiohttp_apispec import docs, request_schema\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods import name\n"
             f"from app.source.views.{name.lower()}.schemas import {name.capitalize()}\n"
             "from app.source.views.schemas import Error\n"
             "\n"
             "\n"
             "def swagger_extension(method):\n"
             "    @docs(\n"
             "        tags=[name],\n"
             "        summary='Создание',\n"
             "        description='''Метод создания.''',\n"
             "        # parameters=[{\n"
             "        #     'in': 'header',\n"
             "        #     'name': 'Authorization',\n"
             "        #     'description': 'Токен пользователя.',\n"
             "        #     'schema': {'type': 'string'},\n"
             "        #     'required': 'true'\n"
             "        # }],\n"
             "        responses={\n"
             "            200: {\n"
             "                # 'schema': {},\n"
             "                'description': 'Данные.'\n"
             "            },\n"
             "            400: {\n"
             "                'schema': Error,\n"
             "                'description': 'Уже существует.'\n"
             "            }\n"
             "        }\n"
             "    )\n"
             f"    @request_schema({name.capitalize()}())\n"
             "    def extension(*args, **kwargs):\n"
             "        return method(*args, **kwargs)\n"
             "\n"
             "    return extension\n"
             "\n"
    )

    make_file(
        'document.py',
        path=f'/app/source/views/{name.lower()}/methods/patch',
        text="from aiohttp_apispec import docs, request_schema\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods import name\n"
             f"from app.source.views.{name.lower()}.schemas import {name.capitalize()}\n"
             "from app.source.views.schemas import Error\n"
             "\n"
             "\n"
             "def swagger_extension(method):\n"
             "    @docs(\n"
             "        tags=[name],\n"
             "        summary='Создание',\n"
             "        description='''Метод создания.''',\n"
             "        # parameters=[{\n"
             "        #     'in': 'header',\n"
             "        #     'name': 'Authorization',\n"
             "        #     'description': 'Токен пользователя.',\n"
             "        #     'schema': {'type': 'string'},\n"
             "        #     'required': 'true'\n"
             "        # }],\n"
             "        responses={\n"
             "            200: {\n"
             "                # 'schema': {},\n"
             "                'description': 'Данные.'\n"
             "            },\n"
             "            400: {\n"
             "                'schema': Error,\n"
             "                'description': 'Уже существует.'\n"
             "            }\n"
             "        }\n"
             "    )\n"
             f"    @request_schema({name.capitalize()}())\n"
             "    def extension(*args, **kwargs):\n"
             "        return method(*args, **kwargs)\n"
             "\n"
             "    return extension\n"
             "\n"
    )

    make_file(
        'document.py',
        path=f'/app/source/views/{name.lower()}/methods/delete',
        text="from aiohttp_apispec import docs, request_schema\n"
             "from marshmallow import Schema, fields\n"
             "\n"
             "from app.source.views.schemas import (\n"
             "    Status,\n"
             "    Identifier\n"
             ")\n"
             f"from app.source.views.{name.lower()}.methods import name\n"
             "\n"
             "\n"
             "class DeleteRequestSchema(Schema):\n"
             "    id = fields.Int()\n"
             "\n"
             "\n"
             "def swagger_extension(method):\n"
             "    @docs(\n"
             "        tags=[name],\n"
             "        summary='Удаление',\n"
             "        description='''Метод для удаления.''',\n"
             "        # parameters=[{\n"
             "        #     'in': 'header',\n"
             "        #     'name': 'Authorization',\n"
             "        #     'description': 'Токен пользователя.',\n"
             "        #     'schema': {'type': 'string'},\n"
             "        #     'required': 'true'\n"
             "        # }],\n"
             "        responses={\n"
             "            202: {\n"
             "                'schema': Status,\n"
             "                'description': 'Статус процесса удаления.'\n"
             "            }\n"
             "        }\n"
             "    )\n"
             "    @request_schema(Identifier())\n"
             "    def extension(*args, **kwargs):\n"
             "        return method(*args, **kwargs)\n"
             "\n"
             "    return extension\n"
    )

    append_to_file(
        '__init__.py',
        path=f'/app/source/views/{name.lower()}/methods',
        text=f"\nname = '{name.capitalize()}'\n"
    )

    make_file(
        'handler.py',
        path=f'/app/source/views/{name.lower()}/methods/get',
        text="from json import JSONDecodeError\n"
             "from aiohttp import web\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods.get.document import swagger_extension\n"
             "from app.source.models import *\n"
             "\n"
             "\n"
             "__all__ = ('Handler', )\n"
             "\n"
             "\n"
             "class Handler(web.View):\n"
             "\n"
             "    @swagger_extension\n"
             "    async def get(self):\n"
             "        response = {\n"
             "            'status': web.HTTPOk.status_code,\n"
             "            'data': {\n"
             "                'info': 'Get method.'\n"
             "            }\n"
             "        }\n"
             "\n"
             "        return web.json_response(**response)\n"
    )

    make_file(
        'handler.py',
        path=f'/app/source/views/{name.lower()}/methods/patch',
        text="from json import JSONDecodeError\n"
             "from aiohttp import web\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods.patch.document import swagger_extension\n"
             "from app.source.models import *\n"
             "\n"
             "\n"
             "__all__ = ('Handler', )\n"
             "\n"
             "\n"
             "class Handler(web.View):\n"
             "\n"
             "    @swagger_extension\n"
             "    async def patch(self):\n"
             "        response = {\n"
             "            'status': web.HTTPOk.status_code,\n"
             "            'data': {\n"
             "                'info': 'Patch method.'\n"
             "            }\n"
             "        }\n"
             "\n"
             "        return web.json_response(**response)\n"
    )

    make_file(
        'handler.py',
        path=f'/app/source/views/{name.lower()}/methods/delete',
        text="from json import JSONDecodeError\n"
             "from aiohttp import web\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods.delete.document import swagger_extension\n"
             "from app.source.models import *\n"
             "\n"
             "\n"
             "__all__ = ('Handler',)\n"
             "\n"
             "\n"
             "class Handler(web.View):\n"
             "\n"
             "    @swagger_extension\n"
             "    async def delete(self):\n"
             "        response = {\n"
             "            'status': web.HTTPOk.status_code,\n"
             "            'data': {\n"
             "                'info': 'Delete method.'\n"
             "            }\n"
             "        }\n"
             "\n"
             "        return web.json_response(**response)\n"
    )

    make_file(
        'handler.py',
        path=f'/app/source/views/{name.lower()}/methods/{"put" if idempotent else "post"}',
        text="from json import JSONDecodeError\n"
             "from aiohttp import web\n"
             "\n"
             f"from app.source.views.{name.lower()}.methods.{'put' if idempotent else 'post'}.document import swagger_extension\n"
             "from app.source.models import *\n"
             "\n"
             "\n"
             "__all__ = ('Handler',)\n"
             "\n"
             "\n"
             "class Handler(web.View):\n"
             "\n"
             "    @swagger_extension\n"
             f"    async def {'put' if idempotent else 'post'}(self):\n"
             "        response = {\n"
             "            'status': web.HTTPOk.status_code,\n"
             "            'data': {\n"
             f"                'info': '{'Put' if idempotent else 'Post'} method.'\n"
             "            }\n"
             "        }\n"
             "\n"
             "        return web.json_response(**response)\n"
    )

    append_to_file(
        '__init__.py',
        path=f'/app/source/views/{name.lower()}',
        text=f"from app.source.views.{name.lower()}.methods.get import GetView\n"
             f"from app.source.views.{name.lower()}.methods.patch import UpdateView\n"
             f"from app.source.views.{name.lower()}.methods.{'put' if idempotent else 'post'} import CreateView\n"
             f"from app.source.views.{name.lower()}.methods.delete import DeleteView\n"
             "\n"
             "\n"
             f"class {name.capitalize()}HandlerView(\n"
             "    GetView,\n"
             "    UpdateView,\n"
             "    CreateView,\n"
             "    DeleteView\n"
             "):\n"
             "    pass\n"
    )

    append_import_to_file(
        'routes.py',
        path='/app/source',
        importing=f'from app.source.views.{name.lower()} import {name.capitalize()}HandlerView'
    )

    append_text_to_file_after_specified_string(
        'routes.py',
        specify_string='def setup_routes(app):',
        path='/app/source',
        text=f'app.router.add_view("/{name.lower()}", {name.capitalize()}HandlerView)'
    )

    append_to_file(
        "__init__.py",
        path=f'/app/source/views/{name.lower()}/methods/delete',
        text=f"from app.source.views.{name.lower()}.methods.delete.handler import Handler\n"
             "\n"
             "\n"
             "class DeleteView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_to_file(
        "__init__.py",
        path=f'/app/source/views/{name.lower()}/methods/get',
        text=f"from app.source.views.{name.lower()}.methods.get.handler import Handler\n"
             "\n"
             "\n"
             "class GetView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_to_file(
        "__init__.py",
        path=f'/app/source/views/{name.lower()}/methods/patch',
        text=f"from app.source.views.{name.lower()}.methods.patch.handler import Handler\n"
             "\n"
             "\n"
             "class UpdateView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_to_file(
        "__init__.py",
        path=f'/app/source/views/{name.lower()}/methods/{"put" if idempotent else "post"}',
        text=f"from app.source.views.{name.lower()}.methods.{'put' if idempotent else 'post'}.handler import Handler\n"
             "\n"
             "\n"
             "class CreateView(\n"
             "    Handler\n"
             "):\n"
             "    pass\n"
    )

    append_model(name)

    append_text_to_file_after_specified_string(
        'accessor.py',
        path='/app/store/database',
        specify_string='def __init__(self):',
        text=f"from app.source.models import {name.capitalize()}"
    )

    append_text_to_file_after_specified_string(
        'accessor.py',
        path='/app/store/database',
        specify_string=f"from app.source.models import {name.capitalize()}",
        text=f'self.{name.lower()} = {name.capitalize()}'
    )


def make_migrations(msg="") -> None:
    """
    Make migrations.
    :param msg: message
    :return:
    """
    system(f"alembic revision -m=\"{msg}\" --autogenerate")
    print(f'astframe: Migrations created.')


def migrate() -> None:
    """
    Migrate
    :return:
    """
    system("alembic upgrade head")
    print(f'astframe: Migrate has been made.')


if __name__ == '__main__':
    try:
        command = argv[1]
    except IndexError:
        command = None

    if command == 'init':
        try:
            init(argv)
        except FileExistsError:
            print('astframe: Error: Some directory already exist. Folders /app and /config dirs must not exist.')
    elif command == 'make_object':
        if len(argv) > 2:
            try:
                make_object(argv[2], idempotent='-idempotent' in argv)
            except FileNotFoundError:
                print(
                    'astframe: Error: Recently you must initialize project. Make command "python astproject.py init".')
        else:
            print('astframe: Error: Must specify the name of object as the second argument.')
    elif command == 'make_migrations':
        make_migrations(msg=argv[2] if len(argv) > 2 else "")
    elif command == 'migrate':
        migrate()
    else:
        print("""    AstFrame:
        Существующие комманды:
        - init {Название проекта (опционально)}: Инициализация проекта.
        - make_object "Object_name" {-idempotent (опционально)}: Создание шаблона объекта.
        - make_migrations: Создание миграций.
        - migrate: Миграция.
        """)
