import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
import random


XOXB_KEY = os.environ.get("XOXB_KEY")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
XAPP_KEY = os.environ.get("XAPP_KEY")


app = App(token=XOXB_KEY)
openai.api_key = OPENAI_KEY
chatbot = openai.Completion()

funny_answers = [
    "🤓 Dame un minutito que me pongo los lentes... ",
    "👀 Leyendo...",
    "✍️ Como no! Resumiendo... ",
    "👾 Dame un toquesito...",
    "🤖 Beep boop! A la orden!",
]


@app.event("app_mention")
def handle_mention(ack, body, say):
    channel_history = ""
    channel_id = body.get("event").get("channel")

    # Fetching up to the last 50 messages in the chat
    response = app.client.conversations_history(
        token=app._token, channel=channel_id, limit=50
    )

    if response.get("ok"):
        messages = response.get("messages")
        for message in messages:
            if "text" in message:
                channel_history += message.get("text")
        say(random.choice(funny_answers))

    try:
        response = chatbot.create(
            engine="text-davinci-003",
            prompt=f"Quiero que me hagas un resumen de esta conversación en un canal de Slack: {channel_history}",
            max_tokens=1000,
        )
        say(str(response.choices[0].text))
    except:
        say("🤔 Bz! Parece que OpenAI presenta problemas, intentá más tarde.")


if __name__ == "__main__":
    SocketModeHandler(
        app,
        XAPP_KEY,
    ).start()
