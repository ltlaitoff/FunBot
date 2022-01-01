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

    @logger.catch
    def get_all_by_user_id(self, user_id):
        with self.connection:
            return self.cursor.execute(
                "SELECT * FROM users WHERE id = ?", (user_id,)
            ).fetchall()

    @logger.catch
    def get_all_by_tg_id(self, tg_id):
        with self.connection:
            return self.cursor.execute(
                "SELECT * FROM users WHERE tg_id = ?", (tg_id,)
            ).fetchall()

    @logger.catch
    def update_user_lol_data(self, tg_id, lol_puuid, lol_name):
        with self.connection:
            return self.cursor.execute(
                "UPDATE users SET lol_puuid = ?, lol_name = ? WHERE tg_id = ?", (
                    lol_puuid, lol_name, tg_id)
            )

    @logger.catch
    def get_user_id_by_puuid(self, puuid):
        with self.connection:
            return self.cursor.execute(
                "SELECT id FROM users WHERE lol_puuid = ?", (puuid,)
            ).fetchall()

    @logger.catch
    def get_last_user_match(self, user_id):
        with self.connection:
            return self.cursor.execute(
                "SELECT match_id FROM matchs WHERE user_id = ?", (user_id,)
            ).fetchall()

    @logger.catch
    def add_new_match(self, user_id, match_id, date, champion, kills, deaths, assists) -> None:
        with self.connection:
            self.cursor.execute(
                "INSERT INTO matchs(user_id, match_id, date, champion, kills, deaths, assists) VALUES (?, ?, ?, ?, ?, ?, ?)", (
                    user_id, match_id, date, champion, kills, deaths, assists)
            )

    @logger.catch
    def add_new_record_in_history(self, user_id, data, value, current_coef, result_pull_ups, global_pull_ups) -> None:
        with self.connection:
            self.cursor.execute(
                "INSERT INTO history(user_id, data, value, current_coef, result_pull_ups, global_pull_ups) VALUES (?, ?, ?, ?, ?, ?)", (
                    user_id, data, value, current_coef, result_pull_ups, global_pull_ups)
            )

    @logger.catch
    def update_user_pull_ups(self, user_id, pull_ups) -> None:
        with self.connection:
            self.cursor.execute(
                "UPDATE users SET pull_ups = ?", (pull_ups,)
            )

    @logger.catch
    def get_all_users(self):
        with self.connection:
            return self.cursor.execute(
                "SELECT * FROM users"
            ).fetchall()
