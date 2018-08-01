# fcoin 
null

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
