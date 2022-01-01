from loguru import logger
import sqlite3
from datetime import datetime


class DataBase:
    @logger.catch
    def __init__(self):
        """Подключение и курсор"""
        self.connection = sqlite3.connect("utils/db_api/db.db")
        self.cursor = self.connection.cursor()

    @property
    def users(self):
        return Users(self.connection, self.cursor)

    @property
    def history(self):
        return History(self.connection, self.cursor)

    @property
    def matchs(self):
        return Matchs(self.connection, self.cursor)


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
            if (self.get_by_tg_id(tg_id) != None):
                logger.error('adding duplicate user')
                return
        elif (lol_puuid != None):
            if (self.get_by_lol_puuid(lol_puuid) != None):
                logger.error('adding duplicate user')
                return

        with self.connection:
            self.cursor.execute(
                "INSERT INTO users(tg_id, tg_name, lol_puuid, lol_name, pull_ups, coefficient) VALUES (?, ?, ?, ?, ?, ?)", (
                    tg_id, tg_name, lol_puuid, lol_name, poull_ups, coefficient)
            )

        return 0

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


class History():
    @logger.catch
    def __init__(self, connection, cursor):
        """Подключение и курсор"""
        self.connection = connection
        self.cursor = cursor

    # === GET ===
    def get_by_user_id(self, user_id):
        return self.__get('user_id', user_id)

    def __get(self, type, value):
        sql = f"SELECT * FROM history WHERE {type} = {value}"

        with self.connection:
            data = self.cursor.execute(sql).fetchall()

        if (data == []):
            return None

        return self.__transform_data_items_to_dicts(data)

    def __transform_data_items_to_dicts(self, data):
        result = []
        for item in data:
            result.append({
                "id": item[0],
                "user_id": item[1],
                "date": datetime.strptime(item[2], "%d/%m/%Y %H:%M:%S"),
                "value": item[3],
                "current_coef": item[4],
                "result_pull_ups": item[5],
                "global_pull_ups": item[6]
            })
        return result

    # === ADD ===
    def add(self, user_id, date, value, current_coef, result_pull_ups, global_pull_ups):

        if (type(date) != datetime):
            date = datetime.strptime(date, "%d/%m/%Y %H:%M:%S")

        sql = f"INSERT INTO history VALUES ({user_id}, {date}, {value}, {current_coef}, {result_pull_ups}, {global_pull_ups})"

        with self.connection:
            self.cursor.execute(sql)


class Matchs():
    @logger.catch
    def __init__(self, connection, cursor):
        """Подключение и курсор"""
        self.connection = connection
        self.cursor = cursor

    # === GET ===
    def get_by_user_id(self, user_id):
        return self.__get('user_id', user_id)

    def get_by_match_id(self, match_id):
        return self.__get('match_id', match_id)

    def __get(self, type, value):
        sql = f"SELECT * FROM matchs WHERE {type} = {value}"

        with self.connection:
            data = self.cursor.execute(sql).fetchall()

        if (data == []):
            return None

        return self.__transform_data_items_to_dicts(data)

    def __transform_data_items_to_dicts(self, data):
        result = []
        for item in data:
            result.append({
                "id": item[0],
                "user_id": item[1],
                "match_id": item[2],
                "date": datetime.strptime(item[3], "%d/%m/%Y %H:%M:%S"),
                "champion": item[4],
                "kills": item[5],
                "deaths": item[6],
                "assists": item[7]
            })
        return result

    # === ADD ===
    def add(self, user_id, match_id, date, champion, kills, deaths, assists):

        if (type(date) != datetime):
            date = datetime.strptime(date, "%d/%m/%Y %H:%M:%S")

        sql = f"INSERT INTO matchs VALUES ({user_id}, {match_id}, {date}, {champion}, {kills}, {deaths}, {assists})"

        with self.connection:
            self.cursor.execute(sql)
