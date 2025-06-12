import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Cargar datos
df = pd.read_csv("data.csv")
df['date'] = pd.to_datetime(df['date'])

# Inicializar app Dash
app = Dash(__name__)
app.title = "Dashboard Interactivo"

# Layout
app.layout = html.Div([
    html.H1("📊 Dashboard Interactivo con Plotly", style={"textAlign": "center"}),

    html.Label("Selecciona categoría:"),
    dcc.Dropdown(
        id="category-dropdown",
        options=[{"label": cat, "value": cat} for cat in df["category"].unique()],
        value=df["category"].unique()[0]
    ),

    dcc.Graph(id="line-chart"),

    html.Hr(),

    dcc.Graph(id="bar-chart"),
])


# Callbacks
@app.callback(
    [Output("line-chart", "figure"),
     Output("bar-chart", "figure")],
    Input("category-dropdown", "value")
)
def update_charts(selected_category):
    filtered_df = df[df["category"] == selected_category]

    line_fig = px.line(
        filtered_df, x="date", y="value", title=f"Tendencia de {selected_category}"
    )
    bar_fig = px.bar(
        filtered_df, x="date", y="value", title=f"Barras de {selected_category}"
    )

    return line_fig, bar_fig


# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)
