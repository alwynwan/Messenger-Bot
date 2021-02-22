# -*- coding: UTF-8 -*-
import pickle, os, string, random, srtgen
from moviepy.editor import *
from fbchat import Client, log
from fbchat.models import *

prefix = ["o!", "O!"]
owo_uwu = ['owo', 'uwu']

# this is super gay but it works
remap_dict = {
    "?": "\U00002753",
    "!": "\U00002757",
    "+": "\U00002795",
    "-": "\U00002796",
    "#": "#️⃣",
    "*":"*️⃣",
    "0": "0️",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
}

help_items = {
    "em <message>": "Converts your message into emoji",
    "sb": "Converts your message into retard Spongebob text",
    "help": "Displays this help message",
    "jojoke": "Posts a random JoJoke (WIP)",
    "wjj": "Posts a random 'Watch JoJo' meme (WIP)",
    "bajj": "Posts a random 'Before/After JoJO' meme (WIP)",
    "ynl <message>": "Generates a \"Your next line is...\" GIF with your message"
}

processing_messages = ["👌 Comin' right up", "⏲️ Working on it...", "✔️ Yes sir!", "⏲️ Hol' your horses, I'm doing my best!"]

def spongebob(msg):
    result = msg.lower()
    flipflop = True
    for x in range(0,len(msg)):
        if ord(msg[x]) in range(ord('a'), ord('z')):
            if flipflop:
                result = result.replace(msg[x],msg[x].upper(), 1)
            flipflop = not flipflop
    return result

def make_emoji(msg):
    result = (" ".join(map(lambda y : str(y),msg))).lower()

    for x in range(0,len(msg)):
        if ord(msg[x]) in range(ord('a'), ord('z')):
            # cool unicode range magic
            result = result.replace(msg[x], chr(ord(msg[x]) + 0x1F185),1)
        elif msg[x] in remap_dict:
            result = result.replace(msg[x], remap_dict[msg[x]],1)

    return result

def get_jojoke(_type):
    path = ""
    if _type == "jojoke": path = r"C:\Users\User\Google Drive\Jojokes"
    elif _type == "wjj": path = r"C:\Users\User\Google Drive\Jojokes\watch jojo"
    elif _type == "bajj": path = r"C:\Users\User\Google Drive\Jojokes\before after jojo"
    return os.path.join(path,random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]))


class OwOBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if message_object.text == None:
                super(OwOBot, self).onMessage(
                author_id=author_id,
                message_object=message_object,
                thread_id=thread_id,
                thread_type=thread_type,
                **kwargs
            )
        else:
            if author_id == 100009299193226:
                self.reactToMessage(message_object.uid, MessageReaction.YES)
            if message_object.text.lower() in owo_uwu:
                self.reactToMessage(message_object.uid, MessageReaction.LOVE)
            if message_object.text[0:2] in prefix:
                msg_content = message_object.text[2::]
                self.markAsDelivered(thread_id, message_object.uid)
                self.markAsRead(thread_id)

                log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

                if author_id != self.uid:
                    args = msg_content.split()

                    cmd = args[0].lower()

                    if cmd == "help":
                        self.send(Message(text="Current prefixes: %s\r\nAvailable commands:\r\n\t%s" % (", ".join(prefix), "\r\n\t".join(map(lambda x : ": ".join(map(lambda y : str(y), x)), help_items.items())))), thread_id=thread_id, thread_type=thread_type)
                    elif cmd == "em":
                        self.send(Message(text=make_emoji(" ".join(args[1::]))), thread_id=thread_id, thread_type=thread_type)
                    elif cmd == "sb":
                        self.send(Message(text=spongebob(" ".join(args[1::]))), thread_id=thread_id, thread_type=thread_type)
                    elif cmd == "ynl":
                        self.send(Message(text=random.choice(processing_messages)),thread_id=thread_id, thread_type=thread_type)
                        srtgen.composite_gif(" ".join(args[1::]))
                        self.sendLocalImage(r"D:\Final Renders\result.gif",thread_id=thread_id, thread_type=thread_type)
                        os.remove(r"D:\Final Renders\result.gif")
                    elif cmd == "jojoke":
                        self.send(Message(text=random.choice(processing_messages)),thread_id=thread_id, thread_type=thread_type)
                        joke = get_jojoke("jojoke")
                        self.sendLocalImage(joke,thread_id=thread_id, thread_type=thread_type)
                    elif cmd == "wjj":
                        self.send(Message(text=random.choice(processing_messages)),thread_id=thread_id, thread_type=thread_type)
                        joke = get_jojoke("wjj")
                        self.sendLocalImage(joke,thread_id=thread_id, thread_type=thread_type)
                    elif cmd == "bajj":
                        self.send(Message(text=random.choice(processing_messages)),thread_id=thread_id, thread_type=thread_type)
                        joke = get_jojoke("bajj")
                        self.sendLocalImage(joke,thread_id=thread_id, thread_type=thread_type)
                    else:
                        self.reactToMessage(message_object.uid, MessageReaction.ANGRY)
                        self.send(Message(text="❌ Invalid command"),thread_id=thread_id, thread_type=thread_type)
            else:
                super(OwOBot, self).onMessage(
                    author_id=author_id,
                    message_object=message_object,
                    thread_id=thread_id,
                    thread_type=thread_type,
                    **kwargs
                )

client = OwOBot(username,password,logging_level=30)

if os.path.isfile('cookies.p'):
    cookies = pickle.load(open('cookies.p','rb'))
    client = OwOBot('bowot.chan@hotmail.com', 'jJIh7SYBAh6wna',session_cookies=cookies,logging_level=30)

session = client.getSession()
pickle.dump(session,open('cookies.p','wb'))

print("Own id: {}".format(client.uid))
client.listen()