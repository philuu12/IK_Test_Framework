# Generate data
def gen_data(title: object = None, body: object = None, userId: object = None) -> object:
    data = {}

    if title is not None:
        data["title"] = title

    if body is not None:
        data["body"] = body

    if userId is not None:
        data["userId"] = body

    return data

