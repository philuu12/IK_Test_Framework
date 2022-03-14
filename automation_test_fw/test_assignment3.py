# HW3: Create testcases using my own Test Framework
import pytest
import sys
sys.path.insert(0, '.')

from util_lib.gen_endpoint import generate_endpoint
from util_lib.gen_request import gen_http_request
from util_lib.make_request import make_http_request
from util_lib.parse_output import parse_output
from util_lib.gen_header import generate_header
from util_lib.gen_data import gen_data


@pytest.mark.hw3
def test_1_get_all_posts():
#     endpoint = generate_endpoint(front_resource="posts")
#     http_req_url = gen_http_request(base_url="https://jsonplaceholder.typicode.com/", end_point=endpoint)
#     response = make_http_request("GET", url=http_req_url)
#     parse_output(response)
    pass

