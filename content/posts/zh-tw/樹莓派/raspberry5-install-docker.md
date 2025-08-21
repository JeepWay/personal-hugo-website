+++
title = '在 Raspberry Pi 5 安裝 Docker'
date = '2025-08-08T09:18:16+08:00'
lastmod = '2025-08-22T07:13:00+08:00'
draft = false
categories = ['樹莓派']
tags = ['樹莓派', 'Docker']
+++

# 在 Raspberry Pi 安裝 Docker

## 安裝步驟
1. 安裝 Docker
    ```bash
    curl -sSL https://get.docker.com | sh
    ```
2. 為當前用戶 pi 新增執行 Docker 指令的權限，新增完後需要重新開機才能生效。
    ```bash
    sudo usermod -aG docker pi
    ```
    * 若沒有新增，則每次都需要加上 `sudo`，蠻麻煩的。
    * 如果有自訂你的用戶名稱，則把 pi 改成你的自訂的。
    * 當前用戶和群組可以用以下相關命令查詢。
        ```bash
        # 直接顯示當前終端機的用戶名稱
        $ whoami
        
        # 顯示當前用戶的詳細資訊，包括用戶 ID（UID）、群組 ID（GID）以及用戶所屬的所有群組。
        $ id
        
        # 顯示當前用戶的環境變數 $USER
        $ echo $USER
        
        # 列出所有當前登入系統的用戶，包括終端機或遠端會話的用戶名稱
        $ who
        
        # 列出當前用戶所屬的所有群組
        $ groups
        
        # 查看所有群組的配置檔案
        $ cat /etc/group
        ```
3. 測試是否成功安裝 Docker
    ```bash
    docker run hello-world
    ```
    * 有出現以下內容就是安裝成功了
        ```bash
        $ docker run hello-world
        ....
        Hello from Docker!
        This message shows that your installation appears to be working correctly.
        ....
        ```
    * 若沒有重新開機過，則要改成執行 `sudo docker run hello-world`。
4. 查看 Docker 的 Client 和 Server 是否皆啟動
    ```badsh
    docker version
    ```
    * 有出現以下就是成功
        ```bash
        Client: Docker Engine - Community
         Version:           28.3.3
         API version:       1.51
         Go version:        go1.24.5
         Git commit:        980b856
         Built:             Fri Jul 25 11:35:32 2025
         OS/Arch:           linux/arm64
         Context:           default

        Server: Docker Engine - Community
         Engine:
          Version:          28.3.3
          API version:      1.51 (minimum version 1.24)
          Go version:       go1.24.5
          Git commit:       bea959c
          Built:            Fri Jul 25 11:35:32 2025
          OS/Arch:          linux/arm64
          Experimental:     false
         containerd:
          Version:          1.7.27
          GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
         runc:
          Version:          1.2.5
          GitCommit:        v1.2.5-0-g59923ef
         docker-init:
          Version:          0.19.0
          GitCommit:        de40ad0
        ```
6. 查看 Docker 的使用方式
    ```bash
    docker --help
    ```
    ```bash
    docker compose --help
    ```

## 新增命名方式
把舊版的 docker compose 用法 `docker-compose` 加到環境變數的 alias，輸入以下命來來把述加到換境變數檔案 `~/.bashrc` 裡面，然後更新 `~/.bashrc`。

```bash
echo "alias docker-compose='docker compose'" >> ~/.bashrc

source ~/.bashrc
```