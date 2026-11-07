import os
SRC='/home/user/mathlockin/src/hi'
def page_path(book):
    if book<=93: return f'{SRC}/a-{book+6:02d}.png'
    return f'{SRC}/b-{book-93:02d}.png'
