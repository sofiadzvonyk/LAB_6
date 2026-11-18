clothes1 = {
    "jacket": 2200.56,
    "boots": 1179.99,
    "trousers": 843.38,
    "shirt": 650.50,
    "jeans": 950.00
}
clothes2 = {
    "jacket": 2100.00,
    "boots": 1300.00,
    "dress": 1500.00,
    "trousers": 900.00,
    "hat": 300.00
}
for key, value in clothes1.items():
    if key in clothes2:
        print((key, value))