+++
title = 'Window 11 下刪除雙系統中的 Ununtu'
date = '2025-08-14T01:42:18+08:00'
lastmod = '2025-08-16T14:13:00+08:00'
draft = false
categories = ['Ubuntu']
tags = ['Ubuntu', '雙系統']
+++

# Window 11 下刪除雙系統中的 Ununtu

當初裝 Ununtu 的容量切得太大了，幾乎都沒用到，導致 C 槽幾乎沒有空間，所以想要把 Ubuntu 砍掉重裝

- [刪除雙系統中的Ubuntu](https://medium.com/@wade3c/%E5%88%AA%E9%99%A4%E9%9B%99%E7%B3%BB%E7%B5%B1%E4%B8%AD%E7%9A%84ubuntu-90d8b2327669)
- [如何從我的電腦上卸載 Ubuntu](https://zh-tw.ubunlog.com/%E5%A6%82%E4%BD%95%E5%8D%B8%E8%BC%89ubuntu/)


## 刪除 Ununtu 占用的磁區

搜尋並點擊**電腦管理**，對 Ubuntu 所在的磁碟 (通常會是 EXT 格式) 按右鍵，然後選擇**刪除磁碟區**。
**備註：這邊的配置很怪，因為我之前用了 EaseUS Partition Master 來把 D 槽的一些容量切給 C 槽，導致 E 槽跟 1GB 空間出現問題，而 E 槽跟 1GB 空間對應原本的 Ubuntu 磁碟跟修復磁碟分割。**
![image](https://hackmd.io/_uploads/B1xDuT5_xe.png)

刪除後可以看到有尚未配置的空間，那這樣就是刪除了，如下面圖片
![image](https://hackmd.io/_uploads/SkIuFTqOle.png)

刪除後，在對 C 槽按右鍵，然後選擇**延伸磁碟區**，來收回未使用的空間
![image](https://hackmd.io/_uploads/BkjCY6qOxe.png)

確認是要延伸的區域，點擊**下一步**
![image](https://hackmd.io/_uploads/rJNH9pqOlg.png)

然後就可以看到 C 槽的空間變大了
![image](https://hackmd.io/_uploads/r1CBnT9uex.png)

透過 diskpart 命令可以查看到磁碟分割 5 確實是復原用的。可以參考這支影片：[Windows 11基礎教學-如何刪除修復磁碟分割並延伸磁碟區](https://www.youtube.com/watch?v=O94exmppO38)

![image](https://hackmd.io/_uploads/Bye3hT5_gg.png)

接著就同樣做法刪除該磁碟區並延伸，結果如下面
![image](https://hackmd.io/_uploads/SyC86a9dge.png)

刪除磁碟區後，就不需要每次都進到 GRUB 來選擇作業系統，因為這是 Linux 用的，我們現在已經用不到了，所以需要重新設定 Bootloader 的開機方式，可以參考這個文章：[How to Remove Ubuntu Dual Boot from Windows 10](https://linuxhint.com/remove-ubuntu-dual-boot-from-windows-10/)，

有兩種方法來重新設定：1. Through Command Prompt, 2. Using UEFI for changing Boot orders

我們先選擇 **Through Command Prompt** 方法，因為比較方便。先以系統管理員身分打開 cmd (system 32)，然後輸入以下命令。如果想知道命令細節，可以輸入 `bcdedit /?` 來查看說明

```bash
C:\WINDOWS\system32> bcdedit /set "{bootmgr}" path \efi\microsoft\boot\bootmgfw.efi
操作順利完成。
```

然後重新開機來看成果，發現沒有直接以 Window 開機，而是進到 GUN GRUB 介面，也就是上面的命令沒有正確更改開機順序。此外，即便我們已經刪除 Ubuntu 所在的硬碟分區，GRUB 還是繼續工作，因為 GRUB 是存放在**EFI 系統磁碟分割裡面**。
![image](https://hackmd.io/_uploads/BkQn0C9_ge.png)

此時就先輸入在 GRUB 命令列 輸入 `exit` 來重啟電腦，然後一直按 **F2 鍵**來進到 BIOS。進入 BIOS 以後，到 Boot 頁籤，在 Boot priority order 區塊，使用 **F6 鍵**把 Window Boot Loader 移到最上面，然後按 **F10 鍵**儲存並重啟電腦，這樣之後開機就不會再進入到 GRUB 介面，而是直接開啟 Window 作業系統。
至於要按下那些鍵來操作 BIOS 會取決於你的電腦，可以上網查詢相關資訊，我用的電腦是 Acer Aspire A515-57G。
![image](https://hackmd.io/_uploads/HyVE1yo_ee.png)

如果你不想那麼麻煩，可以直接採用方法二 Using UEFI for changing Boot orders，重啟後就可以選擇進入到 BIOS。詳細不走可以參考[這篇的 step1](https://itsfoss.com/uninstall-ubuntu-linux-windows-dual-boot/)


## 刪除 GRUB
- [Linux中GRUBX64.EFI和SHIMX64.EFI有什么区别？](https://blog.csdn.net/Linuxprobe18/article/details/124768794)

刪除 Ubuntu 所在的磁區後，若想要把 GUN GRUB 也刪除，那需要去把 EFI 磁碟裡面的 Ubuntu 資料夾全部刪光

### 以下方法無效
- 文章：[删除Ubuntu的UEFI启动项](https://blog.csdn.net/smilingc/article/details/51236717)
    > boot-repair可能只会让情况更加糟糕，请尽量不要使用。
    > 我的情况是，当年我用安装ubuntu并不是UEFI，然后直接导致我现在的windows启动有点问题，只要用legacy和uefi混合的模式就无法启动，然后我用boot-repair去修复，修复还是没有用而且导致我的UEFI多了好几项ubuntu的启动。总之就是我拔掉ubuntu的硬盘之后还是存在，看着心烦。
- 文章：[刪除 Ubuntu 後如何移除 GNU GRUB 開機載入程式畫面](https://www.reddit.com/r/Ubuntu/comments/n5zt9e/how_to_remove_gnu_grub_bootloader_screen_after/?tl=zh-hant)
    > 如果你可以安全地啟動 Windows，那就用管理員權限打開 cmd (system 32) 然後用 bcdedit /deletevalue {bootmgr} path \EFI\ubuntu\grubx64.efi 搞搞。很有可能這樣就能關掉 GRUB，讓你直接開機進你唯一的作業系統，也就是 Windows。

先使用以下命令查看 Ubuntu 的 UEFI 啟動區塊，通常是 shimx64.efi，或者是 grubx64.efi。補充一下，shimx64.efi 是一個相對簡單的程式，提供在安全啟動 (Secure Boot) 模式下的操作。
```bash
bcdedit /enum firmware
```

找到 Ubuntu efi 對應的 identifier，替換並執行以下命令
```bash
bcdedit /deletevalue {bootmgr} path \EFI\ubuntu\shimx64.efi

bcdedit /delete {identifier}
```

然後重新啟動進到 BIOS 來查看是否真的移除 Ubuntu 的開機選項了

補充，可以查看開機硬碟的命令
```
# 查看 bcdedit /enum 的使用手冊
bcdedit /? /enum

# 查看所有項目
bcdedit /enum ALL

# 查看所有開機管理程式項目
bcdedit /enum BOOTMGR

# 查看預設開機項目
bcdedit /enum {default}
```

### 以下方法有效 
- 來源影片：[How to safely remove Ubuntu (Linux) from dual boot in Windows 10/11](https://www.youtube.com/watch?v=H0hMHCZv7QY)

先以系統管理員身分打開 cmd，依序執行以下命令，選擇 Boot Loader 所在的磁碟分割，然後刪除 ubuntu 目錄。

執行完以下操作後，進入到 BIOS 查看開機順序、或是開機後使用 `bcdedit /enum firmware
` 來查看開機順序是否只剩下 Window，是的話就完工了！！

```bash=
C:\Windows\System32> diskpart

Microsoft DiskPart 版本 10.0.26100.1150

DISKPART> list disk

  磁碟 ###  狀態           大小     可用     Dyn  Gpt
  --------  -------------  -------  -------  ---  ---
  磁碟 0    連線              476 GB      0 B        *
  
DISKPART> select disk 0

磁碟 0 是所選擇的磁碟。

DISKPART> list partition

  磁碟分割  ###  類型              大小     位移
  -------------  ----------------  -------  -------
  磁碟分割  1    系統                 260 MB  1024 KB
  磁碟分割  2    保留                  16 MB   261 MB
  磁碟分割  3    主要                 248 GB   277 MB
  磁碟分割  4    主要                 227 GB   249 GB
 
DISKPART> select partition 1

磁碟分割 1 是所選擇的磁碟分割。

DISKPART> assign letter=x

DiskPart 成功地指派了磁碟機代號或掛接點。

DISKPART> exit

正在離開 DiskPart...

C:\Windows\System32> x:

X:\> dir
 磁碟區 X 中的磁碟是 ESP
 磁碟區序號:  F8S5-3F56

 X:\ 的目錄

2025/01/21  下午 02:25    <DIR>          EFI
               0 個檔案               0 位元組
               1 個目錄     203,378,688 位元組可用

X:\> cd EFI

X:\EFI> dir
 磁碟區 X 中的磁碟是 ESP
 磁碟區序號:  6674-3FDE

 X:\EFI 的目錄

2022/10/10  下午 04:20    <DIR>          .
2022/10/10  下午 04:20    <DIR>          ..
2025/01/21  下午 02:25    <DIR>          Microsoft
2025/01/21  下午 02:25    <DIR>          ubuntu
2023/02/28  上午 03:39    <DIR>          Boot
2022/10/10  下午 05:38    <DIR>          OEM
               0 個檔案               0 位元組
               5 個目錄     203,378,688 位元組可用
               
X:\EFI> dir ubuntu    
 磁碟區 X 中的磁碟是 ESP
 磁碟區序號:  6674-3FDE

 X:\EFI\ubuntu 的目錄

2022/10/10  下午 04:41    <DIR>          .
2022/10/10  下午 04:41    <DIR>          ..
2025/02/21  下午 05:36         2,656,136 grubx64.efi
2025/02/21  下午 05:36           966,664 shimx64.efi
2025/02/21  下午 05:36           856,280 mmx64.efi
2025/02/21  下午 05:36               108 BOOTX64.CSV
2025/02/21  下午 05:36               117 grub.cfg
               5 個檔案       4,479,305 位元組
               2 個目錄     198,887,184 位元組可用
              
X:\EFI> rd ubuntu /s
ubuntu, Are you sure (Y/N)? Y

X:\EFI> exit
```

