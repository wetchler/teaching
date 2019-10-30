#!/usr/bin/python
'''Utility functions for exploratory data analysis (EDA).

Author: Everett Wetchler
'''

import seaborn as sns


#############################################################################
# Colorblind palette
#############################################################################


# Colors changed in seaborn 0.9 (from 0.8)
version = [int(x) for x in sns.__version__.split('.')]
if version >= [0, 9, 0]:
    (COLOR_BLUE, COLOR_GREEN, COLOR_ORANGE, COLOR_RED,
     COLOR_PURPLE, COLOR_BROWN, COLOR_PINK, COLOR_GRAY,
     COLOR_YELLOW, COLOR_LIGHTBLUE) = sns.color_palette("colorblind")

    def activate_colorblind():
        sns.set_palette(sns.color_palette("colorblind"))


#############################################################################
# Cal (UC Berkeley) palette
# from brand.berkeley.edu/colors/
#############################################################################

# Primary palette
COLOR_CAL_BERKELEY_BLUE = "#003262"
COLOR_CAL_S_ROCK = "#3B7EA1"
COLOR_CAL_CALIFORNIA_GOLD = "#FDB515"
COLOR_CAL_MEDALIST = "#C4820E"
# Primary palettes
COLOR_CAL_WELLMAN_TILE = "#D9661F"
COLOR_CAL_ROSE_GARDEN = "#EE1F60"
COLOR_CAL_GOLDEN_GATE = "#ED4E33"
COLOR_CAL_SOUTH_HALL = "#6C3302"
COLOR_CAL_BAY_FOG = "#DDD5C7"
COLOR_CAL_LAWRENCE = "#00B0DA"
COLOR_CAL_LAP_LANE = "#00A598"
COLOR_CAL_PACIFIC = "#46535E"
COLOR_CAL_SATHER_GATE = "#B9D3B6"
COLOR_CAL_ION = "#CFDD45"
COLOR_CAL_SOYBEAN = "#859438"
COLOR_CAL_STONE_PINE = "#584F29"

COLOR_PALETTE_CAL = [
    COLOR_CAL_BERKELEY_BLUE,
    COLOR_CAL_CALIFORNIA_GOLD,
    COLOR_CAL_S_ROCK,
    COLOR_CAL_MEDALIST,
    COLOR_CAL_BAY_FOG,
    COLOR_CAL_PACIFIC,
    COLOR_CAL_SATHER_GATE,
    COLOR_CAL_STONE_PINE,
    COLOR_CAL_SOUTH_HALL,
    COLOR_CAL_ION,
#     COLOR_CAL_WELLMAN_TILE,  # Too similar to other reds
    COLOR_CAL_GOLDEN_GATE,
    COLOR_CAL_ROSE_GARDEN,
    COLOR_CAL_LAWRENCE,
    COLOR_CAL_LAP_LANE,
    COLOR_CAL_SOYBEAN,
]

def activate_cal():
    sns.set_palette(sns.color_palette(COLOR_PALETTE_CAL))


#############################################################################
# Stanford palette
#############################################################################


COLOR_STANFORD_CARDINAL_RED_PANTONE = "#8C1515"
COLOR_STANFORD_BACKGROUND_BLUE = "#F0F4F5"
COLOR_STANFORD_GRAY_BLUE = "#D0D8DA"
COLOR_STANFORD_DARK_GRAY_BLUE = "#AABEC6"
COLOR_STANFORD_ACCENT_BLUE_PANTONE = "#009ABB"
COLOR_STANFORD_LINK_BLUE_PANTONE = "#007C92"
COLOR_STANFORD_DARK_BLUE = "#09425A"
COLOR_STANFORD_LIGHT_GREEN_PANTONE = "#C7D1C6"
COLOR_STANFORD_BRIGHT_GREEN = "#80982A"
COLOR_STANFORD_DARK_GREEN = "#556222"
COLOR_STANFORD_ORANGE_PANTONE = "#B96D12"
COLOR_STANFORD_PURPLE_PANTONE = "#53284F"
COLOR_STANFORD_MAROON_PANTONE = "#5E3032"

COLOR_PALETTE_STANFORD = [
  # I'm organizing this like a paired palette
  COLOR_STANFORD_CARDINAL_RED_PANTONE,
  COLOR_STANFORD_BRIGHT_GREEN,
  COLOR_STANFORD_DARK_GREEN,
  COLOR_STANFORD_LIGHT_GREEN_PANTONE,
  COLOR_STANFORD_DARK_BLUE,
  COLOR_STANFORD_LINK_BLUE_PANTONE,
  COLOR_STANFORD_ORANGE_PANTONE,
  COLOR_STANFORD_MAROON_PANTONE,
  COLOR_STANFORD_PURPLE_PANTONE,
  COLOR_STANFORD_DARK_GRAY_BLUE,
  # COLOR_STANFORD_BACKGROUND_BLUE,  # Too light
  # COLOR_STANFORD_GRAY_BLUE,  # Too light
  # COLOR_STANFORD_ACCENT_BLUE_PANTONE,  # too similar to link blue
]

def activate_stanford():
    sns.set_palette(sns.color_palette(COLOR_PALETTE_STANFORD))


#############################################################################
# Everett's "personal brand" palette
#############################################################################


COLOR_PALETTE_EVERETT = [  # With help from from coolors.co
    '#131112',  # Licorice
    '#F5F5F8',  # White smoke
    '#B8AEA9',  # Greige
    '#656B7B',  # Chair
    '#645F65',  # Granite
]


def activate_everett():
    sns.set_palette(sns.color_palette(COLOR_PALETTE_EVERETT))
