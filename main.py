from flask import Flask, request, jsonify
from auth import requires_auth
from functions import traverse
from functools import wraps
from datetime import datetime
from lxml import etree


import os
import json
import xml.etree.ElementTree as ET


# create the output directory if it doesn't already exist
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


app = Flask(__name__)


@app.route('/convert', methods=['POST'])
@requires_auth
def convert_json_to_xml():
    # Load the JSON input data from the request
    json_data = request.get_json()

    # Create the root element of the XML tree
    root = ET.Element('data')

    traverse(json_data, root)

    # Write the XML tree to a file with current date and time
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_file = 'output_{}.xml'.format(current_time)
    xml_data = ET.ElementTree(root)

    output_file = os.path.join(output_dir, output_file )
    xml_data.write(output_file)

    # Validate the XML output against the XSD schema
    xml_tree = etree.parse(output_file)

    # Return a JSON response indicating success
    response = {'success': True}
    return jsonify(response)




if __name__ == '__main__':
    app.run(debug=True)
