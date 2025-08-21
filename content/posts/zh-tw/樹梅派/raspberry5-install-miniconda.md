+++
title = '在 Raspberry Pi 安裝 miniconda'
date = '2025-08-11T09:35:44+08:00'
lastmod = '2025-08-22T12:45:00+08:00'
draft = true
categories = ['樹梅派']
tags = ['樹梅派', 'miniconda']
+++

# 在 Raspberry Pi 安裝 miniconda

## 前言
為了讓每個 python 專案有自己的專屬環境來管理套件，而不去影響其他專案，最好是安裝環境管理系統，像是 Anaconda 或是 miniconda。
因為在大部分情況下，Anaconda 的很多功能都用不到，所以安裝體積更小的 miniconda 才是好選擇。

## 下載 miniconda 安装包
先使用 `uname -a` 來查看樹梅派的硬體架構，可以看到樹梅派是 aarch64，也就是 ARM64 架構。
```bash
uname -a
Linux rpiserver 6.12.25+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.12.25-1+rpt1 (2025-04-30) aarch64 GNU/Linux
```

再到 [miniconda官網](https://repo.anaconda.com/miniconda/)，找到對應的 aarch64 安裝包，然後使用 `wget` 來下載，安裝最新版的就好，如果偏好以前的版本再選擇其他的。
```bash
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
```

## 安裝 miniconda
下載完後，使用 bash 來安裝
```bash
bash Miniconda3-latest-Linux-aarch64.sh
```

你會先看到以下，直接看 `ENTER` 鍵就好
![image](https://hackmd.io/_uploads/SkiWr_vueg.png)

接著往下滑或按任何鍵，直到出現以下畫面，然後輸入 `yes`
![image](https://hackmd.io/_uploads/rJGISdwOgl.png)

然後會被詢問安裝位置，直接默認就好，直接按下 `ENTER` 鍵
![image](https://hackmd.io/_uploads/SyBtSOvOll.png)

接著會被問要不要自動初始化 conda，預設不要就好，直接按下 `ENTER` 
![image](https://hackmd.io/_uploads/ByqLIuPdee.png)

然後就可以看到安裝成功了
![image](https://hackmd.io/_uploads/BJytU_wOge.png)


## 設置環境變數
打開 `.bashrc` 來編輯。如果沒有安裝 vim 的話先安裝。
```bash
vim ~/.bashrc
```

進入後 vim，在最底下新增以下敘述
```
export PATH="$HOME/miniconda3/bin":$PATH
```
![image](https://hackmd.io/_uploads/rymnD_Pdxe.png)


然後按下 EXC 鍵，並輸入 `wq` 來保存定退出 vim。

輸入以下命令來更新環境變數
```bash
source ~/.bashrc
```

## 測試 conda
開啟一個新的終端機，來後輸入 `conda env list` 來看有沒有成功，成功的話會出現以下結果。
```bash
$ conda env list

# conda environments:
#
base                   /home/jeepway/miniconda3
```

就樣就大功告成了，之後就安裝你自己的環境吧，例如：
```bash
conda create -n myenv python=3.11
```