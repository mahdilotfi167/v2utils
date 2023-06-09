#!/bin/sh

ARCH="64"
TAG="v5.3.0"
TMP_DIR = /tmp/v2ray

# Creating temp working directory
mkdir -p $TMP_DIR
cd $TMP_DIR

# Download v2ray binary
V2RAY_FILE="v2ray-linux-${ARCH}.zip"
echo "Downloading binary file: ${V2RAY_FILE}"

wget -O ${PWD}/v2ray.zip https://github.com/v2fly/v2ray-core/releases/download/${TAG}/${V2RAY_FILE} > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "Error: Failed to download binary file: ${V2RAY_FILE}" && exit 1
fi
echo "Download binary file: ${V2RAY_FILE} completed"

# Prepare
echo "Prepare to use"
unzip -qq v2ray.zip && chmod +x v2ray
mv v2ray /usr/local/bin/
mv geosite.dat geoip.dat /usr/local/share/v2ray/

# Clean
rm -rf ${PWD}/*
echo "Done"