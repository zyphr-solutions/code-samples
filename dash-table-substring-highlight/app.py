import dash
import dash_table
import dash_html_components as html
import pandas as pd


app = dash.Dash(__name__)


def generate_df():
    df = pd.DataFrame(
        {
            "date": ["2020-01-01", "2020-01-02", "2020-01-03"],
            "sentence": [
                "The dog.\nThe cat.\nThe mouse.",
                "The dog.\nA cat.\nA mouse.",
                "A dog.\nA cat.\nThe mouse.",
                # "There was no telling what thoughts would come from the machine.",
                # "The paintbrush was angry at the color the artist chose to use.",
                # "There is no better feeling than staring at a wall with closed eyes.",
            ],
        }
    )
    return df


def generate_table(df, highlight_colname=None, highlight_phrase=None):

    def highlight_lines(text):
        text = text.split("\n")
        new_text = []
        for line in text:
            if highlight_phrase in line:
                line = f"**{line}**"
            new_text.append(line)
        new_text = "\n".join(new_text)
        return new_text

    if highlight_phrase:
        df[highlight_colname] = df[highlight_colname].apply(lambda text: highlight_lines(text))

    columns=[
        {"name": column, "id": column, "presentation": "markdown"}
        if highlight_colname == column else
        {"name": column, "id": column}
        for column in df.columns
    ]

    table = dash_table.DataTable(
        columns=columns,
        data=df.to_dict("records"),
    )
    return table


app.layout = html.Div(
    generate_table(
        df=generate_df(), highlight_colname="sentence", highlight_phrase="The"
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)
