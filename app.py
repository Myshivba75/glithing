import Flask

app = Flask(__name__)

@app.route('/')

def tst():
    return "Hi am viky"

if __name__ == "__main__":
	app.run()    