import random
import time

def generate_word(length):
    word = ''
    for i in range(length):
        word += random.choice('abcdef0123456789')
    return word

def run_game():
    print('タイピングゲームを始めます。')
    time.sleep(1)

    score = 0
    while True:
        word = generate_word(5)
        print('次の単語をタイプしてください: {}'.format(word))
        start_time = time.time()
        user_input = input().strip()
        end_time = time.time()

        if user_input == word:
            time_taken = end_time - start_time
            score += int(5 / time_taken)
            print('正解です。得点: {}'.format(score))
        else:
            print('間違いです。')

        time.sleep(1)

if __name__ == '__main__':
    run_game()
