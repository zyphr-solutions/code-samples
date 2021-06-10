from datetime import timedelta

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


app = dash.Dash(__name__)


MAX_DAYS_WITH_DTICK_FORMAT = 99


def generate_df(days):
    min_date = pd.to_datetime("2020-01-01")
    df = pd.DataFrame(
        [
            {"date": str((min_date + timedelta(days=i)).date()), "count": i}
            for i in range(days)
        ]
    )
    df["date"] = pd.to_datetime(df["date"]).dt.date

    return df


def generate_bar(df, fix=False):
    fig = px.bar(df, x="date", y="count")

    if fix:
        # compute number of days in date range of date column
        max_date = pd.to_datetime(df["date"]).max()
        min_date = pd.to_datetime(df["date"]).min()
        num_days = (max_date - min_date).days

        # update x-axis format if number of days within specified limit
        if num_days < MAX_DAYS_WITH_DTICK_FORMAT:
            fig.update_xaxes(dtick=86400000.0, type="date")

    fig.update_xaxes(
        tickformatstops=[
            dict(dtickrange=[None, 86400000], value="%b %d"),
            dict(dtickrange=[86400000, "M1"], value="%b %d"),
            dict(dtickrange=["M1", "M12"], value="%b %Y"),
            dict(dtickrange=["M12", None], value="%Y"),
        ]
    )

    fig.update_layout(autosize=False, width=1000)

    return fig


app.layout = html.Div(
    [
        dcc.Graph(figure=generate_bar(df=generate_df(days=days), fix=fix))
        for days, fix in [
            (5, False), 
            (5, True),
            (100, False),
            (100, True)
        ]
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
