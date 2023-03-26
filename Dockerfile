FROM python:3.9-alpine

# Install v2ray
WORKDIR /root
COPY v2ray.sh .

RUN set -ex \
    && apk add --no-cache tzdata openssl ca-certificates \
    && mkdir -p /etc/v2ray /usr/local/share/v2ray /var/log/v2ray \
    && chmod +x /root/v2ray.sh \
    && /root/v2ray.sh

WORKDIR /app
COPY requirements.txt .

RUN set -ex \
    && apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .

ENV V2ENV=prod

ENTRYPOINT ["/bin/sh", "-c", "/app/run.sh"]