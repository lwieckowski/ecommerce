## Configuration
Configure sqitch on the machine that has sqitch installed and runs migrations
in `~/.sqitch/sqitch.conf`:
```
[core]
    engine = pg
[target "<target_name>"]
    uri = db:pg://<postgres_username>:<postgres_password>@<postgres_host>/<database_name>
[engine "pg"]
    target = <target_name>
[user]
    name = <username>
    email = <email>
```

## Commands
See sqitch help, but here are some most important ones:
```
sqitch deploy
sqitch verify
sqitch revert
```