from ask_ron.ask import Ask


class TestAsk:
    def setup_class(self):
        self.default_answers = (
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
        self.custom_answers = (
            "Yerp",
            "Nerp"
        )

    def test_default_init(self):
        ask_default = Ask()
        assert self.default_answers == ask_default.answers

    def test_custom_init(self):
        ask_custom = Ask(answers=self.default_answers)
        assert self.default_answers == ask_custom.answers

    def test_get_answer(self):
        ask_custom = Ask(answers=self.default_answers)
        assert ask_custom.get_answer() in self.custom_answers
