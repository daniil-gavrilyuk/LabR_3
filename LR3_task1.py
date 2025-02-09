class Book:
    """ Базовый класс книги. """
    def init(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self):
        """Свойство для получения названия книги."""
        return self._name
    @property
    def author(self):
        """Свойство для получения автора книги."""
        return self._author
    def str(self):
        return f"Книга {self.name}. Автор {self.author}"
    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r})"
class PaperBook(Book):
    """Класс бумажной книги."""
    def init(self, name: str, author: str, pages: int):
        super().init(name, author)
        self.pages = pages
    @property
    def pages(self):
        """Свойство для получения количества страниц."""
        return self._pages
    @pages.setter
    def pages(self, value: int):
        """Свойство для установки количества страниц с проверкой."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value
    def str(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"
    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"
class AudioBook(Book):
    """Класс аудиокниги."""
    def init(self, name: str, author: str, duration: float):
        super().init(name, author)
        self.duration = duration
    @property
    def duration(self):
        """Свойство для получения продолжительности аудиокниги."""
        return self._duration
    @duration.setter
    def duration(self, value: float):
        """Свойство для установки продолжительности с проверкой."""
        if not isinstance(value, float) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом с плавающей запятой.")
        self._duration = value

    def str(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
