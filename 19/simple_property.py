from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name=str, expires=datetime):
        self.name = name
        self.expires = expires
        self._expired = NOW

    @property
    def expired(self):
        return bool(self._expired)
