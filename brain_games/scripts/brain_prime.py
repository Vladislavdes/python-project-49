from ..engine import engine


def main():
    """run brain-prime"""
    game = 'brain-prime'
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(game, rules)