from convert_currency import ConvertCurrency

api_key = "fc3fabf54808552803af"
conv_curr = ConvertCurrency(api_key)
##conv_curr.show_currencies()
print(conv_curr.transform_currency("BRL", 33, "USD"))