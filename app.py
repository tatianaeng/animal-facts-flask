from flask import Flask, render_template

app = Flask(__name__)

animal_facts = {"dog": "Dogs have a sense of smell that is 40 times better than humans!",
"cat": "Cats sleep for an average of 13 to 16 hours a day!", 
"elephant": "Elephants can 'hear' with their feet by picking up vibrations in the ground."
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/fact/<animal>')
def fact(animal):
	fact = animal_facts.get(animal.lower(), "Sorry, I don't have a fact for that animal.")
	return render_template("fact.html", animal=animal, fact=fact)

if __name__ == '__main__':
    app.run(debug=True)

