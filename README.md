
中国用水数据
======

这个 Python 包提供了一些函数，用于加载、整理和绘制中国用水数据。它还允许用户将数据转换为不同的单位。

特点
--

1. **数据加载**: 从各种来源加载中国用水数据，包括政府网站和研究论文。
2. **数据组织**: 将数据组织成易于处理的标准格式和结构。
3. **数据可视化**: 创建数据可视化，包括时间序列图和条形图。
4. **单位转换**: 将数据转换为不同的单位，以满足用户的需求。

安装
--

您可以通过 [pip](https://pip.pypa.io/en/stable/) 安装此软件包:

zsh

```zsh
pip install china-water-use
```

用法
--

python

```python
from china_water_use import ChineseWater

# 加载数据
cwu = ChineseWater()

# 组织数据
#
provinces = [
    "Qinghai",
    "Gansu",
    "Neimeng",
    "Ningxia",
    "Shanxi",
    "Shaanxi",
    "Henan",
    "Shandong",
]
# 更新研究范围:
    # - 关注以下省份的城市
    # - 关注用水强度 (WUI)
    # - 关注灌溉行业
cities = cwu.update_scope("Province_n", provinces)
wui = cwu.update_scope("measurements", "WUI")
sectors = cwu.update_scope("sectors", "IRR")
cwu.data.head()

# 转换单位为 mm / km^2
data = cwu.units(data, unit='mm * km**-2')

# 绘制数据
print(cwu.items)  # 显示缩小关注范围后选定的条目
cwu.scaled_plots("Irrigation water-use intensity (WUI): Maize")
```

贡献
--

欢迎贡献! 如果您遇到任何错误或问题，请在 [GitHub 仓库](https://github.com/SongshGeo/China-Water-Uses) 上开启一个 issue。如果您想贡献代码，请打开一个 pull request。

许可证
---

本项目基于 MIT 许可证。有关详情，请参阅 [LICENSE](LICENSE) 文件。

数据来源
----

本项目使用来自 [Zhou (2020)](https://www.pnas.org/doi/10.1073/pnas.1909902117) 发表的论文的数据集。
