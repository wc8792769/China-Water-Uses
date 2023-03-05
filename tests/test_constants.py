#!/usr/bin/env python 3.11.0
# -*-coding:utf-8 -*-
# @Author  : Shuang (Twist) Song
# @Contact   : SongshGeo@gmail.com
# GitHub   : https://github.com/SongshGeo
# Website: https://cv.songshgeo.com/

import pandas as pd

from src.constants import IRR, select, select_items

data = pd.read_csv("src/data/values_data.csv")
all_columns = data.columns

selection = [
    "City_ID",
    "Province_n",
    "Year",
    "Industrial WUI: Thermal electrivity",
    "Rural domestic WUI",
    "Irrigation water-use intensity (WUI): Maize",
    "Irrigation water-use intensity (WUI): Others",
    "Industrial WUI: Cements",
    "Industrial WU: Mining",
    "Irrigation WU: Maize",
    "Industrial WU: Textile",
    "Industrial WU: Others",
    "Industrial WUI: Mining",
    "Industrial WU: Cements",
    "Industrial WU: Electronics",
    "Industrial WU: Machinery",
    "Urban service WUI",
    "Industrial WUI: Papermaking",
    "Industrial WUI: Machinery",
    "Industrial WUI: Electronics",
    "Industrial WU: Food",
    "Industrial WUI: Food",
    "Rural livestock WU",
    "Urban domestic WU",
    "Industrial WUI: Textile",
    "Industrial WUI: Petrochemicals",
    "Rural livestock WUI",
    "Irrigation water-use intensity (WUI): Wheat",
    "Irrigation WU: Others",
    "Industrial WU: Thermal electrivity",
    "Rural domestic WU",
    "Industrial WUI: Metallurgy",
    "Irrigation water-use intensity (WUI): Vegetables and fruits",
    "Irrigation water-use intensity (WUI): Rice",
    "Irrigation WU: Rice",
    "Industrial WU: Metallurgy",
    "Industrial WU: Petrochemicals",
    "Industrial WUI: Others",
    "Irrigation WU: Wheat",
    "Irrigation WU: Vegetables and fruits",
    "Industrial WU: Papermaking",
    "Urban domestic WUI",
    "Urban service WU",
    "RUR",
    "URB",
    "IRR",
    "IND",
    "Total water use",
]
IRR_WU = [
    "Irrigation WU: Rice",
    "Irrigation WU: Wheat",
    "Irrigation WU: Maize",
    "Irrigation WU: Vegetables and fruits",
    "Irrigation WU: Others",
]
IND_WU = [
    "Industrial WU: Textile",
    "Industrial WU: Papermaking",
    "Industrial WU: Petrochemicals",
    "Industrial WU: Metallurgy",
    "Industrial WU: Mining",
    "Industrial WU: Food",
    "Industrial WU: Cements",
    "Industrial WU: Machinery",
    "Industrial WU: Electronics",
    "Industrial WU: Thermal electrivity",
    "Industrial WU: Others",
]

URB_WU = ["Urban domestic WU", "Urban service WU"]
RUR_WU = ["Rural domestic WU", "Rural livestock WU"]


IRR_WUI = [
    "Irrigation water-use intensity (WUI): Rice",
    "Irrigation water-use intensity (WUI): Wheat",
    "Irrigation water-use intensity (WUI): Maize",
    "Irrigation water-use intensity (WUI): Vegetables and fruits",
    "Irrigation water-use intensity (WUI): Others",
]
IND_WUI = [
    "Industrial WUI: Textile",
    "Industrial WUI: Papermaking",
    "Industrial WUI: Petrochemicals",
    "Industrial WUI: Metallurgy",
    "Industrial WUI: Mining",
    "Industrial WUI: Food",
    "Industrial WUI: Cements",
    "Industrial WUI: Machinery",
    "Industrial WUI: Electronics",
    "Industrial WUI: Thermal electrivity",
    "Industrial WUI: Others",
]
RUR_WUI = ["Rural domestic WUI", "Rural livestock WUI"]
URB_WUI = ["Urban domestic WUI", "Urban service WUI"]


def test_selections():
    # for each sectors
    assert select_items(sectors="IRR", measurements="WU") == IRR_WU
    assert select_items(sectors="IND", measurements="WU") == IND_WU
    assert select_items(sectors="URB", measurements="WU") == URB_WU
    assert select_items(sectors="RUR", measurements="WU") == RUR_WU
    # for each sectors
    assert select_items(sectors="IRR", measurements="WUI") == IRR_WUI
    assert select_items(sectors="IND", measurements="WUI") == IND_WUI
    assert select_items(sectors="URB", measurements="WUI") == URB_WUI
    assert select_items(sectors="RUR", measurements="WUI") == RUR_WUI
    # 俩俩组合
    assert set(select_items(sectors=["IRR", "IND"], measurements="WU")) == {
        *IRR_WU,
        *IND_WU,
    }
    assert set(select_items(sectors=["URB", "RUR"], measurements="WU")) == {
        *URB_WU,
        *RUR_WU,
    }
    assert set(select_items(sectors="IRR")) == {*IRR_WUI, *IRR_WU}
    set1 = set(select(include_summary=True))
    set2 = set(selection)
    assert set1 == set2, f"Sets are not the same: {set1} and {set2}"


def test_summary():
    for i in (data[[f"Irrigation WU: {crop}" for crop in IRR]].sum(axis=1) / 1e5).round(
        5
    ) == data["IRR"].round(5):
        assert i is True
    # assert (data[[f'Industrial WU: {ind}' for ind in IND]].sum(axis=1)).round(5) == data['IND'].round(5)
