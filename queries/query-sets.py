class QuerySets:
    def __init__(self, *data):
        self._data = data

    def __iter__(self):
        return iter(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def delete(self):
        # todo
        pass

    def contains(self):
        # todo
        pass

    def count(self):
        # todo
        pass

    def distinct(self):
        # todo
        pass

    def exists(self):
        # todo
        pass

    def earliest(self):
        # todo
        pass

    def latest(self):
        # todo
        pass

    def first(self):
        # todo
        pass

    def last(self):
        # todo
        pass

    def order_by(self):
        # todo
        pass

    def reverse(self):
        # todo
        pass