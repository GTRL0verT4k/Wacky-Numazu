import random

def message():
    messages = [
        "おっと、風が強くなってしまいました！もう一度挑戦してください！",
        "あれ、何かがあなたの注意を引きました！もう一度挑戦しましょう！",
        "ははは、あなたがトロールの罠にかかりました！もう一度予想してみてください！",
        "アブラカダブラ！あなたの予想は空中に消えました！もう一度見つけられるかな？",
        "おやおや、話すリスがあなたの予想を盗みました！新しい予想を作りましょう！",
    ]
    return random.choice(messages)

def play_game():
    target_number = random.randint(1, 20)
    attempts = 0

    print("ようこそ、ワクワク数字当てゲームへ！")
    print("1から20の間で秘密の数字を選びました。")
    print("それが何か当ててみましょう！楽しい驚きが待っています！\n")

    while True:
        guess = int(input("ワクワクした予想を教えてください："))
        attempts += 1

        if guess < target_number:
            print("うわーっ！予想が低すぎます！もっと大胆に行きましょう！")
            print(message() + "\n")
        elif guess > target_number:
            print("まさか！予想が宇宙の彼方です！もう少し控えめにしましょう！")
            print(message() + "\n")
        else:
            print("\nおめでとうございます！ワクワクする数字を見つけました！")
            print(f"あなたは{attempts}回でこの素晴らしい数字を発見しました！")
            break

    print("\nワクワク数字当てゲームをプレイしていただきありがとうございました！")
    print("日常生活でもワクワクを忘れず")

play_game()