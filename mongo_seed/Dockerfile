
FROM mongo:4.4
ARG DATABASE_URI
ARG USERNAME
ARG PASSWORD

ENV DATABASE_URI ${DATABASE_URI}
ENV USERNAME ${USERNAME}
ENV PASSWORD ${PASSWORD}

COPY accounts-api-large.json /accounts-api-large.json

COPY transactions-api-large.json /transactions-api-large.json

CMD mongoimport --username ${USERNAME} --password ${PASSWORD} --uri ${DATABASE_URI} --collection accounts --drop --file /accounts-api-large.json && \
    mongoimport --username ${USERNAME} --password ${PASSWORD} --uri ${DATABASE_URI} --collection transactions --drop --file /transactions-api-large.json

