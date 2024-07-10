import http.server
import threading


# Define a new HTTP request handler class
class CachingHandler(http.server.BaseHTTPRequestHandler):
    # Initialize the cache as an empty dictionary
    cache = {}

    # Override the do_GET() method
    def do_GET(self):
        if self.path in self.cache:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.cache[self.path])
            print("using cached response", self.path)
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = f"Hello {self.path}!".encode("utf-8")
            self.cache[self.path] = message
            self.wfile.write(message)
            print("generated response", self.path)


# Create a server that uses the request handler class
if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, CachingHandler)
    print(f"Serving on port {server_address[1]}...")

    # Serve in the background until any key is pressed
    import threading
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    input("Press any key to stop the server.")
    httpd.shutdown()
    print("Server stopped.")
