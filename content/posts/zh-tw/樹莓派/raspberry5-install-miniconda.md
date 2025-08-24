---
title: 在 Raspberry Pi 安裝 miniconda
date: '2025-08-11T21:35:44+08:00'
lastmod: '2025-08-24T16:06:20+08:00'
draft: false
categories:
- 樹莓派
tags:
- 樹莓派
- Miniconda
featuredImage: https://lh3.googleusercontent.com/pw/AP1GczOMoMMqDLhSCJ70DuG2pxShS61Lzp9OLtslZVVebqTyVk5FYlAesWLzRsKSlaCPMrjO7y-cnXruJMZdByMFLkfwCSTvfe5-MyFBJFNebi7PH-HVmq9aTONRX1SFHUOiGwlrdW6_eo6dkx6FCJLp9xzH=w819-h378-s-no-gm
featuredImagePreview: null
---

介紹如何在 Raspberry Pi 5 上安裝 Miniconda，其他版本的樹莓派也適用。你也可以安裝 Anaconda，但是大部分功能都沒用到，所以可以安裝 Miniconda 就好。

<!--more-->

## 前言
為了讓每個 python 專案有自己的專屬環境來管理套件，而不去影響其他專案，最好是安裝環境管理系統，像是 Anaconda 或是 miniconda。
因為在大部分情況下，Anaconda 的很多功能都用不到，所以安裝體積更小的 miniconda 才是好選擇。

## 下載 miniconda 安装包
先使用 `uname -a` 來查看樹莓派的硬體架構，可以看到樹莓派是 aarch64，也就是 ARM64 架構。
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
<img src="https://lh3.googleusercontent.com/pw/AP1GczONH4anKnGeuBwNUGZpjCRYg5LxfQsJZeXIltIYso7rsWX8JrwJ0xUTBWvkRfcbQHN_hJjwQqa95iBRh9Q27RSHH7u5_jsH9qQL_P5B4o0aG6Fa-1BjlRKEXU4Bat5fLIjjJq1_cnjC6Wo73qhfBWS1=w663-h154-s-no-gm?authuser=0" alt="rpi5-install-miniconda-step1" title="rpi5-install-miniconda-step1">

接著往下滑或按任何鍵，直到出現以下畫面，然後輸入 `yes`  
<img src="https://lh3.googleusercontent.com/pw/AP1GczO9ehYco92oz3WFLxAe2-rLWvG8H45AO_C4mE4U2KFcUu6GCthudPrynQTXuZODoLL7Z7s6Oo5uUA0NPMU2LYewdCoMQyJYDGzPRJbuPI0EptcOmZJKU1ENF41NytUoTFCobgUaSmehhfZIobdln2Ff=w1105-h559-s-no-gm?authuser=0" alt="rpi5-install-miniconda-step2" title="rpi5-install-miniconda-step2">

然後會被詢問安裝位置，直接默認就好，直接按下 `ENTER` 鍵  
<img src="https://lh3.googleusercontent.com/pw/AP1GczO7uTLhK7hREqDFFJsiCglkNXMqOT_V-51QDCyIGC0TV01F_iC5fNK5h5W1rY5C_bnWx2Yh_omBA0Lp__S6BHxaDKAr5ubgAr0jSM6F3Hf9PftlANdoxhT0A4_dqX1k4DDfpVEo0BDUfrQaVO63_1DJ=w493-h220-s-no-gm?authuser=0" alt="rpi5-install-miniconda-step3" title="rpi5-install-miniconda-step3">

接著會被問要不要自動初始化 conda，預設不要就好，直接按下 `ENTER`  
<img src="https://lh3.googleusercontent.com/pw/AP1GczMS1ODzS0oGwXxq8G-0g3ph11CKzGHROYVCXSJMV7P2v9jLsLcNRYk2iFtbom2OuqNa_9cvDhAgYPkJqGJBJm8-0uQiU0RPl2GNqNFXjbRKSftZNcupVy-MlCKBFlPWD0Nx3xOdbZRbfNeR_u4O10o8=w822-h311-s-no-gm?authuser=0" alt="rpi5-install-miniconda-step4" title="rpi5-install-miniconda-step4">

然後就可以看到安裝成功了  
<img src="https://lh3.googleusercontent.com/pw/AP1GczNDDvraVi5_nW_R7jO_XtbDPvby6NyH1qvI_eMRtADy7YQe-xP6EXtPIwUPWiEPaGKno3GI7os8c_rhP6akbpzP9E06qZn0HyclCe_zBEgG1t2dg1TZmJ01v6c-JN2YcQBHhv02U-cESTp_d4T3ZRrL=w696-h215-s-no-gm?authuser=0" alt="rpi5-install-miniconda-step5" title="rpi5-install-miniconda-step5">

## 設置環境變數
打開 `.bashrc` 來編輯。如果沒有安裝 vim 的話先安裝。
```bash
vim ~/.bashrc
```

進入後 vim，在最底下新增以下敘述
```
export PATH="$HOME/miniconda3/bin":$PATH
```
<img src="https://lh3.googleusercontent.com/pw/AP1GczMpUg6OdK7hLTmEvpFwCX4XFycCrbmyElugcqfW2iD8TnmJFnGhw0Z1Nf1MbPkWBt8W5z67-ScSTQCwIpqApcpuoj33_DLGkM5T69d1Mgk683bW0WiwUpul-g2SD-jw5qP55xvYagHP1aTgUhl15p59=w630-h237-s-no-gm?authuser=0" alt="rpi5-install-miniconda-step6" title="rpi5-install-miniconda-step6">


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