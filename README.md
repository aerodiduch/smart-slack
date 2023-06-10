
# smart-slack

An OpenAI integration to stay on track with your team's Slack conversations!

Have you suddenly opened a channel and saw that there were more messages that you could ever imagine? This app is for you, my friend!

With smart-slack you'll be able to get a nice summary of the last 50 messages on that channel, so you can join the conversation!

# Prerequisites
In order to integrate this app to your Slack workspace, you'll need to:


- Have an OpenAI `api key` (paid service)
- Have an Slack application in `socket mode`, with its `XOXB` and `XAPP` key.
- `Docker` and `docker compose`.

## Setting up correct permissions
SInce this app needs to read the channel history, you need to make sure that your app has this OAuth scopes defined:

- `app_mentions:read`
- `channels:history`
- `channels:read`
- `chat:write`

# Preparing for deploy
If you are going to deploy smart-slack as a docker container, you need to populate enviromental variables inside docker-compose.yaml

> Do not put the keys between double or single quotes. You need to pass them raw like in the example below.


```yaml
environment:
      - XOXB_KEY=xoxb-1234
      - OPENAI_KEY=sk-1234
      - XAPP_KEY=xapp-1234
```
Then, you can simply build an deploy!

```sh
docker compose build --no-cache && docker compose up -d
```

# Usage
Simply mention the bot on the channel you want. Boom!