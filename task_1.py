import unittest

def title(input: str) -> str:

    words = input.split() # Создаем список слов без пробелов
    result = input # Копируем строку для того, чтобы вставлять в нее замену
    for word in words:
        result = result.replace(word, word[0].upper() + word[1:], 1) # Заменяем каждое слово в строке на слово с заглавной буквой

    return result


class TestTitle(unittest.TestCase):

    def test_basic(self):  # Пример из задания
        self.assertEqual(title("тесТОвое задание   для pt"), "ТесТОвое Задание   Для Pt")

    def test_empty_string(self): #Пустая строка
        self.assertEqual(title(""), "")

    def test_single_word(self):#Строка, состоящая из одного слова
        self.assertEqual(title("слово"), "Слово")

    def test_all_uppercase(self):
        self.assertEqual(title("ТЕСТ"), "ТЕСТ") #Строка, где все буквы уже заглавные

    def test_no_spaces(self): #Строка, где нет пробелов
        self.assertEqual(title("тестоваястрока"), "Тестоваястрока")

    def test_multiple_spaces(self): #Строка, где слова разделены несколькими пробелами
        self.assertEqual(title("несколько   пробелов  aaa"), "Несколько   Пробелов  Aaa")

    def test_mixed_case(self): # Строка со смешанным регистром
        self.assertEqual(title("смЕшанНый РеГиСтР"), "СмЕшанНый РеГиСтР")

    def test_numerics_with_symbols(self):# Строка с цифрами
        self.assertEqual(title("123 тест!"), "123 Тест!")

def main():
    unittest.main()

if __name__ == '__main__':
    main()


