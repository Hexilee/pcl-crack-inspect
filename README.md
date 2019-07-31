### 通过管道点云寻找裂缝

#### 技术栈

`python3`、`numpy` 和 `python-pcl`

安装

```bash
brew install python3 &&
brew install python3-pip &&
pip3 install numpy cython
```

下载 `python-pcl` 源码，进入 `python-pcl-master` 目录

```bash
brew install pcl &&
python3 setup.py build_ext -i &&
python3 setup.py install
```

#### 实现

- 载入 `xyz` 文件
- 通过 `numpy.array` 和 `pcl.PointCloud` 生成点云对象
- 分割并配置参数生成模型
- 机器学习检测漏洞


