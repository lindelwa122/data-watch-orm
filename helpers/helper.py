from queries.query_set import QuerySet

def delete(data):
    # todo
    pass

def contains(data):
    # todo
    pass

def count(data):
    # todo
    pass

def distinct(data):
    # todo
    pass

def exists(data):
    # todo
    pass

def earliest(data):
    # todo
    pass

def latest(data):
    # todo
    pass

def first(data):
    # todo
    pass

def last(data):
    last_point = data[-1]
    return QuerySet(last_point)

def order_by(data):
    # todo
    pass

def reverse(data):
    # todo
    pass