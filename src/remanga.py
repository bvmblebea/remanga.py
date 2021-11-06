# library made by DeLuvSushi & github.com/Zakovskiy
# P.S I didn't tested many functions!
import requests
import json


class Client:
    def __init__(self):
        self.api = "https://api.remanga.org"
        self.access_token = None
        self.user_Id = None
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
            }

    # login
    def auth(self, user: str, password: str):
        data = {"user": user, "password": password}
        request = requests.post(
            f"{self.api}/api/users/login/",
            json=data,
            headers=self.headers)
        json = request.json()
        self.access_token = json["content"]["access_token"]
        self.user_Id = json["content"]["id"]
        self.headers["authorization"] = f"bearer {self.access_token}"
        return json

    # send comment
    def send_comment(
            self,
            text: str,
            title_Id: int,
            is_pinned: bool = False,
            is_spoiler: bool = False):
        data = {
            "is_pinned": is_pinned,
            "is_spoiler": is_spoiler,
            "text": text,
            "title": title_Id}
        request = requests.post(
            f"{self.api}/api/activity/comments/?title_id={title_Id}",
            json=data,
            headers=self.headers)
        return request.json()

    # logging
    def logging(self, path_name: str = "/"):
        data = {
            "user": self.user_Id,
            "access_token": self.access_token,
            "msg": "CONSOLE",
            "location": {
                "pathname": path_name,
                "search": "",
                "hash": "",
                "key": ""},
            "deviceType": "desktop",
            "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
        request = requests.post(
            f"{self.api}/api/logging/",
            json=data,
            headers=self.headers)
        return request.json()

    # register account
    def register(self, email: str, password: str, username: str):
        data = {
            "confirm_password": password,
            "email": email,
            "password": password,
            "username": username}
        request = requests.post(
            f"{self.api}/api/users/signup/",
            json=data,
            headers=self.headers)
        return request.json()

    # get similar titles
    def similar_titles(self, title: str):
        request = requests.get(
            f"{self.api}/api/titles/{title}/similar/",
            headers=self.headers)
        return request.json()

    # search title
    def search_title(self, title: str, count: int = 5):
        request = requests.get(
            f"{self.api}/api/search/?query={title}&count={count}",
            headers=self.headers)
        return request.json()

    # search publishers
    def search_publishers(self, username: str, page: int = 1, count: int = 10):
        request = requests.get(
            f"{self.api}/api/search/?count={count}&field=publishers&page={page}&query={username}",
            headers=self.headers)
        return request.json()

    # edit profile
    def edit_profile(
            self,
            username: str = None,
            adult: bool = False,
            sex: int = 0,
            yaoi: int = 0):
        data = {"adult": adult, "sex": sex, "username": username, "yaoi": yaoi}
        request = requests.put(
            f"{self.api}/api/users/current/",
            json=data,
            headers=self.headers)
        return request.json()

    # get report reasons
    def get_report_reasons():
        request = requests.get(
            f"{self.api}/api/reports/?get=reasons&type=title",
            headers=self.headers)
        return request.json()

    # send report to title
    def send_report(
            self,
            message: str,
            reason: int,
            title_Id: int,
            type: str = "title"):
        data = {
            "message": message,
            "reason": reason,
            "target": title_Id,
            "type": type}
        request = requests.post(
            f"{self.api}/panel/api/reports/",
            json=data,
            headers=self.headers)
        return request.json()

    # like comment
    def like_comment(self, comment_Id: int, type: int = 0):
        data = {"comment": comment_Id, "type": type}
        request = requests.post(
            f"{self.api}/api/activity/votes/",
            json=data,
            headers=self.headers)
        return request.json()

    # get genres
    def get_genres(self):
        request = requests.get(
            f"{self.api}/api/forms/titles/?get=genres&get=categories&get=types&get=status&get=age_limit",
            headers=self.headers)
        return request.json()

    # get title information
    def get_title_info(self, title: str):
        request = requests.get(
            f"{self.api}/api/titles/{title}/",
            headers=self.headers)
        return request.json()

    # get title chapters
    def get_title_chapters(self, branch_Id: int):
        request = requests.get(
            f"{self.api}/api/titles/chapters/?branch_id={branch_Id}",
            headers=self.headers)
        return request.json()

    # get title comments
    def get_title_comments(self, title_Id: int, page: int = 1):
        data = {"title_id": title_Id, "page": page, "ordering": "-id"}
        request = requests.get(
            f"{self.api}/api/activity/comments/?title_id={title_Id}&page={page}&ordering=-id",
            json=data,
            headers=self.headers)
        return request.json()

    # get user information
    def get_user_info(self, user_Id: str):
        request = requests.get(
            f"{self.api}/api/users/{user_Id}",
            headers=self.headers)
        return request.json()

    # get notifications
    def get_notifications(self):
        request = requests.get(
            f"{self.api}/api/users/notifications/count/",
            headers=self.headers)
        return request.json()

    # get current account information
    def get_account_info(self):
        request = requests.get(
            f"{self.api}/api/users/current/",
            headers=self.headers)
        return request.json()

    # get daily top titles
    def get_daily_top_titles(self, count: int = 5):
        request = requests.get(
            f"{self.api}/api/titles/daily-top/?count={count}",
            headers=self.headers)
        return request.json()

    # get titles last chapters
    def get_titles_last_chapters(self, page: int = 1, count: int = 5):
        request = requests.get(
            f"{self.api}/api/titles/last-chapters/?page={page}&count={count}",
            headers=self.headers)
        return request.json()

    # add to bookmarks
    # bookmark types, 0 - reading, 1 - will read, 2 - readed, 3 - abandoned, 4
    # - postponed, 5 - not interesting
    def add_to_bookmarks(self, title_Id: int, type: int):
        data = {"mangaId": title_Id, "title": title_Id, "type": type}
        request = requests.post(
            f"{self.api}/api/users/bookmarks/",
            json=data,
            headers=self.headers)
        return request.json
