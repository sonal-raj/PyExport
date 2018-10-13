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
    _title   = ""
    def __init__(self, title, theme='default'):
        _document = self.create_document(title=title)
        return

    def create_document(self, title=""):
        """
        Create the html document with the <head> and <body>
        including the supplied style classes
        """
        self._title = title
        self._document = "<html>\
                            <head>\
                            <title>%s<\title>\
                            </head>\
                            <body>\
                            </body>\
                          <html>" % self._title   

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

    def add_section(self):
        '''
        Creates the <section> tags for grouping content together.
        '''
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
        from BeautifulSoup import BeautifulSoup as bs
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
        doc_above, doc_before = self._document.split(split_tag)
        self._document = "%s%s%s%s" % (doc_above, content, split_tag, doc_before)

    def export(format="html"):
        '''
        Export the created document into a user specified format
        '''
        return

if __name__=="__main__":
    exit
