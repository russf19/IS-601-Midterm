class History:
    _history = []

    @classmethod
    def add_history(cls, record):
        cls._history.append(record)

    @classmethod
    def get_history(cls):
        return cls._history

    @classmethod
    def clear_history(cls):
        cls._history.clear()
