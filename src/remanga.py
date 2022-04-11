import requests


class Client:
    def __init__(self, access_token: str = None):
        self.api = "https://api.remanga.org"
        self.user_id = None
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
        if access_token:
            self.signin_by_access_token(access_token)

    # login
    def signin_by_access_token(self, access_token: str):
        self.access_token = access_token
        self.headers["authorization"] = f"bearer {self.access_token}"
        self.user_id = self.get_account_info()["content"]["id"]
        return self.access_token

    # send comment
    def send_comment(
            self,
            text: str,
            title_id: int,
            is_pinned: bool = False,
            is_spoiler: bool = False):
        data = {
            "is_pinned": is_pinned,
            "is_spoiler": is_spoiler,
            "text": text,
            "title": title_id}
        return requests.post(
            f"{self.api}/api/activity/comments/?title_id={title_id}",
            json=data,
            headers=self.headers).json()

    # logging
    def logging(self, path_name: str = "/"):
        data = {
            "user": self.user_id,
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
        return requests.post(
            f"{self.api}/api/logging/",
            json=data,
            headers=self.headers).json()

    # get similar titles
    def similar_titles(self, title: str):
        return requests.get(
            f"{self.api}/api/titles/{title}/similar/",
            headers=self.headers).json()

    # search title
    def search_title(self, title: str, count: int = 5):
        return requests.get(
            f"{self.api}/api/search/?query={title}&count={count}",
            headers=self.headers).json()

    # search publishers
    def search_publishers(self, username: str, page: int = 1, count: int = 10):
        return requests.get(
            f"{self.api}/api/search/?count={count}&field=publishers&page={page}&query={username}",
            headers=self.headers).json()

    # edit profile
    def edit_profile(
            self,
            username: str = None,
            adult: bool = False,
            sex: int = 0,
            yaoi: int = 0):
        data = {"adult": adult, "sex": sex, "username": username, "yaoi": yaoi}
        return requests.put(
            f"{self.api}/api/users/current/",
            json=data,
            headers=self.headers).json()

    # get report reasons
    def get_report_reasons():
        return requests.get(
            f"{self.api}/api/reports/?get=reasons&type=title",
            headers=self.headers).json()

    # send report to title
    def send_report(
            self,
            message: str,
            reason: int,
            title_id: int,
            type: str = "title"):
        data = {
            "message": message,
            "reason": reason,
            "target": title_id,
            "type": type}
        return requests.post(
            f"{self.api}/panel/api/reports/",
            json=data,
            headers=self.headers).json()

    # like comment
    def like_comment(self, comment_id: int, type: int = 0):
        data = {"comment": comment_id, "type": type}
        return requests.post(
            f"{self.api}/api/activity/votes/",
            json=data,
            headers=self.headers).json()

    # get genres
    def get_genres(self):
        return requests.get(
            f"{self.api}/api/forms/titles/?get=genres",
            headers=self.headers).json()

    # get title information
    def get_title_info(self, title: str):
        return requests.get(
            f"{self.api}/api/titles/{title}/",
            headers=self.headers).json()

    # get title chapters
    def get_title_chapters(self, branch_id: int):
        return requests.get(
            f"{self.api}/api/titles/chapters/?branch_id={branch_id}",
            headers=self.headers).json()

    # get title comments
    def get_title_comments(self, title_id: int, page: int = 1):
        data = {"title_id": title_id, "page": page, "ordering": "-id"}
        return requests.get(
            f"{self.api}/api/activity/comments/?title_id={title_id}&page={page}&ordering=-id",
            json=data,
            headers=self.headers).json()

    # get user information
    def get_user_info(self, user_id: str):
        return requests.get(
            f"{self.api}/api/users/{user_id}",
            headers=self.headers).json()

    # get notifications
    def get_notifications(self, count: int = 30, page: int = 1):
        return requests.get(
            f"{self.api}/api/users/notifications/?count={count}&page={page}&status=0&type=0",
            headers=self.headers).json()

    def get_notifications_count(self):
        return requests.get(
            f"{self.api}/api/users/notifications/count/",
            headers=self.headers).json()

    # get current account information
    def get_account_info(self):
        return requests.get(
            f"{self.api}/api/users/current/",
            headers=self.headers).json()

    # get daily top titles
    def get_daily_top_titles(self, count: int = 5):
        return requests.get(
            f"{self.api}/api/titles/daily-top/?count={count}",
            headers=self.headers).json()

    # get titles last chapters
    def get_titles_last_chapters(self, page: int = 1, count: int = 5):
        return requests.get(
            f"{self.api}/api/titles/last-chapters/?page={page}&count={count}",
            headers=self.headers).json()

    # add to bookmarks
    # bookmark types, 0 - reading, 1 - will read, 2 - readed, 3 - abandoned, 4
    # - postponed, 5 - not interesting
    def add_to_bookmarks(self, title_id: int, type: int):
        data = {"mangaId": title_id, "title": title_id, "type": type}
        return requests.post(
            f"{self.api}/api/users/bookmarks/",
            json=data,
            headers=self.headers).json()

    def change_password(self, old_password: str, new_password: str):
        data = {
            "old_password": old_password,
            "confirm_password": new_password,
            "password": new_password
        }
        return requests.put(
            f"{self.api}/api/users/current/",
            json=data,
            headers=self.headers).json()

    def bill_promo_code(self, promo_code: str):
        data = {
            "promo_code": promo_code
        }
        return requests.post(
            f"{self.api}/api/billing/promo-codes/",
            json=data,
            headers=self.headers).json()

    def create_publishers(self, name: str, vk_url: str):
        data = {"name": name, "vk": vk_url}
        return requests.post(
            f"{self.api}/api/publishers/",
            json=data,
            headers=self.headers).json()

    def rate_title(self, title_id: int, rating: int = 10):
        data = {"rating": rating, "title": title_id}
        return requests.post(
            f"{self.api}/api/activity/ratings/",
            json=data,
            headers=self.headers).json()

    def like_chapter(self, chapter_id: int, type: int = 0):
        data = {"chapter": chapter_id, "type": type}
        return requests.post(
            f"{self.api}/api/activity/votes/",
            json=data,
            headers=self.headers).json()

    def get_categories(self):
        return requests.get(
            f"{self.api}/api/forms/titles/?get=categories",
            headers=self.headers).json()

    def get_age_limits(self):
        return requests.get(
            f"{self.api}/api/forms/titles/?get=age_limit",
            headers=self.headers).json()

    def get_types(self):
        return requests.get(
            f"{self.api}/api/forms/titles/?get=types",
            headers=self.headers).json()

    def get_statuses(self):
        return requests.get(
            f"{self.api}/api/forms/titles/?get=status",
            headers=self.headers).json()

    def get_user_bookmarks(self, type: int, user_id: int, page: int = 1):
        return requests.get(
            f"{self.api}/api/users/{user_id}/bookmarks/?ordering=-chapter_date&page={page}&type={type}",
            headers=self.headers).json()

    def get_user_history(self, user_id: int, page: int = 1):
        return requests.get(
            f"{self.api}/api/users/{user_id}/history/?page={page}",
            headers=self.headers).json()

    def get_social_notifications(self, count: int = 30, page: int = 1):
        return requests.get(
            f"{self.api}/api/users/notifications/?count={count}&page={page}&status=0&type=1",
            headers=self.headers).json()

    def get_important_notifications(self, count: int = 30, page: int = 1):
        return requests.get(
            f"{self.api}/api/users/notifications/?count={count}&page={page}&status=0&type=2",
            headers=self.headers).json()
