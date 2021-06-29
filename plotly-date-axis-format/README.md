# Override the Default Behaviour for Plotly Date Axes

For Plotly time series charts, time appears in the date axis when the date range is small or when you zoom in. 

We discuss how to override this default behaviour in our [blog post](https://medium.com/zyphr-solutions/plotly-date-axis-formatting-dbf349ff7264) and provide sample code working through the mentioned fixes in [`app.py`](app.py).

## How to run this app locally

Clone the repository:

```bash
git clone https://github.com/zyphr-solutions/code-samples.git
```

Redirect to the respective app directory:

```bash
cd login-template/plotly-date-axis-format
```

It would be advisable to create a separate virtual environment running Python 3:

```bash
python -m virtualenv venv
```

Activate the environment by running:

* UNIX: 
    ```bash
    source venv/bin/activate
    ```

* Windows:
    ```bash
    venv\Scripts\activate
    ```

Install all required packages to this environment:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

View in your browser at http://127.0.0.1:8050.

## Resources

* [Dash documentation for Python](https://dash.plotly.com/)
* [Plotly documentation for Python](https://plotly.com/python/)
