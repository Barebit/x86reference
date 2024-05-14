# just a quick validator

import xmlschema   # pip install xmlschema

XML_FILE = 'x86reference.xml'
XSD_FILE = 'x86reference.xsd'

schema = xmlschema.XMLSchema(XSD_FILE)

try:
    schema.validate(XML_FILE)
    print(f"{XML_FILE} validates against {XSD_FILE}")
except xmlschema.XMLSchemaValidationError as e:
    print(f"{XML_FILE} failed to validate against {XSD_FILE}")
    print(f"error: {e}")
    print(f"element: {e.elem}")
    print(f"path: {e.path}")
except Exception as e:
    print(f"an unexpected error occurred during validation of {XML_FILE}")
    print(f"error: {e}")
