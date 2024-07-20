import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sqlite3
import os

# Импортируем функции из основного файла
from ebay_tracker import get_ebay_data, store_data


class TestEbayScraper(unittest.TestCase):

    @patch("ebay_traker.requests.get")
    def test_get_ebay_data(self, mock_get):
        # Пример HTML для имитации ответа
        html = """
        <html>
        <body>
            <div class="s-item">
                <h3 class="s-item__title">Test Item 1</h3>
                <span class="s-item__price">$10.00</span>
                <a class="s-item__link" href="http://example.com/item1"></a>
            </div>
            <div class="s-item">
                <h3 class="s-item__title">Test Item 2</h3>
                <span class="s-item__price">$20.00</span>
                <a class="s-item__link" href="http://example.com/item2"></a>
            </div>
        </body>
        </html>
        """

        mock_get.return_value = MagicMock(status_code=200, text=html)

        keywords = "test"
        df = get_ebay_data(keywords)

        expected_data = {
            "title": ["Test Item 1", "Test Item 2"],
            "price": ["$10.00", "$20.00"],
            "link": ["http://example.com/item1", "http://example.com/item2"],
        }

        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)

    def test_store_data(self):
        # Пример данных
        data = {
            "title": ["Test Item 1", "Test Item 2"],
            "price": ["$10.00", "$20.00"],
            "link": ["http://example.com/item1", "http://example.com/item2"],
        }
        df = pd.DataFrame(data)

        # Имя тестовой базы данных
        db_name = "test_ebay_data.db"

        # Удаляем тестовую базу данных, если она существует
        if os.path.exists(db_name):
            os.remove(db_name)

        store_data(df, db_name)

        # Подключаемся к базе данных и проверяем сохраненные данные
        conn = sqlite3.connect(db_name)
        saved_df = pd.read_sql_query("SELECT * FROM items", conn)
        conn.close()

        pd.testing.assert_frame_equal(df, saved_df)

        # Удаляем тестовую базу данных
        os.remove(db_name)


if __name__ == "__main__":
    unittest.main()
