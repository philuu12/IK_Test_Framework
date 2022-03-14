# HW3: Create testcases using my own Test Framework
import pytest
import sys
sys.path.insert(1, '..')

from util_lib.gen_endpoint import generate_endpoint
from util_lib.gen_request import gen_http_request
from util_lib.make_request import make_http_request
from util_lib.parse_output import parse_output
from util_lib.gen_header import generate_header
from util_lib.gen_data import gen_data
# from gen_endpoint import generate_endpoint
# from gen_request import gen_http_request
# from make_request import make_http_request
# from parse_output import parse_output
# from gen_header import generate_header
# from gen_data import gen_data

@pytest.mark.hw3
def test_1_get_all_posts(api):
    endpoint = generate_endpoint(front_resource="posts")
    http_req_url = gen_http_request(base_url=api, end_point=endpoint)
    response = make_http_request("GET", url=http_req_url)
    parse_output(response)


@pytest.mark.hw3
def test_2_get_one_postid_100(api):
    endpoint = generate_endpoint(front_resource="posts", id="100")
    http_req_url = gen_http_request(api, endpoint)
    response = make_http_request("GET", url=http_req_url)
    parse_output(response, expected_resp_dict={'id': 100, 'title': "at nam consequatur ea labore ea harum"})


@pytest.mark.hw3
def test_3_get_all_comments_under_postid_one(api):
    endpoint = generate_endpoint(front_resource="posts", id="1", back_resource="comments")
    http_req_url = gen_http_request(api, endpoint)
    response = make_http_request("GET", url=http_req_url)
    parse_output(response)


@pytest.mark.hw3
def test_4_get_all_comments_under_postid_one_2(api):
    endpoint = generate_endpoint(front_resource="comments?postId=1")
    http_req_url = api + endpoint
    response = make_http_request("GET", url=http_req_url)
    parse_output(response)


# --------------------
@pytest.mark.hw3
def test_5_get_all_photos_of_albumId_one(api):
    endpoint = generate_endpoint(front_resource="albums", id="1", back_resource="photos")
    http_req_url = gen_http_request(api, endpoint)
    response = make_http_request("GET", url=http_req_url)
    parse_output(response)


@pytest.mark.hw3
def test_6_get_all_albums_of_userId_one(api):
    endpoint = generate_endpoint(front_resource="users", id="1", back_resource='albums')
    http_req_url = gen_http_request(api, endpoint)
    response = make_http_request(method="GET", url=http_req_url)
    parse_output(response)


@pytest.mark.hw3
def test_7_get_all_todos_of_userId_one(api):
    endpoint = generate_endpoint(front_resource="users", id="1", back_resource="todos")
    http_req_url = gen_http_request(api, endpoint)
    response = make_http_request("GET", url=http_req_url)
    parse_output(response)


@pytest.mark.hw3
def test_8_get_all_posts_of_userId_one(api):
    endpoint = generate_endpoint(front_resource="users", id="1", back_resource="posts")
    http_req_url = gen_http_request(api, end_point=endpoint)
    response = make_http_request("GET", url=http_req_url)
    parse_output(response)


# -----------------
@pytest.mark.hw3
def test_9_post_new_post_with_no_postId(api):
    # http request
    end_point = generate_endpoint(front_resource="posts/")
    http_req_url = gen_http_request(api, end_point)

    # data
    title = "Create a new post with postID 45"
    body = "Contents here !!!"
    data = gen_data(title=title, body=body)

    # header
    header = generate_header("Content-Type")

    # response = requests.post(url=http_req_url, data=json.dumps(data), headers=header)
    response = make_http_request("POST", url=http_req_url, header=header, data=data)
    expected_response = {
                            "id": 101,
                            'title': "Create a new post with postID 45"
                        }
    parse_output(response, expected_resp_dict=expected_response)


@pytest.mark.hw3
def test_10_put_new_post_with_postId_1(api):
    # header
    header = generate_header(header='Content-Type')

    # http request
    end_point = generate_endpoint(front_resource="posts", id="1")
    http_req_url = gen_http_request(api, end_point)

    # data to be posted
    userId = 1
    title = "Create a new post with postID 1"
    body = "Discussion contents are posted here"
    data = gen_data(userId=userId, title=title, body=body)

    response = make_http_request("PUT", url=http_req_url, header=header, data=data)
    parse_output(response, expected_resp_dict={'id': userId, 'title': title, 'body': body})


@pytest.mark.hw3
def test_11_patch_album_one_title(api):
    # header
    header = generate_header(header='Content-Type')

    # http request
    end_point = generate_endpoint(front_resource="albums", id="1")
    http_req_url = gen_http_request(api, end_point)

    # data to be patched
    title = "No Title"
    data = gen_data(title=title)

    response = make_http_request("PATCH", url=http_req_url, header=header, data=data)
    parse_output(response)


@pytest.mark.hw3
def test_12_delete_postId_one(api):
    endpoint = generate_endpoint(front_resource="posts", id="1")
    http_req_url = gen_http_request(api, endpoint)
    response = make_http_request("DELETE", url=http_req_url)
    parse_output(response)


# ---------------------
# Negative tests
# ---------------------
@pytest.mark.hw3
def test_13_invalid_url(api):
    """Purpose: Misspelled endpoint "album" instead of "albums" """

    # http request
    end_point = generate_endpoint(front_resource="album")
    http_req_url = gen_http_request(api, end_point)

    response = make_http_request("GET", url=http_req_url)

    parse_output(response, expected_neg_resp_code=404)


@pytest.mark.hw3
def test_14_invalid_data(api):
    """ Purpose: Data dictionary is mistakenly/purposely empty to generate a non-200 response code """

    # header
    header = generate_header("Content-Type")

    # http request
    # end_point = gen_endpoint.generate_endpoint(front_resource="posts", id=101)
    end_point = generate_endpoint(front_resource="posts")
    https_req_url = gen_http_request(api, end_point)

    # data to be patched
    # data = gen_data.gen_data(userId=101)
    data = gen_data()

    # send request
    response = make_http_request("PUT", url=https_req_url, data=data, header=header)

    parse_output(response, expected_neg_resp_code=404)
