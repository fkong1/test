import abc

class DB:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def exists(self, key):
        pass

    @abc.abstractmethod
    def put(self, key, val):
        pass

    @abc.abstractmethod
    def delete(self, key):
        pass

    @abc.abstractmethod
    def count(self):
        pass

class InMemoryDB(DB):
    def __init__(self):
        self._store = {}
    
    def get(self, key):
        return self._store.get(key)

    def exists(self, key):
        return self._store.has_key(key)

    def put(self, key, val):
        repalced = self._store.has_key(key)
        self._store[key] = val
        return repalced

    def delete(self, key):
        if self._store.has_key(key):
            del self._store[key]
            return True
        return False
    
    def count(self):
        return len(self._store)
