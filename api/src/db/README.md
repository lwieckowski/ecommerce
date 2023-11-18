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
[deploy]
	verify = true
[rebase]
	verify = true
```

## Commands
See sqitch help, but here are some most important ones:
```
sqitch add <change_name> --requires <dependency_name> -n 'Change message'
sqitch deploy
sqitch verify
sqitch revert
```