from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{ 
                margin: 10px 0;
                width: 540px;
                height: 120px; 
            }} 
        </style> 
    </head>
    <body>
    <form method="POST">
             <label>Rotate by:
             <input  type="text" name="rot" value='0'></label><br/>
             <textarea rows="5" cols="50" name="text">{0}</textarea><br/>
             
             <input type="Submit">
      
        </form>
      
    </body>
</html>
"""

   
@app.route("/")
def index():
    # return form
    return form.format("")

@app.route("/", methods=['POST'])
def encrypted():
    rot = int(request.form["rot"])
    text = (request.form ["text" ])
    return "<h1>" + form.format(encrypt(text,rot))+ "</h1>"
    
#form.format
app.run()