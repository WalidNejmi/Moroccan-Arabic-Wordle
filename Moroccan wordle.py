import sys
import random

# كل ملف نصي يحتوي على 1000 كلمة
LISTSIZE = 1000

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

    # اختيار كلمة عشوائية لهذه اللعبة
    choice = random.choice(options)

    # السماح بتخمينة واحدة أكثر من طول الكلمة
    guesses = wordsize + 1
    won = False

    # طباعة الترحيب، باستخدام رموز الألوان ANSI للتوضيح
    print("\033[38;2;255;255;255;1m\033[48;2;106;170;100;1mهذه هي WORDLE50\033[0;39m")
    print(f"لديك {guesses} محاولات لتخمين كلمة {wordsize} حروف أفكر فيها")

    # الحلقة الرئيسية للعبة، تكرار لكل تخمينة
    for i in range(guesses):
        # الحصول على تخمينة المستخدم
        guess = get_guess(wordsize)

        # مصفوفة لحفظ حالة التخمينة، بداية مجموعاتها على 0
        status = [WRONG] * wordsize

        # حساب النقاط للتخمينة
        score = check_word(guess, wordsize, status, choice)

        print(f"التخمينة {i + 1}: ", end="")

        # طباعة التخمينة
        print_word(guess, wordsize, status)

        # إذا تخمينوا بشكل صحيح، توقف عن الحلقة
        if score == EXACT * wordsize:
            won = True
            break

    if won:
        print("لقد فزت!")
    else:
        print(f"الكلمة الصحيحة: {choice}")

if __name__ == "__main__":
    main()















