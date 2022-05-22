
# Return a function from another function
print("--Return a function from another function--")
def html_tag(tag):

    def wrap_text(message):
        print(f'<{tag}>{message}<{tag}>')

    return wrap_text


text_h1=html_tag('h1')

text_h1('Hello')
#text_h1('Hi')

'''
text_p=html_tag('p')

text_p('Hello')
text_p('Hi')

'''
