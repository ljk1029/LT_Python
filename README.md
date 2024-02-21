# Python
    Large model artificial intelligence

## API
    https://docs.python.org/zh-cn/3/
    https://www.liaoxuefeng.com/wiki/1016959663602400

## 提交说明
    -feat: 新功能（feature）
    -fix:  修补bug
    -refactor: 重构

## function
    基础语法

### pdb
    pdb 相当于gdb
    python3 -m pdb log.py

### 生成可执行文件
    pip install pyinstaller
    pyinstaller your_script.py
    
    1、问题1：若ssl问题则显示加载
    pyinstaller --hidden-import=_ssl ssh_win.py 