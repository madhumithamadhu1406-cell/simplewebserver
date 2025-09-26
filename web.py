from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
r="3" cellspacing="5" cellpadding=""10>
            <tr> 
                <th>S.No.</th>
                <th>Device specifications</th>
                <th>Description</th>
            </tr>
            <tr><html>
    <head>
        <title>Sample</title>
    </head>
    <body>
        <h1 align="center"><b>Device Description-Madhumitha V-25016067</b></h1>
        <table borde
                <td>1</td>
                <td>Storage</td>
                <td>954GB</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Graphics card</td>
                <td>128GB</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed Ram</td>
                <td>160GB</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Processor</td>
                <td>Intel(R)Core(TM)Ultra 5 125H</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Device Name</td>
                <td>LAPTOP-S2BBC0Q4</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()