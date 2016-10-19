from flask import Flask, render_template
import random

app = Flask(__name__)
BOOK_OF_PROPHECIES = [
    'You will reign supreme.',
    'You will be cursed by an imp.',
    'You will obtain mediocre wealth.',
    'You will be thwarted at every turn.',
    'You will master a skill of marginal utility.',
    'You will ascend to your planar form.'
]

@app.route('/crystal')
def stuff():
    prophecy = random.choice(BOOK_OF_PROPHECIES)
    return render_template('index.html', prophecy=prophecy)

if __name__ == '__main__':
    app.run()
