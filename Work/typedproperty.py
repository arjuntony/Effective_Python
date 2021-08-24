def typedproperty(attr_name, expected_type):
    private_name = '_' + attr_name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop


String = lambda attrname: typedproperty(attrname, str)
Integer = lambda attrname: typedproperty(attrname, int)
Float = lambda attrname: typedproperty(attrname, float)
