# v2utils
V2ray utilities

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