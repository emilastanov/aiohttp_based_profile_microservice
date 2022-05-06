from app.middlewares.models import get_model_by_name
from app.store.database.models import db


async def filter_by_linked_models_param(linked_model_name: str, params: list):
    query = db.text(f''
                    f'SELECT * FROM {linked_model_name} as t '
                    f'INNER JOIN user_cv as cv ON cv.id = t.cv '
                    f'WHERE t.id = ANY(:params) '
                    f'ORDER BY t.cv '
                    )
    data = await db.all(query, params=params)

    for obj in data:
        print(obj)
    return

