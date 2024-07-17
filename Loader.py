import numpy as np

def load(wordLen):
    answerBank = 'WordBank/'
    guessBank  = 'WordBank/'

    match wordLen:
        case 4:
            answerBank += '4-letter-words.txt'
            guessBank  += '4-letter-words.txt'
        case 5:
            answerBank += 'wordle-answers.txt'
            guessBank  += 'wordle-guesses.txt'
        case _:
            answerBank += 'wordle-answers.txt' # make this default behavior for now
            guessBank  += 'wordle-guesses.txt'

    with open(answerBank, 'r') as answerFile, open(guessBank, 'r') as guessFile:
        answers = np.array([line.strip().lower() for line in answerFile])
        guesses = np.array([line.strip().lower() for line in guessFile])

    return answers, guesses