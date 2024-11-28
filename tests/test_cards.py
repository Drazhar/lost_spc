from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

import lost_spc.calculations.control_limits as limits
import lost_spc.calculations.spc_values as val
import lost_spc.constants as const
import lost_spc.plots as plot
import lost_spc.utils as ut


def test_cards():
    """Sollte noch aufgeteilt werden in mehrere Tests für eine bessere Übersicht"""
    df = pd.read_csv(str(Path("./tests/vane.txt")), sep=" ", header=None)
    print(df.head())
    array = df.to_numpy()
    sample_size = ut.get_sample_size(array)
    n = sample_size.n
    m = sample_size.m
    print("Zeilen x Spalten: ", n, "x", m)

    # %% a) mean, range, std
    ybar = val.calculate_means(array)
    R = val.calculate_ranges(array)
    std = val.calculate_standard_deviations(array)
    print(ybar)
    print(R)
    print(std)

    d = const.get_d(m)
    d2 = d.d2
    d3 = d.d3
    print(d2, d3)

    # %% b) R-chart
    control_limits = limits.calculate_control_limits(array, chart_type="R")
    UCL = control_limits["UCL"]
    CL = control_limits["CL"]
    LCL = control_limits["LCL"]

    print("R-Karte UCL: ", UCL)
    print("R-Karte CL: ", CL)
    print("R-Karte LCL: ", LCL)

    # plots
    # Erstelle eine Figur mit Subplots
    _, axes = plt.subplots(1, 2, figsize=(8, 10))

    # Erster Subplot: R-Chart
    plot.shewhart_card(UCL, CL, LCL, R, title="R-chart", ylabel=r"$R_i$", ax=axes[0])

    # Zweiter Subplot: R-Karte aus der Klasse
    rchart = plot.cards.R()
    rchart.fit(array)
    rchart.transform(array, ax=axes[1])

    # Subplots optimieren und anzeigen
    plt.tight_layout()
    plot.plots.plot_histogram_normal(array.flatten())
    plot.plots.plot_qq_plot(array.flatten())

    print(limits.get_confidence_interval_cp(val.calculate_cp(UCL, LCL, std.mean()), array, 0.95))

    array.reshape(-1)
    ewmachart = plot.cards.EWMA(lambda_=0.2, plot_calibration_data=True)
    ewmachart.fit(array)
    ewmachart.transform(array + 2)
    # plt.show()
