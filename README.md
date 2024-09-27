### Introduction
This approach provides a simple solution for auto-sign-in in NTU's signing website and provide a random time sign-in function. Simple libraries such as `webdriver`, `selenium`, `apscheduler` and `random` were used to realize this thought.

For example, you can install these packages with `pip install` in the terminal:
```{shell}
pip install webdriver
pip install selenium
pip install apscheduler
pip install random
```

> [!WARNING]  
> 1. You need a desktop with wired internet IP in NTU to execute the program.
> 2. This approach use `ChromeDriver` for automation, please download and install the corresponding [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-tw) to make sure the process is supported. 

### Environment
`Python >= 3.7` (confirmed)

### Usage
Edit the account name and password for user:
```{python}
username: "your_username"
password: "your_password"
```
Execute the program code and then confirm that the computer will not shut down.

### Roadmap
- [x] Add random time sign-in
- [x] Add apscheduler for automation
- [ ] Add sign-out function
- [ ] Bundle .py and its api files into .exe packages


