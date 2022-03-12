# Parse output
# def parse_output(response, search_key=None, expected_id_number=None, expected_json_response=None):
def parse_output(response, expected_resp_dict=None, expected_neg_resp_code=None):
    msg_200 = "200 (OK): This code indicates that the request was made successfully."
    msg_201 = "201 (Created): This response code indicates that the request was successful and a resource was created. It is used to confirm the success of a PUT or POST request."
    msg_400 = "400 (Bad Request): This code indicates that the data is in an incorrect format."
    msg_401 = "401 (Unauthorized): This code indicates an authentication error."
    msg_405 = "405 (Method Not Allowed): This code indicates that the HTTP method used is not supported for this resource."
    msg_409 = "409 (Conflict): This code indicates that there is a conflict request to create the same resource twice."
    msg_404 = "404 (Not Found): This code indicates that the required resource could not be found."
    msg_500 = "500 (Internal Server Error): This code indicates that there is some error on the server-side."
    msg_negative = "FAILED: Negative testing with actual responce code "
    msg_unknown = "Unknown code response"

    if expected_resp_dict is None:
        expected_resp_dict = {}

    if expected_resp_dict:
        for search_key, search_val in expected_resp_dict.items():
            assert response.json()[search_key] == search_val

    act_resp_code = response.status_code

    if expected_neg_resp_code:
        assert expected_neg_resp_code == act_resp_code, msg_negative + str(act_resp_code)
    else:
        if act_resp_code == 200:
            assert True, msg_200
        elif act_resp_code == 201:
            assert True, msg_201
        elif act_resp_code == 400:
            assert False, msg_400
        elif act_resp_code == 401:
            assert False, msg_401
        elif act_resp_code == 404:
            assert False, msg_404
        elif act_resp_code == 405:
            assert False, msg_405
        elif act_resp_code == 409:
            assert False, msg_409
        elif act_resp_code == 500:
            assert False, msg_500
        else:
            assert False, msg_unknown

