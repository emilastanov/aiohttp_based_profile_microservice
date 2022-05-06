

async def make_cv_query_response(cv_data):
    limit, offset, count, cv_data = cv_data

    beautify_data = []
    for cv in cv_data:
        beautify_data.append({
            "id": cv[0],
            "wish_position": cv[1],
            "military_duty": cv[2],
            "possibility_of_moving": cv[3],
            "marital_status": cv[4],
            "avatar": cv[5],
            "wish_salary": cv[6],
            "first_name": cv[7],
            "last_name": cv[8],
            "date_of_birthday": str(cv[9])
        })

    return {
        "status": 200,
        "data": {
            "status": "ok",
            "data": beautify_data,
            "limit": int(limit),
            "offset": int(offset),
            "count": int(count or 0)
        }
    }


