from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():     
    return "<p>Hello world!</p>"

#de beide regels hieronder moeten altijd de laatste van het hoofdbestand zijn
if __name__ == '__main__':    
    app.run(port=5000,debug=True)