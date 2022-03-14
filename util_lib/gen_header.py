# Header generations
def generate_header(header=all):
    if header == 'Content-Type':
        return {header: 'application/json; charset=UTF-8'}
    elif header == 'Transfer-Encoding':
        return {header: 'chunked'}
    elif header == 'Connection':
        return {header: 'keep-alive'}
    elif header == 'X-Powered-By':
        return {header: 'Express'}
    elif header == 'Access-Control-Allow-Credentials':
        return {header: 'true'}
    elif header == 'Accept':
        return {header: '*/*'}
    elif header == 'Accept-Encoding':
        return {header: 'gzip, deflate, br'}
    elif header == 'X-Content-Type-Options':
        return {header: 'nosniff'}
    elif header == 'Content-Encoding':
        return {header: 'br'}
    elif header == 'CF-Cache-Status':
        return {header: 'HIT'}
    elif header == 'all':
        return {'Content-Type': 'application/json; charset=UTF-8',
                'Transfer-Encoding': 'chunked',
                'Connection': 'keep-alive',
                'X-Powered-By': 'Express',
                'Access-Control-Allow-Credentials': 'true',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'X-Content-Type-Options': 'nosniff',
                'Content-Encoding': 'br',
                'CF-Cache-Status': 'HIT',
                }
    else:
        return {None: None}