from english_words import english_words_lower_alpha_set
from collections import defaultdict
import numpy as np
import re


def get_feedback(wrong, close, correct, guess):
    feedback = ''
    while not re.match(r"[012]{5}", feedback):
        feedback = input('Feedback: ')

    for i, v in enumerate(feedback):
        v = int(v)
        if v == 0:
            if not guess[i] in ''.join([y for x in close.values() for y in x]):
                wrong.add(guess[i])
        elif v == 1:
            close[i].append(guess[i])
        else:
            correct[i] = guess[i]


def filter_options(options, wrong, misplaced, knowns):
    regex = ""
    for i in range(5):
        if i in knowns.keys():
            regex += knowns[i]
        else:
            regex += '[^' + ''.join(wrong)
            if i in misplaced.keys():
                regex += ''.join(misplaced[i])
            regex += ']'
    r = re.compile(regex)
    filtered = list(filter(r.search, options))
    mis = [y for x in misplaced.values() for y in x]
    f = list(filter(lambda x: all(c in x for c in mis), filtered))
    return f


def score_word(word, freq):
    try:
        return sum([freq[x] for x in word])
    except KeyError:
        return 0


def main():
    freq = {}
    with open("freq.csv") as file:
        for line in file.readlines():
            a = str(line.rstrip()).split(',')
            freq[a[0].lower()] = float(a[1])

    options = []
    with open("words.csv") as file:
        for line in file.readlines():
            options.append(line.rstrip())

    # these are all pretty good starting words and we pick one at random to keep things fresh
    guess = np.random.choice(['salet', 'reast', 'crate', 'trace'], 1)[0]
    print("Guess 1:", guess)

    wrong = set()
    close = defaultdict(list)
    correct = {}

    for g in range(5):
        print('-'*20)
        get_feedback(wrong, close, correct, guess)
        if len(correct.keys()) == 5:
            print("Congrats, Wordle cracked!")
            break

        options = filter_options(options, wrong, close, correct)
        options.sort(key=lambda x: score_word(x, freq), reverse=True)
        print(options)
        valid = False
        while not valid:
            guess = options.pop(0)
            print(f'Guess {g + 2}: {guess}')
            state = ''
            while state not in ['y', 'n']:
                state = input('Was valid word? [y/n] ')
            valid = state == 'y'


if __name__ == '__main__':
    main()
