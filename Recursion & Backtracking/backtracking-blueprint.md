# Backtracking Blueprint

Table of Contents
-----------------

* [中心思想](#中心思想)
* [解题模版](#解题模版)
* [数形结合](#数形结合)
* [特别鸣谢](#特别鸣谢)



## 中心思想

解决一个回溯问题，实际上就是一个决策树的遍历过程



## 解题模版

```python
# 决策树结果集
result = []


def backtracking(当前选择列表, 待选择列表):

    if 满足结束条件:
        result.add(当前选择列表)
        # 任务完成
        return

    for 选择 in 待选择列表:
      
        # 将选择加入当前选择列表
        做选择(极有可能需要条件判断)
        # 进入决策树下一层
        backtracking(当前选择列表, 待选择列表)
        # 回溯
        撤销当前选择

```





## 数形结合

<div align="center"> <img src="backtracking.jpg" width="60%"/> </div><br>



## 特别鸣谢

- [回溯算法解题套路框架](https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/3.1-hui-su-suan-fa-dfs-suan-fa-xi-lie/hui-su-suan-fa-xiang-jie-xiu-ding-ban)

