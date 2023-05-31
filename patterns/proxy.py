from typing import Tuple

class User:
    id = 1
    def __init__(self, name, group_id) -> None:
        self.name = name
        self.group_id = group_id
        self.id = User.id
        User.id += 1


class Page:
    allowed_group_ids: Tuple[int] 
    def __init__(self, content: str):
        self.content = content

class MainPage(Page):
    allowed_group_ids = (1, 2, 3)

class AdminPage(Page):
    allowed_group_ids = (1,)

class PermitProxy:
    @staticmethod
    def get_content(page: Page, user: User):
        if user.group_id in page.allowed_group_ids:
            return page.content
        return 'You do not have permission to view this page'
    
main_page = MainPage('Main page content')
admin_page = AdminPage('Administration of Lipetsk')
admin = User('admin', 1)
maxim = User('M@X!M', 3)

print(PermitProxy.get_content(main_page, maxim))    # Main page content
print(PermitProxy.get_content(admin_page, maxim))   # You do not have permission to view this page
print(PermitProxy.get_content(admin_page, admin))   # Administration of Lipetsk
