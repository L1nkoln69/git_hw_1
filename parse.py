def parse(query: str) -> dict:
    try:
        x = query.split('?', 1)[1].lstrip()
        if x is None:
            return {}
        elif x is not True:
            some_dict = {}
            new_str = x.split('&')
            for i in new_str:
                some_str = i.split('=')
                if len(some_str) > 1:
                    some_dict333333333[f'{some_str[0]}'] = f'{some_str[1]}'
                else:
                    pass
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
