# v2utils
V2ray utilities

### Incoming Improvements
- [ ] Fake Traffic generator
- [ ] User status telegram bot
- [X] Custom admin page for user configurations (telegram token, binary path, traffic generation ratio, ...)
- [X] Store configurations in file and load a copy in memory for performance purposes.
- [ ] Show and Get traffic values in human readable format (B, MB, GB, ...)
- [ ] Quick setup with docker (Nginx, V2utils, DNS cache service, Distributed database, ...)
- [ ] Add logs and errors to admin panel
- [ ] Partitioned django admin options
- [ ] Two types of fallbacks (A fallbask can point to an inbound and a UDS will be created for share same address)

### How to?
#### Run project
- Add package `v2client/v5/proto` to `PYTHONPATH`
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
#### Add extra setting
- Run `python manage.py makemigrations --empty appname`  
- Use `utils.migrations.AddExtraSetting in the generated migration`.
