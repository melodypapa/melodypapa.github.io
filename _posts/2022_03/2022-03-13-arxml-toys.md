---
layout: post
title:  "今日更新 - ARXML小玩具"
date:   2022-03-12 19:10:00 +0800
categories: autosar
---

前段日子应客户的要求做了一个处理**AUTOSAR**的**ARXML**的小工具，注意包含了以下几个功能：

* 移除ARXML文件里的UUID。
* 更新ARXML文件里的UUID。
* 移除ARXML文件里的时间戳。

可以通过https://github.com/melodypapa/arxml_toys下周源码，慢慢有空可以考虑上传到Python的仓库里。

说明：
1. 因为很多时候会复制**ARXML**内容，特别时**Implementation**的内容，这样就造成了UUID的重复，接着**AUTOSAR Builder**会报warning，客户说会影响Matlab的导入（个人每试过）
2. 时间戳是一个比较烦人的东西，有时候其实内容也没啥修改，就看见一堆时间戳的不同，用版本管理工具比较，一堆的红。在**AUTOSAR Builder**里还没看见有啥选项可以关闭。

