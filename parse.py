def parse(query: str) -> dict:
    try:
        x = query.split('?')[1].lstrip()
        if x is None:
            return {}
        elif x is not True:
            some_dict = {}
            new_str = x.split('&')
            for i in new_str:
                if '=' in i:
                    k, v = i.split('=')
                    some_dict.update({k: v})
            return some_dict
        else:
            return {}
    except IndexError:
        return {}


print(parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'})
print(parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'})
print(parse('https://example.com/path/to/page?&&&&&&&&&&&&&&&') == {})
print(parse('http://example.com/') == {})
print(parse('http://example.com/name') == {})
print(parse('http://example.com/?') == {})
print(parse('http://example.com/?name=Dima') == {'name': 'Dima'})
print(parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'})
print(parse('https://example.com/path/to/page?name=ferret&color=purple&age=2') ==
      {'name': 'ferret', 'color': 'purple', 'age': '2'})
print(parse('http://exam') == {})
print(parse('http://example.com/?') == {})
print(parse('http://example.com/?name&dfgdfg') == {})
print(parse('http://example.com/?name=Dima') == {'name': 'Dima'})
