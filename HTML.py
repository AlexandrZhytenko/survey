
def bold_decorator(f):
    def decorate(*parameters):
        parameters = list(parameters)
        parameters[1] = '<b>' + parameters[1] + '</b>'
        result = f(*parameters)
        return result
    return decorate

def list_item_decorator(f):
    def decorate(*parameters):
        parameters = list(parameters)
        parameters[1] = '<li>' + parameters[1] + '</li>'
        result = f(*parameters)
        return result
    return decorate

def italic_decorator(f):
    def decorate(*parameters):
        parameters = list(parameters)
        parameters[1] = '<i>' + parameters[1] + '</i>'
        result = f(*parameters)
        return result
    return decorate

@bold_decorator
@list_item_decorator
def write_name(webpage_file, name):
    webpage_file.write(name)

@italic_decorator
@list_item_decorator
def write_surname(webpage_file, surname):
    webpage_file.write(surname)

def add_button(webpage_file, button_name):
    webpage_file.write()


def create_webpage():
    people = [
        {
            'name': 'Olexandr',
            'surname': 'Zhytenko'
        },
        {
            'name': 'Bob',
            'surname': 'Sky'
        }
    ]

    with open('index.html', 'w') as webpage:
        for person in people:
            webpage.write('<ul>')
            write_name(webpage, person['name'])
            write_surname(webpage, person['surname'])
            webpage.write('</ul>')

#конструкція використовуєть щоб виконати саме той код в цьому файлі
if __name__ == '__main__':
    create_webpage()