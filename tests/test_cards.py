import lost_spc.utils as ut
import lost_spc.calculations.spc_values as val
import lost_spc.constants as const
import lost_spc.calculations.control_limits as limits
import lost_spc.plots as plt

df = ut.load_data(".\\tests\\vane.txt", "csv", sep=" ", header=None)
print(df.head())
array = ut.data_to_array(df)
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
plt.shewhart_card(UCL, CL, LCL, R, title="R-chart", ylabel=r"$R_i$")

# cards
rchart = plt.cards.R(array)
rchart.fit(array)
rchart.transform(array)
