from loguru import logger
import sqlite3


class DataBase:
    @logger.catch
    def __init__(self):
        """Подключение и курсор"""
        self.connection = sqlite3.connect("utils/db_api/db.db")
        self.cursor = self.connection.cursor()

    @logger.catch
    def add_new_telegram_user(self, tg_id, tg_name) -> None:
        if (self.get_all_by_tg_id(tg_id) == []):
            with self.connection:
                self.cursor.execute(
                    "INSERT INTO users(tg_id, tg_name) VALUES (?, ?)", (tg_id, tg_name)
                )

    @logger.catch
    def get_all_by_tg_id(self, tg_id):
        with self.connection:
            return self.cursor.execute(
                "SELECT * FROM users WHERE tg_id = ?", (tg_id,)
            ).fetchall()
