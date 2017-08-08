FROM node:8.2.1-alpine

RUN apk add -q --no-cache git
RUN npm install -gq quasar-cli

ADD package.json /tmp/package.json
RUN cd /tmp && npm install -q && mkdir -p /frontend && cp -a /tmp/node_modules /frontend

WORKDIR /frontend
ADD . /frontend
# RUN quasar build

EXPOSE 8080
CMD [ "quasar", "dev" ]
