from random import choice as random_choice


class Ask:

    def __init__(self, answers: tuple = None):
        if answers is not None:
            self.answers = answers
        else:
            # default acceptable answers
            self.answers = (
                "As I see it, yes.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don’t count on it.",
                "It is certain.",
                "It is decidedly so.",
                "Most likely.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Outlook good.",
                "Reply hazy, try again.",
                "Signs point to yes.",
                "Very doubtful.",
                "Without a doubt.",
                "Yes.",
                "Yes – definitely.",
                "You may rely on it.",
            )

    def get_answer(self):
        return random_choice(self.answers)
