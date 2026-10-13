from pywebio.input import *
from pywebio.output import *

put_html("<h1>Currency Converter</h1>")

choose = radio("Choose the conversion type:", options=["Euros to GBP", "GBP to Euros"])

if choose == "Euros to GBP":
    euros_to_convert = input("Enter amount in Euros you want to convert:")
    gbp = float(euros_to_convert) * 0.8
    put_text(f"{euros_to_convert} Euros is equal to {gbp:.2f} GBP.")
else:
    gbp_to_convert = input("Enter amount in GBP you want to convert:")
    eur = float(gbp_to_convert) / 0.8
    put_text(f"{gbp_to_convert} GBP is equal to {eur:.2f} Euros.")




