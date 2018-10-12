"""
Create a html document and it's components programatically 
with python.

Usage:
>> d = Document("This is an Html Page")
>> d.section()
>> d.div()
>> d.paragraph()
>> d.header()
>> d.table()
>> d.image()
>> d.url()
"""
__tag__ = "</>"
class Document:
    # Document Attributes
    _document = ""
    _header   = ""
    def __init__(self, header, theme='default'):
        _document = ""
        return

    def create_document(self):
        """
        Create the html document with the <head> and <body>
        including the supplied style classes
        """
        return

    def add_header(self):
        '''
        Creates the <header> tag for the document
        Meta Information is added.
        '''
        return

    def add_footer(self):
        '''
        Creates the <footer> tag for the document
        Meta Information and copyrights are included here.
        '''
        return

    def add_heading(self, level=1):
        '''
        Creating the <h1> tag by default. Parse the user supplied
        tag_level to create the tag.
        '''
        return

    def add_paragraph(self):
        '''
        Creates the <p> tag using the style classes.
        '''
        return 

    def add_img(self, src="."):
        '''
        Creates the <img> tag with the user defined source tag
        '''
        return

    def add_table(self):
        '''
        Creates the <table> block with the column headers
        and the column data info.
        '''

    def add_line(self):
        '''
        Creates the <ul> tag adding a horizontal rule to the document
        '''
        return

    def add_break(self):
        '''
        Creates the <br/> tag adding a ine break in the document
        '''
        return

    def add_url(self, text="", url=""):
        '''
        Creates a hyperlink from and adds to the document.
        '''
        return

    def add_html(self):
        '''
        Allows the user to add some custom html code to the document
        beyond the creativity of this library.
        '''
        return

if __name__=="__main__":
    exit
