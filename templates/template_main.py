import time
import vk_api
import random
from funcs import work
 
token = "{{token}}"
 
vk = vk_api.VkApi(token=token)
 
vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            peer_id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            if body != "none" :
                answer = work(body)
                vk.method("messages.send", {"peer_id": peer_id, "message": answer, "random_id": random.randint(1, 2147483647)})
                        
    except Exception as E:
        time.sleep(1)
