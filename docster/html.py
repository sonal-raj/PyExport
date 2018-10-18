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
import os
import pdfkit
from xhtml2pdf import pisa
import pypandoc as pdoc
from BeautifulSoup import BeautifulSoup as bs

__tag__ = "</>"
class Document:
    # Document Attributes
    _document = ""
    _title   = ""
    _theme   = ""
    def __init__(self, title, theme='default'):
        self.create_report(title=title)
        print self._document
        self._title = title
        self._theme = theme
        return

    #********************************
    # Exposed APIs for the end_user #
    #********************************
    def create_report(self, title=""):
        """
        Create the html document with the <head> and <body>
        including the supplied style classes

        @param title:
            The document title to use for page header 
            and document header.
        """
        self._title = title
        self._document = "<html>\
                            <head>\
                            <title>%s</title>\
                            </head>\
                            <body>\
                            </body>\
                          <html>" % self._title   

    #************************************************
    # Private wrappers for internal or external use #
    #************************************************
    def add_header(self):
        '''
        Creates the <header> tag for the document
        Meta Information is added.
        '''
        # Ensure single header
        return

    def add_footer(self):
        '''
        Creates the <footer> tag for the document
        Meta Information and copyrights are included here.
        '''
        # Ensure single footer 
        return

    def add_heading(self, text, level=1):
        '''
        Creating the <h1> tag by default. Parse the user supplied
        tag_level to create the tag.
        '''
        content = "<h%s class='h%s'>%s</h%s>" % (level, level, text, level)
        self._append(content)

    def add_paragraph(self, text):
        '''
        Creates the <p> tag using the style classes.
        '''
        content = "<p class='paragraph'>\
                     %s\
                   </p>" % text
        self._append(content)

    def add_img(self, src="."):
        '''
        Creates the <img> tag with the user defined source tag
        '''
        content = "<img src=%s class='img'/>"
        self._append(content)

    def add_table_numpy(self, table_data, no_header=False):
        '''
        Creates the <table> block with the column headers
        and the column data info.
        '''
        content = "<table class='table'>"
        if not no_header:
            header_row = table_data[0]
            table_data = table_data[1:]
            content += "<tr class='table-row'>"
            for entry in header_row:
                content += "<th class='table-header'>{}</th>".format(str(entry))
            content += "</tr>"
        
        for row in table_data:
            content += "<tr class='table-row'>"
            for entry in row:
                content += "<td>{}</td>".format(str(entry))
            content += "</tr>"
        
        content += "</table>"
        self._append(content)

    def add_list(self, list_items_array, numbered=False):
        '''
        Creates a formatted list of items from a given 
        array of inputs
        '''
        list_tag = "ol" if numbered==True else "ul"
        item_string = ""
        for item in list_items_array:
            item_string = item_string + "<li>{}</li>".format(str(item))
        content = "<%s class='list'>\
                        %s\
                   </%s>" % (list_tag, item_string, list_tag)
        self._append(content)

    def add_line(self):
        '''
        Creates the <hr> tag adding a horizontal rule to the document
        '''
        content = "<hr/>"
        self._append(content)

    def add_break(self):
        '''
        Creates the <br/> tag adding a ine break in the document
        '''
        content = "<br/>"
        self._append(content)

    def add_url(self, text="", url=""):
        '''
        Creates a hyperlink from and adds to the document.
        '''
        content = "<a href=%s class='link'>%s</a>"
        self._append(content)

    def add_html(self, content):
        '''
        Allows the user to add some custom html code to the document
        beyond the creativity of this library.
        '''
        self._append(content)

    def show(self):
        '''
        Displays the document contents
        '''
        return self._document

    def pretty_print(self):
        '''
        Formats into appropriate html form and displays
        '''
        soup = bs(self._document)
        prettyHTML = soup.prettify()
        return prettyHTML

    def _append(self, content, append=True, insertAtTop=False, split_tag=""):
        '''
        Smart parser for parsing an html text block and inserting
        a block in the document 
        '''
        if split_tag == "":
            split_tag = "</body>"
        if insertAtTop:
            split_tag = "<body>"
        doc_above, doc_below = self._document.split(split_tag)
        self._document = "%s%s%s%s" % (doc_above, content, split_tag, doc_below)

    def export(self, format="html", path=".", name="default"):
        '''
        Export the created document into a user specified format
        Supported formats - html, pdf, email, doc
        '''
        html_doc = self.get_page()
        soup = bs(self._document)
        prettyHTML = soup.prettify()
        # Export to html
        if format=='html':
            file_name = os.path.join(path, "%s.html" % name)
            f = open(file_name, 'w+')
            f.write(html_doc)
            f.close()
            print("%s successfully saved!" % file_name)
        # Export to pdf
        elif format=='pdf':
            pdf_path = os.path.join(path, "%s.pdf" % name)
            file_handle = open(pdf_path, 'w+b')
            pisaStatus = pisa.CreatePDF(
                                    prettyHTML,                
                                    dest=file_handle
                                    )
            file_handle.close()      
        # elif format=='doc' or format=='docx':\
        #     doc_path = os.path.join(path, "%s.docx" % name)
        #     output = pdoc.convert(prettyHTML, 'docx', format='html', outputfile=doc_path, extra_args=['-RTS'])

    def get_page(self):
        '''
        Extract the html and embedded style selected into a single 
        docstring.
        '''
        # Load the css file
        stylesheet = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../themes/styles/{}.css'.format(self._theme))
        with open(stylesheet, 'r') as myfile:
            style = myfile.read()

        doc_style = "<style>%s</style>" % style
        doc_above, doc_below = self._document.split("</head>")
        consolidated_doc = "%s%s</head>%s" % (doc_above, doc_style, doc_below)
        return consolidated_doc

if __name__=="__main__":
    exit
