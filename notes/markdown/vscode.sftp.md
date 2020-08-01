## Configuration


```json
{
    "host": "10.253.52.106",
    "port": 22,
    "username": "seen-devel",
    "password": "seen-devel",
    "protocol": "sftp",
    "privateKeyPath": null,
    "passphrase": null,
    "passive": false,
    "remotePath": "/srv/repository/jenkins/workspace/tools-status-tenant",
    "uploadOnSave": false,
    "syncMode": "update",
    "watcher": {
        "files": false,
        "autoUpload": false,
        "autoDelete": true
    },
   "ignore": [
        "**/.vscode",
        "**/.git",
        "**/.DS_Store",
        "**/.sftpConfig.json",
        "**/*.pyc",
        "**/*.log",
        "**/logs",
        "**/html/*.json",
        "**/html/*.html"
    ]
}

```
