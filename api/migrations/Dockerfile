FROM sqitch/sqitch:latest

WORKDIR /db

COPY sqitch.conf /db/sqitch.conf
COPY sqitch.plan /db/sqitch.plan
COPY deploy /db/deploy
COPY deploy.sh /db/deploy.sh

ENTRYPOINT ["/db/deploy.sh"]
