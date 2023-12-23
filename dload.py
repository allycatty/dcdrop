import BaseHTTPServer
import SocketServer
import os

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Set the base directory to "./saves"
            base_dir = "./saves"
            # Get the requested path and join it with the base directory
            path = os.path.join(base_dir, self.path[1:])

            # Debug print statements
            print("Current working directory:", os.getcwd())
            print("Requested file path:", path)
            
            # If the path is a directory, generate an index
            if os.path.isdir(path):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                # List files in the directory and its subdirectories as links
                file_links = []
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = os.path.relpath(os.path.join(root, file), base_dir)
                        file_links.append('<li><a href="{0}">{0}</a></li>'.format(file_path))
                
                file_list = '<ul>{}</ul>'.format(''.join(file_links))
                index_page = '<html><body>{}</body></html>'.format(file_list)
                self.wfile.write(index_page)
                
            # If the path is a file, serve it with the appropriate MIME type
            elif os.path.isfile(path):
                # Convert the file extension to lowercase for case-insensitivity
                _, file_extension = os.path.splitext(path)
                file_extension = file_extension.lower()
                
                if file_extension == '.vmi':
                    mimetype = 'application/x-dreamcast-vms-info'
                elif file_extension == '.vms':
                    mimetype = 'application/x-dreamcast-vms'
                else:
                    self.send_error(404, 'File Not Found: {}'.format(self.path))
                    return

                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()

                with open(path, 'rb') as file:
                    self.wfile.write(file.read())
                    
            # If the path is not found, return a 404 error
            else:
                self.send_error(404, 'File Not Found: {}'.format(self.path))
                
        except Exception as e:
            self.send_error(500, 'Internal Server Error: {}'.format(str(e)))

def run(server_class=BaseHTTPServer.HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print 'Starting server on port {}'.format(port)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
