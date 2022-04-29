from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec

from app.settings import config
from app.store.database.accessor import PostgresAccessor


def setup_accessors(application):
    application['db'] = PostgresAccessor()
    application['db'].setup(application)


def setup_config(application):
    application['config'] = config


def setup_routes(application):
    from app.source.routes import setup_routes as imported_routes
    imported_routes(application)


def setup_documentation(application):
    setup_aiohttp_apispec(
        app=application,
        title='Profile service',
        version='v1',
        url='/api/docs/swagger.json',
        swagger_path='/' # Адресс, на котором будет доступна документация
    )


def setup_app(application):
    setup_documentation(application)
    setup_config(application)
    setup_routes(application)
    setup_accessors(application)


app = web.Application()

if __name__ == '__main__':
    setup_app(app)
    try:
        web.run_app(app, port=config['common']['port'], host='0.0.0.0')
    except OSError:
        print('База данных не подключена! В файле /config/config.yaml необходимо указать адресс базы данных.')
