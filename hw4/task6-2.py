some_list = ["a", "b", "c", "d", "e", "f", "g"]
some_list_iterator = iter(some_list)


def iter_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


iter_loop(some_list)
