"""Exercise: use one function with two report formats."""


class TextReport:
    def display(self, message):
        # TODO: print "TEXT: <message>"
        pass


class HTMLReport:
    def display(self, message):
        # TODO: print "<p><message></p>"
        pass


def show_report(report, message):
    # TODO: call the matching object's display method
    pass


text_report = TextReport()
html_report = HTMLReport()

show_report(text_report, "Daily summary")
show_report(html_report, "Daily summary")
