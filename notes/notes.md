# Slack Bot - Arty
## Description

### Why Arty?
It sounds classy and demanding of respect.

## Program requirements
Runnable on: Windows? Mac?
Simple to use
Extensible without coding

## Slack Implementaion Details
This Application will use a SlackBot and the (Web API)[https://api.slack.com/web] to send messages to users. Since this bot doesnt need to read messages in realtime there is no need to set up a server to run the app on.

### Permissions
This app only needs to be able to send messages to anyone in the workspace, so the following permissions are needed:
1. users:read (View people in the workspace)
2. chat:write (Send messages as \@arty)

### Slack API Flow
1: A single call to `user.list` to aquire the messagable users and their id's (Link)[https://api.slack.com/methods/users.list/test]
2: Multiple calls to `conversation.open` to get the channel id of a DM conversation (Link)[https://api.slack.com/methods/conversations.open/test]
3: Multiple calls to `chat.postMessage` to write a message to someone (Link)[https://api.slack.com/methods/chat.postMessage/test]
