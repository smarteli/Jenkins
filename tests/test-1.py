# 4. 學習 pytest 測試框架
# pytest 是一個比 unittest 更簡潔、更靈活的測試框架。

# 基本用法：
# 安裝 pytest：pip install pytest

# 編寫測試腳本：

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
