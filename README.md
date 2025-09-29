# EX01 Developing a Simple Webserver
## Date:24.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Sample</title>
    </head>
    <body>
        <h1 align="center"><b>Device Description-Madhumitha V-25016067</b></h1>
        <table border="3" cellspacing="5" cellpadding=""10>
            <tr> 
                <th>S.No.</th>
                <th>Device specifications</th>
                <th>Description</th>
            </tr>
            <tr>
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
```

## OUTPUT:
![alt text](<Screenshot (19).png>)
![alt text](<Screenshot (21).png>)




## RESULT:
The program for implementing simple webserver is executed successfully.
