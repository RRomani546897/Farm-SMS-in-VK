import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType
import vk


token ="vk1.a.aUpq66QRRVPmLK_nypGIcNKJ-rxwzBQ8aSEahQkt-3ZF9yjZgFf7SmPfkB2IiwLv1h6nqZ3-Jd32BFUkTxinMuS1pMLzOKuyWSoRWe8gQ_veZYlYe0BwZM6lQkGVe04RsGuarpt0MmIXq278GH7dGZ0_czKNPP6pB7ML40pRWuoDqEcZBUny8r8SNOuP8iSg7AN6weSWjy-t_fzFqCw6ug"

vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
t = api.messages.getChat(chat_id="1321")
p = (t["users"])
q = str(p)
users=(q[1:-1])

titl="Blood_royz"



tam=1800
print(users)
