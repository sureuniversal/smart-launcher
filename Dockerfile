# NOTE: If the BASE_URL env var is set to something like "http://localhost:9009"
# then the image should be started using the same port like:
#    docker run -t -p 9009:80 -d smartonfhir/smart-launcher:latest

FROM node:9

WORKDIR /app

ENV NODE_ENV      "production"
ENV LAUNCHER_PORT "443"
ENV BASE_URL      "https://smart-launcher.sureuniversal-dbg.net"
ENV PRIVATE "./cert/"


# Which FHIR servers to use
ENV FHIR_SERVER_R2 "https://r2.smarthealthit.org"
ENV FHIR_SERVER_R3 "https://r3.smarthealthit.org"
ENV FHIR_SERVER_R4 "https://fhir-server.sureuniversal-dbg.net/hapi-fhir-jpaserver/fhir"

# The names of the config files corresponding to the FHIR servers above
ENV PICKER_CONFIG_R2 "r2"
ENV PICKER_CONFIG_R3 "r3"
ENV PICKER_CONFIG_R4 "r4"

ENV PICKER_ORIGIN "https://patient-browser.s3.eu-central-1.amazonaws.com"

# Install and cache
COPY package.json      /tmp/package.json
COPY package-lock.json /tmp/package-lock.json
RUN cd /tmp && npm install --production
RUN mv /tmp/node_modules /app/node_modules

COPY . .

# You must use -p 9009:80 when running the image
EXPOSE 443

CMD ["node", "./src/index.js"]
