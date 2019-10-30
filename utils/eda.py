#!/usr/bin/python
'''Utility functions for exploratory data analysis (EDA).

Author: Everett Wetchler, 2015
'''

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns


import color


#################################################################
# Summary statistics, missing data
#################################################################

def _truncate_str(s, n=15):
    '''Returns string s truncated to n characters, with elipsis as needed...'''
    s = str(s)
    return s if len(s) <= n else s[:(n - 3)] + '...'


def percentify_axis(x_or_y_axis):
    x_or_y_axis.set_major_formatter(
        mtick.PercentFormatter(xmax=1, decimals=decimals))


def percentify_x(ax, decimals=None):
    percentify_axis(ax.xaxis)


def percentify_y(ax, decimals=None):
    percentify_axis(ax.yaxis)


def smart_value_counts(s, top=10, normalize=True, percent=False,
                       sort_index=False, truncate=True):
    '''Similar to s.value_counts() in pandas, but with rollups and pcts.'''
    vc = s.value_counts(ascending=False, normalize=normalize)
    if sort_index:
        vc = vc.sort_index()
    if truncate:
        vc.index = [_truncate_str(i) for i in vc.index]
    out = vc[:top]
    if vc.sum() > out.sum():
        other = pd.Series(
            [vc.sum() - out.sum()],
            index=['[OTHER] (%d types)' % (len(vc) - len(out))])
        out = out.append(other)
    na = 1.0 - vc.sum()
    if na > 0:
        out = out.append(
            pd.Series([na], index=['[NA (%.0f%%)]' % abs(na * 100)]))
    if percent:
        return out.apply(lambda p: '%.2f%%' % abs(p * 100))
    return out


COLOR_HIST_DEFAULT = COLOR_BLUE #(0.86, 0.3712, 0.34)
COLOR_BAR_DEFAULT = COLOR_GREEN #(0.5688, 0.86, 0.34)
COLOR_NA_DEFAULT = COLOR_ORANGE #(.8, .2, .2)
ALPHA_BAR_DEFAULT_DEFAULT = 1.0  #0.8


def smart_hist(s, ax, rugplot=False, color=COLOR_HIST_DEFAULT,
               color_na=COLOR_NA_DEFAULT, alpha=ALPHA_BAR_DEFAULT):
    s = s.astype(float)
    s.hist(ax=ax, color=color, weights=np.zeros(s.count()) + 1. / len(s),
           alpha=alpha)
    ax.set_yticklabels(['%.0f%%' % (t * 100) for t in ax.get_yticks()])
    na = 1.0 - float(s.count()) / len(s)
    if na > 0:
        ax.plot([min(ax.get_xticks()), max(ax.get_xticks())], [na, na],
                color=color_na, label='NA (%.0f%%)' % (na * 100),
                alpha=0.8 if na else 0,
                linestyle='--')
        ax.legend(loc='upper right')
    if rugplot:
        sns.rugplot(s, color=color, alpha=1.0, ax=ax)


def smart_bar(s, ax, color=COLOR_BAR_DEFAULT, color_na=COLOR_NA_DEFAULT,
              alpha=ALPHA_BAR_DEFAULT, sort_index=False, truncate=True):
    s = smart_value_counts(s, truncate=truncate)
    s[::-1].plot(ax=ax, kind='barh', color=color, alpha=alpha)
    ax.set_xticklabels(['%.0f%%' % (t * 100) for t in ax.get_xticks()])


def dist_plot(s, ax, color=COLOR_BAR_DEFAULT, color_na=COLOR_NA_DEFAULT,
              alpha=ALPHA_BAR_DEFAULT, sort_index=False):
    pass

#################################################################
# Correlations
#################################################################

def scatter(df, x_col, y_col, labels=None):
    fig, ax = plt.subplots(1)
    ax.scatter(df[x_col], df[y_col], alpha=0.6, s=40)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    if labels is not None:
        for i, lab in enumerate(labels):
            x, y = (df[x_col].iloc[i], df[y_col].iloc[i])
            ax.annotate(lab, xy=(x, y), xytext = (x - 60, y + 20), fontsize=12)
    return fig, ax


def scatter_colored(df, x_col, y_col, color_var):
    fig, ax = plt.subplots(1)
    colors = sns.color_palette('hls', len(df[color_var].value_counts()))
    for i, pair in enumerate(sorted(list(df.groupby(color_var)))):
        name, group = pair
        x, y = group[x_col], group[y_col]
        if x.count() and y.count():
            ax.scatter(x, y, alpha=0.6, s=40, color=colors[i], label=name)
    ax.legend()
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    return fig, ax


def univariate_corrs_bar(df, to_predict, method='pearson'):
    if not isinstance(to_predict, list):
        to_predict = [to_predict]
    corr = df.corr(method=method.lower())[to_predict]
    corr.drop(to_predict, axis=0, inplace=True)
    corr = corr.sort_index()[::-1]
    fig, ax = plt.subplots(1)
    fig.set_size_inches(12, 8)
    corr.plot(ax=ax, kind='barh')
    ax.set_title('Linear univariate correlations (Pearson R), N=%d' % len(df))
    ax.set_xlabel('R (%s)' % method.capitalize())
    ax.set_yticklabels(
        ['%s (%.0f%% NA)' % (
            c.get_text(),
            100 * (1 - float(df[c.get_text()].count())
                   / len(df[c.get_text()])))
            for c in ax.get_yticklabels()],
        fontsize=14)
    ax.legend(loc='upper right', frameon=True, fontsize=12)
    fig.subplots_adjust(left=0.4)
    return fig, ax


def add_fit(ax, a, b, orders=1, colors=None, fig=None):
    if not isinstance(orders, list):
        orders = [orders]
    if not colors:
        colors = ['gray']
        if len(orders) > 0:
            colors = sns.color_palette()[1:]
        if len(orders) > colors:
            colors = sns.color_palette('hls', len(orders))
    for i, o in enumerate(orders):
        col = colors[i]
        coeffs = np.polyfit(a, b, o)
        f = np.poly1d(coeffs)
        pred = f(a)
        r, p = pearsonr(pred, b)
        if o == 1 and coeffs[0] < 0:
            r = -r
        x = np.linspace(min(a), max(a), 200)
        y = f(x)
        lab = 'Fit line' if o == 1 else 'Fit deg-%d' % o
        ax.plot(x, y, color=col, alpha=0.7, linestyle='--',
                linewidth=2, label='%s (R2 = %.2f, p = %.2f)' % (lab, r, p))
    ax.legend(loc='upper right')


#################################################################
# Other utilities
#################################################################


def insert_col_after(df, s, name, after):
    cols = list(df.columns)
    i = cols.index(after)
    newcols = cols[:(i+1)] + [name] + cols[(i+1):]
    df[name] = s
    return df[newcols]


def insert_col_before(df, s, name, before):
    cols = list(df.columns)
    i = cols.index(before)
    newcols = cols[:i] + [name] + cols[i:]
    df[name] = s
    return df[newcols]


def insert_col_front(df, s, name):
    cols = list(df.columns)
    newcols = [name] + cols
    df[name] = s
    return df[newcols]
