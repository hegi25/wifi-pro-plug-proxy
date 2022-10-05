import http.server
import socketserver
from http import HTTPStatus
from data import *
from inverter import update

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if update():
            self.send_response(HTTPStatus.OK)
            output = b""
            output += "Input_AC_Voltage ".encode() + LastData.Input_AC_Voltage + b"\n"
            output += "Input_AC_Frequency ".encode() + LastData.Input_AC_Frequency + b"\n"
            output += "Output_AC_Voltage ".encode() + LastData.Output_AC_Voltage + b"\n"
            output += "Output_AC_Frequency ".encode() + LastData.Output_AC_Frequency + b"\n"
            output += "Load_In_Watt ".encode() + LastData.Load_In_Watt + b"\n"
            output += "Battery_Voltage ".encode() + LastData.Battery_Voltage + b"\n"
            output += "PV_Input_Voltage ".encode() + LastData.PV_Input_Voltage + b"\n"
            output += "PV_Input_Watt ".encode() + LastData.PV_Input_Watt + b"\n"
            self.send_header('Content-Length', str(len(output)))
            self.send_header('Content-Type', "text/plain") 
            self.end_headers()
            self.wfile.write(output)


def start_prometheus():
    httpd = socketserver.TCPServer(('', 5000), Handler)
    # Start up the server to expose the metrics.
    httpd.serve_forever()
    # Generate some requests.
    while True:
        httpd.process_request()
