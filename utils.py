import os

def draw_line():
    try: columns = os.get_terminal_size().columns
    except OSError:columns = 80 
    print("-" * columns)

def gpm_to_gpd(gpm):
    return gpm * 1440
def gpd_to_gpm(gpd):
    return gpd / 1440