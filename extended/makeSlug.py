from random import randrange
import string


def make_slug():
    data=data=list(string.hexdigits)+list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(string.digits)
    def random_num():
        return randrange(0,83,1)
    return f'{data[random_num()]}{data[random_num()]}{data[random_num()]}{data[random_num()]}{data[random_num()]}{data[random_num()]}{data[random_num()]}{data[random_num()]}'


