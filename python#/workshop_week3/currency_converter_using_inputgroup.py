from pywebio.input import *
from pywebio.output import *

put_html("<h1>Currency Converter</h1>")

user_input = input_group("GBP <> euros", [
    input("Enter amount in GBP you want to convert:", name="currency_value"),
    actions("", ["Convert to gbp", "Convert to Euros"], name="conversion")
]
)

if user_input["conversion"] == "Convert to gbp":
    euros_to_convert = user_input["currency_value"]
    gbp = float(euros_to_convert) * 0.8
    put_text(f"{euros_to_convert} Euros is equal to {gbp:.2f} GBP.")
else:
    gbp_to_convert = user_input["currency_value"]
    eur = float(gbp_to_convert) / 0.8
    put_text(f"{gbp_to_convert} GBP is equal to {eur:.2f} Euros.")


