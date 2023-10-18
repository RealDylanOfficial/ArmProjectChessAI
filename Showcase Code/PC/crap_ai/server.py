from email import message
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
# Further documentation may be found via ( right-click variable, method, etc -> Go to Definition ) using the VSC Python Extension.


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  """
  HTTPRequestHandler class
  Initalizes class for use in HTTP server, in order to send the chess board as a header to front-end. Link to HTTP Server Doc: https://docs.python.org/3/library/http.server.html#http.server.HTTPServer.
  """

  # GET is a standard method for requested HTTP server class.
  def do_GET(self):
    # Send response status code.
    self.send_response(200)

    # Send chess board message back to client.
    message = bytes(
    #   str(self.headers) +
    #   "\n" +
    #   self.requestline +
    #   "\n"
 """BR BN BB BQ BK BB BR BR
    BP BP BP BP .. BP BP BP
    .. .. .. .. .. .. .. ..
    .. .. .. WP BP .. .. ..
    .. .. .. .. .. .. .. ..
    .. .. .. .. .. .. .. ..
    WP WP WP .. WP WP WP WP
    WR WN WB .. WK WB WN WR"""
      , 'utf8')

    # Sends HTTP headers first defining the type of content as plaintext character utf-8, with the length equal to the message. Documentation: https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.send_header
    self.send_header('Content-type','text/plain; charset=utf-8') 
    self.send_header('Content-length', str(len(message))) 
    self.end_headers() # Required end_headers.

    # Write content as utf-8 data.
    self.wfile.write(message)
    return

# Function to start Server.
def run(): 
  print('starting server...')

  # Settings for Server.
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access.
  server_address = ('127.0.0.1', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler) # HTTPServer inherits testHTTPServer_RequestHandler and uses standard function do_GET.
  httpd.serve_forever() # Starts Server.
  print('running server...')


run() # Execution of run thus starting the server.
