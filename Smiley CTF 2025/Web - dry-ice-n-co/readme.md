### Web - dry-ice-n-co

This challenge is about wanting to buy the flag of a million dollars and only having 100 dollars. This kind of challenge immediately reminded me of integer overflow. However, in the end I couldn’t find the correct price and quantity to overflow.

**Vulnerabilities**

1. Typo of user.admin = true instead of user.admin = true —> this assigns you as admin instead of checking whether you are admin, allowing you to add whatever you want

```
if ((user.admin = true) && user != null && name != "flag") {
    availableProducts.add(new DryIceProduct(name, price, description));
}
```

2. Math.abs() fails to making Integer.MIN_VALUE positive as Integer.MAX_VALUE = 2,147,483,647 and hence the output of it is still negative

```python
public int getTotal() {
return Math.abs(price) * Math.abs(quantity);
}
```

**Steps to solve the challenge**

1. go to `/admin/add-product` and add a product using POST /admin/add-product?name=free2&price=-2147483648&description=hehe HTTP/2. The website will store the price is negative as Math.abs() fails to convert it to a positive number
2. buy it with the discount to overflow into a large positive number using `/add` and `/purchase`
3. buy flag

**Flag:**  .;,;.{this_is_not_a_political_statement_btw}