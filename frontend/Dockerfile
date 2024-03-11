FROM node:18-alpine AS base

# Install dependencies only when needed
FROM base AS deps
# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
WORKDIR /usr/app
RUN npm install --global pm2
COPY ./package*.json ./
RUN npm i 
COPY ./ ./
COPY ../ip.txt ./ip.txt
COPY ./setup.sh ./setup.sh
RUN ./setup.sh
RUN npm run build
EXPOSE 3000

ENV PORT 3000
# set hostname to localhost
ENV HOSTNAME "0.0.0.0"

USER node

# server.js is created by next build from the standalone output
# https://nextjs.org/docs/pages/api-reference/next-config-js/output
CMD [ "pm2-runtime", "npm", "--", "start"]
