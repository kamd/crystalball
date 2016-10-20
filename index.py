from flask import Flask, render_template
import random

app = Flask(__name__)
BOOK_OF_PROPHECIES = [
    'You will reign supreme.',
    'You will be cursed by an imp.',
    'You will obtain mediocre wealth.',
    'You will be thwarted at every turn.',
    'You will master a skill of marginal utility.',
    'You will ascend to your planar form.',
    'The skeleton living inside you will sieze control.',
    'You are become Death, Destroyer of Worlds.',
    'You will find an abandoned banknote, and then promptly lose it.',
    'You will study the chaos between worlds, and get a 2:2.',
    'You will travel slowly and steadily forwards through time.'
]

@app.route('/')
def stuff():
    prophecy = random.choice(BOOK_OF_PROPHECIES)
    return render_template('index.html', prophecy=prophecy)

if __name__ == '__main__':
    app.run()
