from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    if polarity >= friendly_threshold:
        return Mood('GOOD', polarity)
    elif polarity <= hostile_threshold:
        return Mood('Angry', polarity)
    else:
        return Mood('neutral', polarity)


def run_bot():
    interaction = True
    print("How do you feel today?:  ")
    while interaction:
        user_input: str = input('You: ')
        # mood: Mood('neutral', polarity)
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f"Bot: {mood.emoji} {mood.sentiment}")
        if user_input == "goodbye":
            print('see you next time!')
            interaction = False


if __name__ == '__main__':
    run_bot()
