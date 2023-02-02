from http.server import BaseHTTPRequestHandler, HTTPServer
import json 
from views.user_requests import create_user, login_user
from views.categories_requests import get_all_catagories, create_category
from views.post_requests import get_all_posts, get_single_post, get_posts_by_user, delete_post, create_post, update_post
from urllib.parse import urlparse


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != '':
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods','GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers','X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        response = {}
        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            (resource, id, query_params) = parsed
            if resource == 'posts':
                self._set_headers(200)
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()

            # NEED TO HAVE A CONDITIONAL TO DISPLAY USER POSTS ON MY-POSTS PATH
            # if resource == 'my-posts':
            #     response = get_posts_by_user(query_params)

        else: # There is a ? in the path, run the query param functions
            (resource, query, query_params) = parsed

            if resource == 'posts':
                self._set_headers(200)
                    # success = True
            response = get_posts_by_user(query_params)

        if resource == 'categories':
            self._set_headers(200)
            response = get_all_catagories()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, id, query_params) = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'categories':
            response = create_category(post_body)
        if resource == 'posts':
            response = create_post(post_body)

        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id, query_params) = self.parse_url(self.path)

        # Delete a single order from the list
        if resource == "posts":
            # PLACEHOLDER BELOW FOR FUNCTION CREATION
            resource = update_post(id, post_body)

            self.wfile.write("".encode())


    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)
        (resource, id, query_params) = self.parse_url(self.path)

        # Delete a single order from the list
        if resource == "posts":
            delete_post(id)




def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
