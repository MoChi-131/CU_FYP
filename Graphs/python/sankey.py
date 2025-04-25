import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ['Wages', 'Others', 'Budget', 'Rent', 'Food', 'Transport', 'Entertainment', 'Savings'],
      color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
    ),
    link = dict(
      source = [0, 1, 2, 2, 2, 2, 2], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 2, 3, 4, 5, 6, 7],
      value = [1500, 250, 700, 300, 100, 150, 500],
      color=['rgba(31, 119, 180, 0.4)', 'rgba(255, 127, 14, 0.4)', 'rgba(44, 160, 44, 0.4)', 
               'rgba(214, 39, 40, 0.4)', 'rgba(148, 103, 189, 0.4)', 'rgba(140, 86, 75, 0.4)', 
               'rgba(227, 119, 194, 0.4)']
  ))])

fig.update_layout(title_text="Budget", font_size=10)
fig.show()