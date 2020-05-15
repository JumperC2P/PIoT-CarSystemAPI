

class ParserUtils:
    """ParserUtils is a parser"""

    #https://www.programcreek.com/python/example/86195/flask.request.content_type
    def parse_qs_plus(self, _dict):
        """ parse_qs_plus is used to transform ResultProxy objects to Dictionary objects.

        :param: _dict(ResultProxy objects): ResultProxy

        :return: Dictionary objects transformed from the input

        """
        data = {}
        if(type(_dict) != dict):
            return _dict
        for k,v in _dict.items():
            if (type(v) == list):
                if (len(v) == 0):
                    data[k] = []
                elif (len(v) == 1):
                    data[k] = v[0]
                else:
                    _list = []
                    for item in v:
                        _list.append(self.parse_qs_plus(item))
                    data[k] = _list
            else:
                data[k] = v
        return data