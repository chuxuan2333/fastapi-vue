"""
多平台同步创建新用户账户
"""

import requests
import json
import base64
from bs4 import BeautifulSoup
import datetime
from hashlib import md5
from core.config import settings


class MultiCreate:
    def __init__(self, username, email, password, real_name):
        self.username = username
        self.email = email
        self.password = password
        self.real_name = real_name

    def zentao_create(self):
        """
        新建禅道用户
        :return:
        """
        # 获取sessionID
        session_json = requests.get(settings.ZENTAO_URL + "api-getsessionid.json").json()
        session_id = json.loads(session_json["data"])["sessionID"]
        # 生成登录Url
        login_url = settings.ZENTAO_URL + f"user-login.json?zentaosid={session_id}"
        # 用户登录获取session
        account = settings.ZENTAO_USER
        password = base64.b64decode(settings.ZENTAO_PASS)
        login_data = {"account": account, "password": password}
        session = requests.Session()
        r = session.post(login_url, data=login_data)
        if r.json()["status"] != "success":
            return False
        # 获取加密rand
        html = session.get(settings.ZENTAO_URL + "user-create-0.html").text
        soup = BeautifulSoup(html, 'html.parser')
        rand_md5 = soup.select_one('#verifyRand').attrs['value']
        # 创建用户
        self.zentao_create_user(account=self.username, password=self.password, real_name=self.real_name,
                                email=self.email,
                                session=session, rand_md5=rand_md5)

    def zentao_create_user(self, account, password, real_name, session, rand_md5, email, dept_id: int = 8):
        """
        创建用户
        :param rand_md5: md5加密的随机值
        :param session: request的session
        :param account: 账号
        :param password: 密码
        :param real_name: 真实姓名
        :param dept_id: 部门编号
        :param email: 邮箱
        :return:
        """
        user_password = md5(password.encode()).hexdigest() + rand_md5
        admin_pass = base64.b64decode(settings.ZENTAO_PASS).decode()
        admin_password = md5((md5(admin_pass.encode()).hexdigest() + rand_md5).encode()).hexdigest()
        data = {
            "dept": dept_id,
            "account": account,
            "password1": user_password,
            "password2": user_password,
            "realname": real_name,
            "join": str(datetime.date.today()),
            "role": "dev",
            "group": 2,
            "email": email,
            "commiter": "",
            "gender": "m",
            "verifyPassword": admin_password,
        }
        response = session.post(settings.ZENTAO_URL + "user-create-0.json", data=data)
        return response.status_code == 200

    def gitea_create(self):
        """
        创建gitea用户
        :return:
        """
        headers = {"Content-Type": "application/json", "accept": "application/json"}
        user_dict = {"email": self.email, "full_name": self.real_name, "login_name": self.username,
                     "must_change_password": True, "password": self.password, "send_notify": False, "source_id": 0,
                     "username": self.username}
        add_url = settings.GITEA_URL
        add_gitea_user = requests.post(add_url, headers=headers, params={"access_token": settings.GITEA_TOKEN},
                                       data=json.dumps(user_dict))
        return add_gitea_user.status_code == 201

    def multi_create(self, platforms):
        """
        :param platforms:平台名List
        :return: 创建成功列表
        """
        create_funcs = {"zentao": self.zentao_create, "gitea": self.gitea_create}
        for platform in platforms:
            create_funcs[platform]()
        return True
