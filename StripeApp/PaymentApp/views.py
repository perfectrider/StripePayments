from StripeApp import settings
from django.views import View
from django.views.generic import TemplateView
import json
import os
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')


class ItemLandingPageView(TemplateView):
    template_name = 'landing.html'

    # class CreateCheckoutSessionView(View):


def calculate_order_amount(items):
    # Replace this constant with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    return 1400


@app.route('/create-payment-intent', methods=['POST'])
def create_payment(self):
    try:
        data = json.loads(request.data)
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=self.calculate_order_amount(data['items']),
            currency='usd',
            automatic_payment_methods={
                'enabled': True,
            },
        )
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403


if __name__ == '__main__':
    app.run(port=4242)
