# pigCrypto施工规划

标签（空格分隔）： flappypig Crypto

---

[TOC]

##代码结构

### 0Xff 这是什么

pigCrypto是一个用于处理CTF中一些比较简单的密码题目的python库，同时也为更复杂的密码题目提供一套工具包。

目录树

```bash
.
└── pigCrypto
    ├── classic
    ├── coding
    ├── modern
    │   ├── padding
    │   ├── publicKey
    │   └── secretKey
    └── toolbox
        ├── block
        ├── ecc
        ├── pair
        ├── stream
        └── zp
```

## 合作开发思路
本代码托管在Github上，地址为https://github.com/FlappyPig/pigcrypto，在本规范中将Github上的代码仓库称为“远程仓库”。远程仓库有两个分支——master和dev，根据Github的最佳开发实践，master分支需要是随时可以部署的分支，因此，我们开发过程中不要往master分支中推送开发代码，任何自己开发的代码需要推送到远程的dev分支中（具体方法在第二节），阶段开发完成后再合并到master分支。
开发者使用“git clone”命令克隆远程仓库到本机的仓库，在本规范中称为“本地仓库”。开发者克隆生成本地仓库后，需要切换到dev分支（重要），然后在本地仓库中以dev分支为基础创建自己的分支，此后的所有代码添加及修改都提交到自己的分支。自己的阶段性开发任务完成后，将自己的分支合并到本地dev分支，随后推送到远程仓库的dev分支，最后可以选择性删除自己的分支。

## 开发具体命令及方法

### 工作流程

1. 克隆项目
2. 签出dev 分支。
3. 	在dev分支基础上创建自己的分支 member* 。
4. 在自己的分支上添加文件
5. 	在自己的分支上修改文件
6. 	合并到dev分支
7. 	推送本地dev分支到远程dev分支
### 命令
1. 	修改自己本地的git的用户名和邮箱设置
将自己本地的git的用户名和邮箱设置的与github相同，否则你推送之后显示的是别人推送的qwq。
```bash
$ git config --global user.name aaa
$ git config --global user.email aaa@aaa.com
```
2. 	设置本地仓库
 这一步克隆分支到本地，并且切换到dev分支，随后建立自己的分支。
```bash
$ cd [项目路径] 
$ git clone https://github.com/FlappyPig/pigcrypto  
$ git checkout dev
$ git checkout -b [MEMBER_NAME]  # [MEMBER_NAME] 是自己的分支名称
```
git checkout的-b参数表示新建分支，无参数表示切换到现有分支。

3. 	更新本地仓库
在这一步进行代码的开发，阶段性开发完成后将代码添加到本地仓库，注意提交注释写的尽量具体，add和commit的作用在第一节说明了
```bash
$ git add .  #这里可以列出具体要添加的文件，也可以使用.添加所有新增文件
$ git commit -m "提交注释"

```
-m参数后接注释，注释尽量写英文吧233
4. 将自己的分支合并到本地dev分支
本步是在阶段性开发完成后，将自己的分支合并到本地dev分支，准备推送到远程。自己的分支开发完成后，首先我们需要切换回dev分支，随后将自己分支的修改合并到dev分支。
```bash
$ git checkout dev
$ git merge --no-ff [MEMBER_NAME] -m "提交注释"  # [MEMBER_NAME] 是自己的分支名称
```
--no-ff参数表示强制生成merge日志。

5. 	将本地dev分支推送到远程
```bash
git push
```
使用该命令之前注意自己的本地分支是否在dev之下（git status查看）。

如果在推送过程中提示与远程dev分支发生冲突，需要先将远程dev分支同步到本地，解决冲突后再推送，平时尽量避免不同开发人员修改同一个文件。
处理代码如下，首先我们使用pull命令同步远程仓库到本地，此时git会提示你处理冲突，处理完成后保存文件。再使用add命令添加处理完的文件，随后commit提交本次冲突处理，然后再去push。
```bash
$ git push 
       #                                               # 遇到错误
$ git pull
       # …                                               # 解决冲突
$ git add .  #添加修改后的文件到本地仓库
$ git commit -m "solve conflict:由于XX原因出错，修改XX文件解决问题"
$ git push
```
6. 删除自己的分支（可选）
```bash
git checkout -d [MEMBER_NAME]  # [MEMBER_NAME] 是自己的分支名称
```
自己的本地分支的存在不会影响远程分支。
7. 	常用查询命令
```bash
$ git branch                          # 查看自己所在分支 以及自己所拥有的分支
$ git log --graph                      # 查看自己的提交记录
$ git reflog                                            # 查看自己的操作历史
$ git status                                        # 查看本地仓库当前的文件状态
$ git blame [FILE_PATH]                  # 查看文件的每一部分最后由谁改动
```
## python模块开发规范
本次开发我们尽量规范化开发。

1.	添加公开函数、模块、类和方法的文档字符串

 在公开函数的def定义下一行，使用"""定义注释，使用pycharm可以自动生成规范的文档字符串（通过在def下一行输入"""并回车），例如:
 ```py
def bbb(a, b):
    """
usage
    :param a:
    :param b:
    :return:
    """
```

 写一下该函数的功能、变量的意义和类型，返回值的意义和类型。
这个注释只在公开函数写即可。

2. 添加py文件的文档字符串

 在py文件的第一行（如何有编码声明和启动声明的话，则在他们后面），使用"""定义注释，在这里简要写一下py文件的功能，重点要写出适配的python版本（2、2.6、2.7、3、3.3、3.4、3.5）、需要事先安装好的其他模块，这两个部分需要在最后打包的时候用到，写的规范随意，能看懂就行。


3. python代码格式采用pep8

第一次合作开发，在过程中肯定会遇到各种问题，大家及时沟通~~
