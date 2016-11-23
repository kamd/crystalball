from flask import Flask, render_template, request
import random

app = Flask(__name__)
PAGE_TITLES = [
    '420 GAZE IT',
    'LIBERI FATALI',
    'SPHERE OF NOSTRADAMUS',
    'BALL OF THE ORACLE',
    'ORB OF THE SEER',
    'EYE OF FATE',
    'GLOBE OF CLAIRVOYANCE',
    'SEE THE FUTURE',
    'TOMORROW\'S FATE, TODAY',
    'THE OMNISCIENT SPHEROID',
    'A VISION OF INEVITABILITY',
    'THE PREDETERMINED RESULT OF YOUR FREE WILL',
    'EVENTS SOON TO COME',
    'HISTORY\'S EVIL TWIN',
    'TALES FROM YOUR GRAVE',
    'THE UNALTERABLE TIMELINE'
    ]
BOOK_OF_PROPHECIES = [
    'You will reign supreme.',
    'You will be cursed by an imp.',
    'You will obtain mediocre wealth.',
    'You will be thwarted at every turn.',
    'You will master a skill of marginal utility.',
    'You will ascend to your planar form.',
    'The skeleton living inside you will sieze control.',
    'You are become Death, the destroyer of worlds.',
    'You will find a dropped banknote, and then promptly lose it.',
    'You will worry what people think of you, when they do not.',
    'You will study the chaos between worlds, and get a 2:2.',
    'You will travel slowly and steadily forwards through time.',
    'You will never reach your potential.',
    'Your identity will be corrupted by your 15 minutes of fame.',
    'You will take two steps forward, two steps back.',
    'You will claim a Pyrrhic victory.',
    'You will live a long and hedonistic life.',
    'You will burn twice as bright, half as long, and die in a wax puddle.',
    'You will live forever as a crudely digitised A.I. facsimilie.',
    'You will live many varied and interesting lives, thanks to cloning.',
    'Your life will be the median of all lives.',
    'Pleasure will be your undoing.',
    'You will bring about a calamity from the skies.',
    'You will be hoisted by your own petard.',
    'You will outlive suspiciously many spouses.',
    'You will be an unwilling participant in the Human Instrumentality Project.',
    'You will never use the coupons you save.',
    'You will commit the perfect murder and be saddened when nobody finds out.',
    'You will remain a cog, and be interchanged.',
    'With divine blood on your hands, you will found the Republic of Heaven.',
    'You will be comforted by the dwindling happiness of others.',
    'You will live for sleep, for there you can dream.',
    'You will win the silver medal.',
    'You will repeat the mistakes of history.',
    'You will nudge forward the boundary of inconsequential human knowledge.',
    'You will get a good grasp on how the world is, only for it to change.',
    'You will lower your expectations and be satisfied.',
    'You will play a small part in your civilisation\'s downfall.',
    'You will slowly accrue, and then be purged from, database records.',
    'You will promote boundless and infinite synergy.',
    'You will become the best, through attrition.',
    'You will live off the compound interest of a lucky mistake.',
    'You will search for meaning that isn\'t there.',
    'You will pull up the ladder behind you, then pour boiling oil where it used to be.',
    'You will be the last of the pre-immortals.',
    'You will forever dwell on the path not taken.',
    'You will hedge your bets until rewards are minimal.',
    'You will reach for the stars, and find lightyears of void.',
    'You will waste what little youth remains.',
    'You and your friends will become different people.',
    'You will be amused by a joke nobody else would understand.',
    'You will be bought out by Google.',
    'You will become a well-known cautionary case study.',
    'You will continue to serve your feudal masters until death.',
    'You will mispronounce a word that nobody will ever correct you on.',
    'You will fail to meet Wikipedia\'s notability threshold.',
    'You will reach the top of the bell curve.',
    'You will unknowingly follow the path of least resistance.',
    'You will be replaced by a Markov chain, and nobody will notice.',
    'You will be overlooked for superficial reasons.',
    'You will defy your fate.',
    'You will be a poster child for cognitive dissonance.',
    'You will be unfairly stereotyped in a Hollywood biopic of an acquaintance.',
    'You will win the battle, and lose the war on drugs.',
    'You will not live long enough to see yourself become the villain.',
    'You will win the war, and lose the election.',
    'You will set a trend, but be mistaken for a hipster.',
    'You will become uncomfortably aware of the Old Ones.',
    'You will be forgotten within a century.',
    'You will loop through time forever, unable to alter it.',
    'You will pretend not to see the frayed edges of reality.',
    'You will remain unequipped to express your groundbreaking mathematical insight.',
    'You will become bored by the eternal fires of Hell.',
    'You will make a demonic pact for a mundane financial instrument.',
    'You will remain blissfully unaware of the bigger picture.',
    'You will study the arcane, and finally disprove it.',
    'You will alienate yourself by overexamining the rules of social interaction.',
    'You will always define yourself by the pop culture of your teenage years.',
    'You will die discovering a new physical constant.',
    'An exotic medical condition will be named after you.',
    'You will be responsible for a new paragraph in obscenity laws.',
    'You will discover reality is a simulation, and keep going through the motions.',
    'You will be contacted by aliens, and write it off as insanity.',
    'You will be disappointed in your next consumer purchase.',
    'You will not be able to distinguish this week from the next.',
    'You will leave your comfort zone long after it would have helped.',
    'You will waste your time on a web app nobody will look at.',
    'You will be scarred by the realisation that everything is a seething cloud of atoms.',
    'You will make them all pay for what they\'ve done.',
    'Your job will soon be done better by robots.',
    'You will live normally, bar the occasional ritualistic murders.',
    'You will enjoy your life as the flame-wreathed  avatar of Makhleb.',
    'You will devote your life to an apathetic deity.',
    'You will be stuck in traffic',
    'Your love of tea will unmake you.',
    'You will soon realise that nobody else has consciousness.',
    'You are a willless marionette, acting out your script.',
    'You will risk it all, and win an addiction to gambling.'
]

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
