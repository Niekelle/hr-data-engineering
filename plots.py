import re
import matplotlib.pyplot as plt
from pypalettes import load_cmap
import os

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'Arial', 'Verdana'] 
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelcolor'] = '#333333'

def plts (data: list, file: str,  hr_avg: float, hr_variance: float):
    """
    takes list of cleaned heart rate data, plots it, and saves it to the images folder

    """
    # color palette
    cmap = load_cmap('AndyWarhol')
    
    plt.style.use('fivethirtyeight')
    plt.figure(figsize=(10, 6))
    plt.plot(data, color = cmap.colors[0], linewidth = 2.5)

    # get phase name
    raw_name = os.path.splitext(os.path.basename(file))[0]
    phase_name = re.sub(r"([a-zA-Z]+)([0-9]+)", r"\1 \2", raw_name).upper()

    # set y-axis limits for easier comparisons
    plt.ylim(40, 130)

    # label plot
    plt.ylabel("Heart Rate (BPM)", fontweight = 'bold', labelpad = 15)
    plt.xlabel("Reading Number", labelpad = 12)
    plt.title(f"{phase_name}", fontstyle = 'italic', pad = 20)

    # stats box
    stats_text = f"Average: {hr_avg}\nVariance: {hr_variance}"
    plt.text(0.95, 0.92, stats_text, transform=plt.gca().transAxes,
             verticalalignment = 'top', horizontalalignment='right',
             bbox=dict(boxstyle = 'round', facecolor= "white", alpha=0.7))

    # save plots
    save_path = os.path.join('images', f'figure_{phase_name}.svg')
    plt.savefig(save_path, bbox_inches='tight')

    print(f"Saved: {save_path}")

    plt.show() 

    plt.close()