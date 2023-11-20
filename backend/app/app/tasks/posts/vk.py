import vk_api

vk_session = vk_api.VkApi(app_id='51791581', client_secret='EP9kmPjEKzlXuVXzd6bJ', scope=['photos', 'wall'], api_version=5.131)

auth_url = vk_session.server_auth()
print(auth_url)





import vk_api
from vk_api import VkUpload

from app.core.config import settings

vk_session = vk_api.VkApi(token=settings.VK_ACCESS_TOKEN)
vk = vk_session.get_api()

# longpool = VkLongPoll(vk_session)
#
# def send_some_msg(id, some_text):
#     vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})
#
# for event in longpool.listen():
#     if event.type == VkEventType.MESSAGE_NEW:
#         if event.to_me:
#             msg = event.text.lower()
#             id = event.user_id
#             if msg == "hi":
#                 send_some_msg(id, "Hi friend!")

post_text = "Ваш текст поста здесь."
vk.wall.post(owner_id='-' + str(settings.VK_GROUP_ID), from_group=1, message=post_text)