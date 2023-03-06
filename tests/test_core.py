#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

from china_water_use.core import ChineseWater


def test_change_scopes():
    """测试更新范围数据关心的范围"""
    cw = ChineseWater()
    assert cw.data.shape == (16709, 63)
    cw.update_scope("sectors", include=["IRR", "IND"], exclude=["IND"])
    assert cw.measurements == {"Magnitude", "WU", "WUI"}
    assert cw.sectors == {"IRR"}
    # 更新时间
    cw.update_scope("Year", list(range(1966, 1978)))
    assert cw.data.shape == (4092, 18)
    cw.update_scope("Province_n", ["Anhui", "Chongqing"])
    assert cw.data.shape == (204, 18)
