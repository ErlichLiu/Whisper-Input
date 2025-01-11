# Whisper Input

Whisper Input 是受到即友[FeiTTT](https://web.okjike.com/u/DB98BE7A-9DBB-4730-B6B9-2DC883B986B1)启发做的一个简单的 python 代码。可以实现按下 Option 按钮开始录制，抬起按钮就结束录制，并调用 Groq Whisper Large V3 Turbo 模型进行转译，由于 Groq 的速度非常快，所以大部分的语音输入都可以在 1-2s 内反馈。并且得益于 whisper 的强大能力，转译效果非常不错。

## 功能

| 功能           | 快捷键                          |
| -------------- | ------------------------------- |
| 多语言语音转译 | Option 或者 Alt                 |
| 中文翻译为英文 | Shift + Option 或者 Shift + Alt |



查看[视频效果演示](https://img.erlich.fun/personal-blog/uPic/WhisperInputV02_compressed.mp4)



**重点：Groq 只要注册，就提供一定的免费用量，并且在我们这个使用场景下免费已经完全够用了！**

**🧐 当然，如果你在国内使用，并且无法访问 Groq 或者无法获得 Groq API，也欢迎反馈。因为我过去还做了一个 Groq 的 Whisper 代理池，理论上可以免费提供相对比较大的并发以及日常使用。但这需要你来单独申请，我会根据大家的需求考虑在后续的代码更新里添加对应的支持**

## 使用方法

1. 注册 Groq 账户：https://console.groq.com/login
2. 复制 Groq 免费的 API KEY：https://console.groq.com/keys
3. 打开 `终端` ，进入到想要下载项目的文件夹
    ```bash
    git clone git@github.com:ErlichLiu/Whisper-Input.git
    ```
4. 创建虚拟环境 【推荐】
    ```bash
    python -m venv venv
    ```

5. 重命名 `.env` 文件
    ```bash
    cp .env.example .env
    ```

6. 粘贴在第 2 步复制的 API KEY 到 `.env`  文件，效果类似
    ```bash
    GROQ_API_KEY=gsk_z8q3rXrQM3o******************8dQEJCYz3QTJQYZ
    ```

7. 在最好不需要关闭的 `终端` 内进入到对应文件夹，然后激活虚拟环境
    ```bash
    # macOS / Linux
    source venv/bin/activate
    
    # Windows
    .\venv\Scripts\activate
    ```

8. 安装依赖
    ```bash
    pip install -r requirements.txt
    ```

9. 运行程序
    ```bash
    python main.py
    ```

    

**🎉  此时你就可以按下 Option 按钮开始语音识别录入啦！**



![image-20250111140954085](https://img.erlich.fun/personal-blog/uPic/image-20250111140954085.png)

## Tips

由于这个程序需要一直在后台运行，所以最好找一个自己不会经常下意识关掉的终端或者终端里的 Tab 来运行，不然很容易会不小心关掉。



关注作者个人网站，了解更多项目: https://erlich.fun





## 未来计划

[✅] 多语言转译功能

[✅] 中文或多语言转译为英文

[  ] 标点符号支持

[  ] 添加 Agents，或许可以实现一些屏幕截图，根据上下文做一些输入输出之类的



**如果你也有想法：** 欢迎 Fork 和 PR，如果你在使用当中遇到问题，欢迎提交 Issue。

## 协议

遵循 MIT 协议