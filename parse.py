import os
import io
import json
import zipfile

import xmltodict
from lxml import etree
from lib.utils import all_files, unzip
from ipdb import set_trace as debugger

DATA_DIR = os.path.join(os.getcwd(), 'data')
DUMP_DIR = os.path.join(os.getcwd(), 'dump')
BUILD_DIR = os.path.join(os.getcwd(), 'build')

def _save_json(filename, json_data):
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    with open(os.path.join(BUILD_DIR, filename), 'wb') as jf:
        jf.write(json_data)

def _remove_namespaces(root_element):
    """
    Take a raw xml object from lxml and use XSLT to remove namespaces

    """
    # http://wiki.tei-c.org/index.php/Remove-Namespaces.xsl
    xslt='''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="no"/>

    <xsl:template match="/|comment()|processing-instruction()">
        <xsl:copy>
          <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="*">
        <xsl:element name="{local-name()}">
          <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="@*">
        <xsl:attribute name="{local-name()}">
          <xsl:value-of select="."/>
        </xsl:attribute>
    </xsl:template>
    </xsl:stylesheet>
    '''

    xslt_doc = etree.parse(io.BytesIO(xslt))
    transform = etree.XSLT(xslt_doc)

    return transform(root_element)

def unzip_data():
    """
    Unzip newsgate zip export and exact data to DUMP_DIR
    """
    if not os.path.exists(DUMP_DIR):
        os.makedirs(DUMP_DIR)

    zipfiles = list(all_files(DATA_DIR, '*.zip'))

    for zf in zipfiles:
        if not os.path.isfile(zf):
            unzip(zf, DUMP_DIR)

def transform_xml_to_json():
    """
    Take xml output and trasform to json
    """
    xml_files = list(all_files(DUMP_DIR, '*.xml'))

    for xf in xml_files:
        with open(xf, 'rb') as xmlfile:
            raw_xml = xmlfile.read()
            root = etree.fromstring(raw_xml)
            dom = _remove_namespaces(root)

            # dom.xpath('//ccitext/*/*/text()')  # Almost

            content = xmltodict.parse(raw_xml, process_namespaces=True)
            output_json = json.dumps(content)
            filename = "{}.json".format(os.path.split(xmlfile.name)[1])

            _save_json(filename, output_json)

if __name__ == '__main__':
    unzip_data()
    transform_xml_to_json()
