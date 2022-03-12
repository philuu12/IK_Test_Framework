# Generate endpoint
# Path parameters are found within the path of the endpoint before the query string (?)


def generate_endpoint(front_resource, id="", back_resource=""):
    if id:
        return front_resource + "/" + str(id) + "/" + back_resource
    else:
        return front_resource + "/"