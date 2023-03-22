# v2utils
V2ray utilities

### Incoming Improvements
- [ ] Fake Traffic generator
- [ ] User status telegram bot
- [ ] Custom admin page for user configurations (telegram token, binary path, traffic generation ratio, ...)
- [ ] Store configurations in file and load a copy in memory for performance purposes.
- [ ] Show and Get traffic values in human readable format (B, MB, GB, ...)
- [ ] Quick setup with docker (Nginx, V2utils, DNS cache service, Distributed database, ...)

### How to?
#### Update protocol buffer
- Clone the latest version of v2ray-core
- Run the following command in the root directory of v2ray-core
```
python -m grpc_tools.protoc \
   -I=${V2RAY_CORE_ROOT} \
   --python_out=${V2UTILS_ROOT}/v2client/v${V2RAY_VERSION}/proto \
   --pyi_out=${V2UTILS_ROOT}/v2client/v${V2RAY_VERSION}/proto \
   --grpc_python_out=${V2UTILS_ROOT}/v2client/v${V2RAY_VERSION}/proto \
   **/*.proto
```
