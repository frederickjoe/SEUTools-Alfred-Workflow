import xml.dom.minidom

from xml.etree.ElementTree import Element, SubElement, tostring


class WorkflowXML(object):

    items = Element('items')

    def __init__(self):
        self.items = Element('items')

    def addItem(self, itemUid=u"", itemArg=u"", itemType=u"file",
                itemValid=u"yes", autocomplete=u"",
                title=u"", subtitle=u"", icon=u"", arg=u""):

        item = SubElement(self.items, 'item')

        # set the item attributes
        if itemUid != "":
            item.set("uid", itemUid)
        if itemArg != "":
            item.set("arg", itemArg)
        if itemType != "file":
            item.set("type", itemType)
        if itemValid != "yes":
            item.set("valid", itemValid)
        if autocomplete != "":
            item.set("autocomplete", autocomplete)

        # set item childs
        if title != "":
            _title = SubElement(item, 'title')
            _title.text = title
        if subtitle != "":
            _subtitle = SubElement(item, 'subtitle')
            _subtitle.text = subtitle
        if icon != "":
            _icon = SubElement(item, 'icon')
            _icon.text = icon
        if arg != "":
            _arg = SubElement(item, 'arg')
            _arg.text = arg

    def toPrettyString(self):
        s = tostring(self.items, 'utf-8')
        reparsedXml = xml.dom.minidom.parseString(s)
        prettyXmlString = reparsedXml.toprettyxml(indent='  ')
        return prettyXmlString

    def toString(self):
        s = tostring(self.items, 'utf-8')
        reparsedXml = xml.dom.minidom.parseString(s)
        xmlString = reparsedXml.toxml()
        return xmlString
