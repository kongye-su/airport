import re
import random
import requests


class Airport:
    def __init__(self):
        self.sess = requests.Session()
        self.email = self.random_email()
        self.password = self.random_password()
        self.name = self.random_name()

    def start(self):
        self.speed_cat()
        # self.ssru8()
        # self.fastlink()

    def get_json(self, url, params=None):
        return self.sess.get(url, params=params).json()

    def post_json(self, url, data=None):
        return self.sess.post(url, data=data).json()

    def get_html(self, url, params=None):
        return self.sess.get(url, params=params)

    def random_email(self):
        length = random.randint(5, 20)
        email_prefixs = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        email_prefix = "".join([random.choice(email_prefixs) for _ in range(length)])
        email_suffixs = ["@163.com", "@qq.com", "@gmail.com", "@outlook.com",
                         "@yahoo.com", "@hotmail.com", "@126.com",
                         "@foxmail.com"]
        email_suffix = random.choice(email_suffixs)
        return email_prefix + email_suffix

    def random_password(self):
        length = random.randint(8, 15)
        passwords = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ.+-*/~`@!#$%^&()_=':;<>,?/"
        password = "".join([random.choice(passwords) for _ in range(length)])
        return password

    def random_name(self):
        length = random.randint(5, 15)
        names = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        name = "".join([random.choice(names) for _ in range(length)])
        return name

    def speed_cat(self):
        # 3天5G流量
        register_url = "https://aff03.speedcat-aff02.com/auth/register"
        data = {"email": self.email,
                "name": self.name,
                "passwd": self.password,
                "repasswd": self.password,
                "code": "speedcat"}
        res_json = self.post_json(register_url, data=data)
        if res_json['ret'] == 1:
            login_url = "https://aff03.speedcat-aff02.com/auth/login"
            data = {"email": self.email,
                    "passwd": self.password,
                    "code": "",
                    "remember_me": "on"}
            res_json = self.post_json(login_url, data)
            if res_json["ret"] == 1:
                buy_url = "https://aff03.speedcat-aff02.com/user/buy"
                data = {
                    "coupon": "free",
                    "shop": "16",
                    "autorenew": "0",
                    "disableothers": "1"
                }
                res_json = self.post_json(buy_url, data)
                user_url = "https://aff03.speedcat-aff02.com/user"
                res = self.get_html(user_url)
                result = re.search(r"apiv2/([a-z1-9]+)\?", res.text)
                key = result[1]
                print("-------------speedcat-------------")
                print("ShadowSocket订阅： https://apiv2.pptiok2020.com/apiv2/%s?sub=2&extend=1" % key)
                print("Clash订阅： https://apiv2.pptiok2020.com/apiv2/%s?clash=1&extend=11" % key)

    def ssru8(self):
        # 1天1G+流量
        register_url = "https://ssru8.icu/auth/register"
        data = {"email": self.email,
                "name": self.name,
                "passwd": self.password,
                "repasswd": self.password,
                "wechat": "",
                "imtype": "",
                "code": "0"}
        res_json = self.post_json(register_url, data=data)
        if res_json['ret'] == 1:
            res_json = self.post_json("https://ssru8.icu/user/checkin")
            user_url = "https://ssru8.icu/user"
            res = self.get_html(user_url)
            result = re.search(r"link/([a-zA-Z1-9]+)\?", res.text)
            key = result[1]
            print("-------------ssru8-------------")
            print("ShadowSocket订阅：https://lting.cyou/link/%s?sub=3" % key)
            print("Clash订阅： https://lting.cyou/link/%s?clash=1" % key)

    def fastlink(self):
        # 3天5G流量
        register_url = "https://v1.fastlink-aff02.com/auth/register"
        data = {"email": self.email,
                "name": self.name,
                "passwd": self.password,
                "repasswd": self.password,
                "code": "0"}
        res_json = self.post_json(register_url, data=data)
        if res_json['ret'] == 1:
            login_url = "https://v1.fastlink-aff02.com/auth/login"
            data = {"email": self.email,
                    "passwd": self.password,
                    "code": ""}
            res_json = self.post_json(login_url, data)
            buy_url = "https://v1.fastlink-aff02.com/user/buy"
            data = {
                "coupon": "599_f3cz8bzm",
                "shop": "3",
                "autorenew": "0",
                "disableothers": "1"
            }
            res_json = self.post_json(buy_url, data)
            user_url = "https://v1.fastlink-aff02.com/user"
            res = self.get_html(user_url)
            result = re.search(r"api_version2/([a-z1-9]+)\?", res.text)
            key = result[1]
            print("-------------FASTLINK-------------")
            print("ShadowSocket订阅： https://apiv2.lipulai.com/api_version2/%s?sub=3&extend=1" % key)
            print("Clash订阅： https://apiv2.lipulai.com/api_version2/%s?clash=1&extend=1" % key)


if __name__ == "__main__":
    a = Airport()
    a.start()
