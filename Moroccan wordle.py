import sys
import random

# Each text file contains a maximum of 1000 words
# كل ملف نصي يحتوي على 1000 كلمة
LISTSIZE = 1000

# Values for colors and points (EXACT == correct letter, correct place; CLOSE == correct letter, wrong place; WRONG == wrong letter)
# قيم للألوان والنقاط (EXACT == الحرف الصحيح، في المكان الصحيح؛ CLOSE == الحرف الصحيح، في المكان الخطأ؛ WRONG == الحرف الخطأ)
EXACT = 2
CLOSE = 1
WRONG = 0

# دوال محددة المستخدم
def get_guess(wordsize):
    guess = ""
    while len(guess) != wordsize:
        guess = input(f"أدخل كلمة من {wordsize} أحرف: ")
    return guess

def check_word(guess, wordsize, status, choice):
    score = 0

    for k in range(wordsize):
        if choice[k] == guess[k]:
            status[k] = EXACT
            score += EXACT
        else:
            for l in range(wordsize):
                if guess[k] == choice[l]:
                    status[k] = CLOSE
                    score += CLOSE
                    break

    print(f"النقاط: {score}")
    return score

def print_word(guess, wordsize, status):
    for m in range(wordsize):
        if status[m] == EXACT:
            print("\033[38;2;255;255;255;1m\033[48;2;106;170;100;1m" + guess[m], end="")
        elif status[m] == CLOSE:
            print("\033[38;2;255;255;255;1m\033[48;2;201;180;88;1m" + guess[m], end="")
        else:
            print("\033[38;2;255;255;255;1m\033[48;2;220;20;60;1m" + guess[m], end="")
    
    # Reset print formatting to normal
    # إعادة تعيين خط الطباعة إلى الطبيعي
    print("\033[0;39m")
    print()

def main():

    wordsize = 5
    wl_filename = f"{wordsize}.txt"
    try:
        with open(wl_filename, "r") as wordlist:
            options = [word.strip() for word in wordlist.readlines()]
    except FileNotFoundError:
        print(f"خطأ في فتح الملف {wl_filename}.")
        return 1

    # Choose a random word for this game
    # اختيار كلمة عشوائية لهذه اللعبة
    choice = random.choice(options)

    # Allow one more guess than the length of the word
    # السماح بتخمينة واحدة أكثر من طول الكلمة
    guesses = wordsize + 1
    won = False

    # Print the welcome message, using ANSI color codes for emphasis
    # طباعة الترحيب، باستخدام رموز الألوان ANSI للتوضيح
    print("\033[38;2;255;255;255;1m\033[48;2;106;170;100;1mهذه هي WORDLE\033[0;39m")
    print(f"لديك {guesses} محاولات لتخمين كلمة {wordsize} حروف أفكر فيها")

    # Main game loop, iterating for each guess
    # الحلقة الرئيسية للعبة، تكرار لكل تخمينة
    for i in range(guesses):
        # Get user's guess
        # الحصول على تخمينة المستخدم
        guess = get_guess(wordsize)

        # Array to store guess status, initially all set to 0
        # مصفوفة لحفظ حالة التخمينة، بداية مجموعاتها على 0
        status = [WRONG] * wordsize

        # Calculate points for the guess
        # حساب النقاط للتخمينة
        score = check_word(guess, wordsize, status, choice)

        print(f"التخمينة {i + 1}: ", end="")

        # Print the guess
        # طباعة التخمينة
        print_word(guess, wordsize, status)

        # If guessed correctly, stop the loop
        # إذا تخمينوا بشكل صحيح، توقف عن الحلقة
        if score == EXACT * wordsize:
            won = True
            break

    if won: #YAY!
        print("لقد فزت!")
    else:
        print(f"الكلمة الصحيحة: {choice}")

if __name__ == "__main__":
    main()















