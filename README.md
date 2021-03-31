# Login Template

This template is comprised of a Dash application protected by user-based authentication, using Python Flask. 

## How to run this template locally

Clone the repository:

```bash
git clone https://github.com/zyphr-solutions/login-template-public.git
```

Relocate to the repo:

```bash
cd login-template-public
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

Initialize an encrypted dictionary of users by running:

```bash
python init_data.py
```

This script will get an unencrypted dictionary of users from [users_unencrypted.py](data/users_unencrypted.py), encrypt the passwords in this dictionary, and overwrite [users.py](data/users.py) to contain this newly encrypted dictionary. 

While this is only an example, in practice, it would be advisable to then remove [users_unencrypted.py](data/users_unencrypted.py):

```bash
rm data/users_unencrypted.py
```

Run the app:

```bash
python index.py
```

View in your browser at http://127.0.0.1:8050.

## Resources

* [Dash documentation](https://dash.plotly.com/)
* [Plotly documentation](https://plotly.com/python/)
* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-Login documentation](https://flask-login.readthedocs.io/en/latest/)
