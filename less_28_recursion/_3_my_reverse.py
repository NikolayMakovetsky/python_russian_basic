def my_reverse(value: str) -> str:
    if not value:
        return ""
    if len(value) == 1:
        return value
    else:
        return "".join(value[-1] + my_reverse(value[:-1]))

rev_short = lambda val: "" if not val else val if len(val) == 1 else "".join(val[-1] + rev_short(val[:-1]))

if __name__ == '__main__':
    assert my_reverse("") == ""
    assert my_reverse("h") == "h"
    assert my_reverse("ho") == "oh"
    assert my_reverse("how") == "woh"

    assert rev_short("") == ""
    assert rev_short("h") == "h"
    assert rev_short("ho") == "oh"
    assert rev_short("how") == "woh"