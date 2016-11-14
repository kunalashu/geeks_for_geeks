#############################################
# Script to seperate xml to different xml file based on the tag provided.
#
#############################################

import os
import xml.etree.ElementTree as ElementTree
import sys


def main(inp_file,tag_name):
    out_file=open(str(tag_name)+'.xml','w')
    with open(inp_file) as f:
        et = ElementTree.parse(f)
        for article in et.findall(str(tag_name)):
            xml_string = ElementTree.tostring(article)
            out_file.write(xml_string)
    print 'All records updated'
    out_file.close
            # Take care to name the files sequentially


if __name__=='__main__':
    inp_file=str(sys.argv[1])
    tag_name=str(sys.argv[2])
    print inp_file
    print tag_name
    main(inp_file,tag_name)
