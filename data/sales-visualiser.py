import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Read the formatted output CSV
formatted_df = pd.read_csv('formatted_output.csv')

# Create a Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer"),

    dcc.Graph(id='sales-chart'),
])


# Callback to update the chart based on user input
@app.callback(
    Output('sales-chart', 'figure'),
    Input('sales-chart', 'relayoutData')
)
def update_chart(relayout_data):
    # Filter data based on date range selection
    if 'xaxis.range' in relayout_data:
        x_range = relayout_data['xaxis.range']
        filtered_df = formatted_df[(formatted_df['date'] >= x_range[0]) & (formatted_df['date'] <= x_range[1])]
    else:
        filtered_df = formatted_df

    # Create line chart
    fig = px.line(filtered_df, x='date', y='sales', labels={'sales': 'Sales Amount', 'date': 'Date'})

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
