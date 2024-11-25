import matplotlib.pyplot as plt


def shewhart_card(
    UCL,
    CL,
    LCL,
    samples,
    calibration_samples=None,
    title="",
    ylabel="",
    fill_alpha=0.07,
    restrict_zero=True,
    ax=None,
):
    """
    Plots a shewhart_card. Draws either on an existing axis (ax) or creates a new figure.
    """
    if restrict_zero:
        if LCL < 0:
            LCL = 0

    if calibration_samples is not None:
        x_min = -len(calibration_samples)
    else:
        x_min = 0

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = None

    # Draw control limits
    ax.hlines([UCL, CL, LCL], x_min, len(samples) - 1, colors=["black"], alpha=0.8)
    area_height = (UCL - CL) / 3
    ax.hlines(
        [CL + area_height, CL + 2 * area_height, CL - area_height, CL - 2 * area_height],
        x_min,
        len(samples) - 1,
        colors=["black"],
        alpha=0.3,
        linestyles="dashed",
    )

    # Add some coloring for the areas
    width = (x_min, len(samples) - 1)
    ax.fill_between(width, CL - area_height, CL + area_height, alpha=fill_alpha, color="green")
    ax.fill_between(width, CL + area_height, CL + 2 * area_height, alpha=fill_alpha, color="yellow")
    ax.fill_between(width, CL - area_height, CL - 2 * area_height, alpha=fill_alpha, color="yellow")
    ax.fill_between(width, CL + 2 * area_height, UCL, alpha=fill_alpha, color="red")
    ax.fill_between(width, CL - 2 * area_height, LCL, alpha=fill_alpha, color="red")

    # Plot points
    if calibration_samples is not None:
        ax.vlines(0, ymin=LCL, ymax=UCL, colors=["red"], linestyles="dotted", alpha=0.6)
        ax.plot(range(-len(calibration_samples), 0, 1), calibration_samples, "o-")
    ax.plot(range(len(samples)), samples, "o-")

    # Plot setup
    ax.set_title(title)
    ax.set_xlabel("Sample")
    ax.set_ylabel(ylabel)
    ax.grid()

    return fig if fig else ax
