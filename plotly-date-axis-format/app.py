from datetime import timedelta
import random

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


app = dash.Dash(__name__)


MAX_DAYS_WITH_DTICK_FORMAT = 99


def generate_df(days):
    random.seed(days)
    min_date = pd.to_datetime("2020-01-01")
    df = pd.DataFrame(
        [
            {
                "date": str((min_date + timedelta(days=i)).date()), 
                "count": random.randint(0, 100),
            }
            for i in range(days)
        ]
    )
    df["date"] = pd.to_datetime(df["date"]).dt.date

    return df


def generate_bar(df, fix=None):
    fig = px.line(df, x="date", y="count")

    if fix == 0:
        fig.update_xaxes(fixedrange=True)

    if fix == 1.1:
        fig.update_xaxes(tickformat="%b %d\n%Y")

    if fix == 1.2:
        fig.update_xaxes(
            tickformatstops=[
                dict(dtickrange=[None, 86400000], value="%b %d\n%Y"),
            ]
        )

    if fix == 2:
        fig.update_xaxes(dtick=86400000)

    if fix == 3:
        # compute number of days in date range of date column
        max_date = pd.to_datetime(df["date"]).max()
        min_date = pd.to_datetime(df["date"]).min()
        num_days = (max_date - min_date).days

        # update x-axis format if number of days within specified limit
        if num_days < MAX_DAYS_WITH_DTICK_FORMAT:
            fig.update_xaxes(dtick=86400000.0)

        fig.update_xaxes(
            tickformatstops=[
                dict(dtickrange=[None, 86400000], value="%b %d\n%Y"),
            ]
        )

    # fig.update_layout(autosize=False, width=1000)

    return fig


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H3(f"days = {days}, fix = {fix}"),
                        dcc.Graph(figure=generate_bar(df=generate_df(days=days), fix=fix))
                    ],
                    style={"width": "49%", "display": "inline-block"}
                )
                for days in [3, 100]
            ],
            # style={"border-bottom": "2px black solid"}
        )
        for fix in [None, 1.1, 1.2, 2, 3]
    ] 
)

if __name__ == "__main__":
    app.run_server(debug=True)
