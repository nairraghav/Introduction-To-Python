from ask_ron.ask import Ask
VERSION = "1.0.0"


def main():
    ask_ronald = Ask()
    input("What is your question? ")
    print(ask_ronald.get_answer())
