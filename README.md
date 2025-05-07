# brentbot
it's brentbot, the awesome link utility bot.

env vars:

-BL contains channel IDs that want to FULLY blacklist links
-WL contains channel IDs and a comma regex sting that want to explicitly remove a link type using regex.

# will you continue doing more
maybe idk

# how run
look in packages, there's a docker package. You should be able to run it once you create two files required by docker
compose, and an env file.
Simply:
```
docker pull ghcr.io/kodakoba/brentbot:main
```

# planned features
switching over to db for channel list instead of files
1 click env deploy
