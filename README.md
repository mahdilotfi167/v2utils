# v2utils
![Redeploy Server Status](https://github.com/mahdilotfi167/v2utils/actions/workflows/django.yml/badge.svg)  
A multi-user, graphical and distributed management application for V2ray with many usefull features.
## Notes
- Supported protocols: Vmess, Vless
- Support TCP, gRPC, WebSocket and H2 transport protocols
- User and inbound groups
- Traffic statistics and limitations (universal limitation or per-group limitation)
- Telegram bot for distribute configs between users
- Fake traffic generation to bypass Iranian's service providers on uplink and downlink traffic
- Automatic subscription generation

## Development
### Incoming Improvements
- [ ] Fake Traffic generator
- [ ] User status telegram bot
- [X] Add Trojan support
- [ ] Admin dashboard and Telegram bot log handlers
- [X] Custom admin page for user configurations (telegram token, binary path, traffic generation ratio, ...)
- [X] Store configurations in file and load a copy in memory for performance purposes
- [X] Add expiration time
- [ ] Show and Get traffic values in human readable format (B, MB, GB, ...)
- [ ] Quick setup with docker (Nginx, V2utils, DNS cache service, Distributed database, ...)
- [ ] Add logs and errors to admin panel (read by grpc and LogsService)
- [X] Partitioned django admin options
- [ ] Sniffing options (Enable sniffing for users to view traffic and used websites)
- [ ] Telegram bot can join channels and groups and automatically create user for all members
- [X] User groups (each inbound will be created in a group and a user can have many groups) for handling user restrictions
- [ ] Automatic self-signed certificate generation
- [ ] IP limitation options (using access logs)
- [ ] Import inbound from json file
- [X] Traffic limitations for Inbound level, Group level, and User level
- [X] Automatic Expiration and reset period
- [ ] Useful APIs
- [ ] Passphrase authentication
- [X] Automatic UDS deletions
- [X] Unit tests and github workflow
- [ ] Documentation and github pages
- [ ] Automatic link generation

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
