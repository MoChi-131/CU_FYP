import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.abspath('..'))

def sankey(data):
  
  node_colors = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78'
    ]
  targets = [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  sources = [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
  
  link_colors = [
        f"rgba({int(node_colors[src][1:3], 16)}, {int(node_colors[src][3:5], 16)}, {int(node_colors[src][5:7], 16)}, 0.6)"
        if src in [0, 1] else
        f"rgba({int(node_colors[tgt][1:3], 16)}, {int(node_colors[tgt][3:5], 16)}, {int(node_colors[tgt][5:7], 16)}, 0.6)"
        for src, tgt in zip(sources, targets)
    ]
  
  fig = go.Figure(data=[go.Sankey(
      node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ['Wages', 'Others', 'Budget', "Toll", "Food", "Parking", "Transport", "Accommodation", "Gasoline", "Telecom", "Miscellaneous", 'Savings'],
        color= node_colors
      ),
      link = dict(
        source = [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        target = targets,
        value = data,
        color=link_colors
    ))])
  
  fig.update_layout(
    width=700,  # Set figure width
    height=500,   # Set figure height
    margin=dict(l=0, r=0, b=0, t=10),
    font=dict(size=15.5, color='black')
  )

  output_path = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Interface\static\Sankey.html"
  fig.write_html(output_path)
  print("saved")

  
if __name__ == "__main__":
  value = [1500, 250, 200, 300, 100, 150, 200, 100, 50, 300, 250]
  sankey(value)