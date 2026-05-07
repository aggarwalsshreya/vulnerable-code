from lxml import etree


def parse_invoice(xml_text):
    parser = etree.XMLParser(resolve_entities=True, load_dtd=True, no_network=False)
    return etree.fromstring(xml_text.encode(), parser=parser)  # CWE-611
