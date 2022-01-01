from loguru import logger
import sqlite3


class DataBase:
    @logger.catch
    def __init__(self):
        """Подключение и курсор"""
        self.connection = sqlite3.connect("utils/db_api/db.db")
        self.cursor = self.connection.cursor()

    @property
    def users(self):
        return Users(self.connection, self.cursor)


class Users:
    @logger.catch
    def __init__(self, connection, cursor):
        """Подключение и курсор"""
        self.connection = connection
        self.cursor = cursor

    # === Get ===
    def get_by_tg_id(self, tg_id):
        return self.__get('tg_id', tg_id)

    def get_by_lol_puuid(self, lol_puuid):
        return self.__get('lol_puuid', lol_puuid)

    def __get(self, type, value):
        sql = f"SELECT * FROM users WHERE {type} = {value}"
        with self.connection:
            user = self.cursor.execute(sql).fetchall()

        if (user == []):
            return None

        return self.__transform_user_data_to_dict(user[0])

    def __transform_user_data_to_dict(self, user_data):
        return {
            'id': user_data[0],
            'tg_id': user_data[1],
            'tg_name': user_data[2],
            'lol_puuid': user_data[3],
            'lol_name': user_data[4],
            'pull_ups': user_data[5],
            'coefficient': user_data[6],
        }

    # === Add ===
    def add(self, tg_id=None, tg_name=None, lol_puuid=None, lol_name=None, poull_ups=0, coefficient=1):
        if (tg_id != None):
            if (self.get_by_tg_id(tg_id) != []):
                logger.error('adding duplicate user')
                return
        elif (lol_puuid != None):
            if (self.get_by_lol_puuid(lol_puuid) != []):
                logger.error('adding duplicate user')
                return

        with self.connection:
            self.cursor.execute(
                "INSERT INTO users(tg_id, tg_name, lol_puuid, lol_name, poull_ups, coefficient) VALUES (?, ?, ?, ?, ?, ?)", (
                    tg_id, tg_name, lol_puuid, lol_name, poull_ups, coefficient)
            )

    # === Update ===
    def update_tg_id(self, user_id,  tg_id):
        self.__update('tg_id', user_id, tg_id)

    def update_tg_name(self, user_id, tg_name):
        self.__update('tg_name', user_id, tg_name)

    def update_lol_puuid(self, user_id, lol_puuid):
        self.__update('lol_puuid', user_id, lol_puuid)

    def update_lol_name(self, user_id, lol_name):
        self.__update('lol_name', user_id, lol_name)

    def update_pull_ups(self, user_id, pull_ups):
        self.__update('pull_ups', user_id, pull_ups)

    def update_coefficient(self, user_id, coefficient):
        self.__update('coefficient', user_id, coefficient)

    def __update(self, type, user_id, value):
        sql = f"UPDATE users SET {type} = {value} WHERE id = {user_id}"

        with self.connection:
            self.cursor.execute(sql)

    # === Delete ===
    def __delete(self, type, value):
        sql = f"DELETE FROM users WHERE {type} = {value}"

        with self.connection:
            self.cursor.execute(sql)

    def delete_by_tg_id(self, tg_id):
        self.__delete('tg_id', tg_id)

    def delete_by_lol_puuid(self, lol_puuid):
        self.__delete('lol_puuid', lol_puuid)


database = DataBase()
print(database.users.get_by_tg_id(906687130))

# @logger.catch
# def add_new_telegram_user(self, tg_id, tg_name) -> None:
#     if (self.get_all_by_tg_id(tg_id) == []):
#         with self.connection:
#             self.cursor.execute(
#                 "INSERT INTO users(tg_id, tg_name) VALUES (?, ?)", (tg_id, tg_name)
#             )

# @logger.catch
# def get_all_by_tg_id(self, tg_id):
#     with self.connection:
#         return self.cursor.execute(
#             "SELECT * FROM users WHERE tg_id = ?", (tg_id,)
#         ).fetchall()

# @logger.catch
# def get_all_by_user_id(self, user_id):
#     with self.connection:
#         return self.cursor.execute(
#             "SELECT * FROM users WHERE id = ?", (user_id,)
#         ).fetchall()

# @logger.catch
# def get_all_by_tg_id(self, tg_id):
#     with self.connection:
#         return self.cursor.execute(
#             "SELECT * FROM users WHERE tg_id = ?", (tg_id,)
#         ).fetchall()

# @logger.catch
# def update_user_lol_data(self, tg_id, lol_puuid, lol_name):
#     with self.connection:
#         return self.cursor.execute(
#             "UPDATE users SET lol_puuid = ?, lol_name = ? WHERE tg_id = ?", (
#                 lol_puuid, lol_name, tg_id)
#         )

# @logger.catch
# def get_user_id_by_puuid(self, puuid):
#     with self.connection:
#         return self.cursor.execute(
#             "SELECT id FROM users WHERE lol_puuid = ?", (puuid,)
#         ).fetchall()

# @logger.catch
# def get_last_user_match(self, user_id):
#     with self.connection:
#         return self.cursor.execute(
#             "SELECT match_id FROM matchs WHERE user_id = ?", (user_id,)
#         ).fetchall()

# @logger.catch
# def add_new_match(self, user_id, match_id, date, champion, kills, deaths, assists) -> None:
#     with self.connection:
#         self.cursor.execute(
#             "INSERT INTO matchs(user_id, match_id, date, champion, kills, deaths, assists) VALUES (?, ?, ?, ?, ?, ?, ?)", (
#                 user_id, match_id, date, champion, kills, deaths, assists)
#         )

# @logger.catch
# def add_new_record_in_history(self, user_id, data, value, current_coef, result_pull_ups, global_pull_ups) -> None:
#     with self.connection:
#         self.cursor.execute(
#             "INSERT INTO history(user_id, data, value, current_coef, result_pull_ups, global_pull_ups) VALUES (?, ?, ?, ?, ?, ?)", (
#                 user_id, data, value, current_coef, result_pull_ups, global_pull_ups)
#         )


@logger.catch
def update_user_pull_ups(self, user_id, pull_ups) -> None:
    with self.connection:
        self.cursor.execute(
            "UPDATE users SET pull_ups = ?", (pull_ups,)
        )

# @logger.catch
# def get_all_users(self):
#     with self.connection:
#         return self.cursor.execute(
#             "SELECT * FROM users"
#         ).fetchall()
