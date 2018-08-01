# Fcoin 
Quantitative Trading

## Question

1. https://github.com/ContinuumIO/anaconda-issues/issues/6678

## Fcoin SDK BUG

```
python3.6/site-packages/fcoin/dataapi.py

def get_signed(self, sig_str):
        sig_str = base64.b64encode(sig_str.encode("utf8"))
        signature = base64.b64encode(hmac.new(self.secret.encode("utf8"), sig_str, digestmod=hashlib.sha1).digest())
        return signature
```

## Trading Strategy

```
SELECT f.name AS symbol, a.name, a.price, a.amount, a.total
	, a.interval, a.enable, b.code AS rule, c.code AS side, d.username
FROM app_tradingstrategy a, app_orderrule b, app_orderside c, auth_user d, app_symbol f
WHERE (a.order_rule_id = b.id
	AND a.order_side_id = c.id
	AND a.username_id = d.id
	AND a.symbol_id = f.id);
```
