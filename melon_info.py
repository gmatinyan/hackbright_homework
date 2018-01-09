"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melons):
    """Print melons."""

    for melon, parametrs in melons.items():
        print melon.upper()
        for parametr, value in parametrs.items():
            print "{} : {}".format(parametr, value)
        print "\n"


print_melons(melons)
