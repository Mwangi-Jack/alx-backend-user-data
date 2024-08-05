# 0x01 Basic Authentication

- This is a simple authentication method for HTTPs, where user ageng e.g. web browser provides a username and password when making a request to a server

- The credentials in the format username:password are encoded in Base64 and sent in the HTTP header in the format Autherization: Basic <encoded str>

- This authentication is not secure on its own because the credentials are easily decodable from Base64
- It should always be used over HTTPS to encrypt the connection and protect the credentials.
