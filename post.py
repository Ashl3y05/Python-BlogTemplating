import requests

class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(url=self.blog_url)

    def get_all_blog_post(self):
        self.response.raise_for_status()
        return self.response.json()

    def get_specific_post(self, blog_num):
        self.response.raise_for_status()
        blog = self.response.json()
        num = int(blog_num) - 1
        return blog[num]
