def compress(iterable, masks):
    for item, mask in zip(iterable,masks):
        if mask:
            yield item


def cycle(iterable):
    var=""
    while True:
        for item in iterable:
            var = "{}{}".format(var, item)
            yield var


def chain(iterable_one, iterable_two):

    for item in iterable_one:
        yield item
    for item in iterable_two:
        yield item
