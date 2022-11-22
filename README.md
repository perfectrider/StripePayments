First toching to STRIPE library, and first working .redirecttoCheckout and .checkout.session.create methods.

Project in development...

---

To launch the project, for Linux OS:

1. Create virtual enviroment:
python -m venv djangoenv

2. To activate the virtual environment with the command:
source djangoenv/bin/activate

3. The next step to install the dependencies from the requirements.txt file. To do this, you need to run the command:
pip install -r StripeApp/requirements.txt

4. Install al migrations:
python3 StripeApp/manage.py migrate

5. To run the local server and test the project, you need run command:
python3 StripeApp/manage.py runserver

6. Check it on 
127.0.0.1:8000/landing
