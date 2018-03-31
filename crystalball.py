from flask import Flask, render_template, request
import random

app = Flask(__name__)
PAGE_TITLES = []
BOOK_OF_PROPHECIES = []
with open('titles.txt') as f:
    for line in f:
        PAGE_TITLES.append(line.strip())
with open('prophecies.txt') as f:
    for line in f:
        BOOK_OF_PROPHECIES.append(line.strip())

@app.route('/')
def stuff():
    prophecy = random.choice(BOOK_OF_PROPHECIES)
    title = random.choice(PAGE_TITLES)
    print()
    try:
        print(' ' + chr(0x1f4bb) + ' ' + request.headers['X-Real-IP'])
    except:
        print(' ' + chr(0x1f4bb) + ' ???')
    print(' ' + chr(0x1f52e) + ' ' + prophecy)
    return render_template('index.html', title=title, prophecy=prophecy)

@app.after_request
def gnu_terry_pratchett(resp):
    resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
    return resp

if __name__ == '__main__':
    app.run()

