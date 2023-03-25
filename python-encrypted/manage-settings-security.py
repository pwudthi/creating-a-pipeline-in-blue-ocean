import argparse
import os.path
import subprocess
import xml.etree.ElementTree as ET

# Define command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    'id', help='the id of the server to update in the settings.xml file')
parser.add_argument(
    'username', help='the username to update in the settings.xml file')
parser.add_argument(
    'password', help='the password to encrypt and update in the settings.xml file')
parser.add_argument('--file', help='the location of the settings.xml file (default: ~/.m2/settings.xml)',
                    default=os.path.join(os.path.expanduser('~'), '.m2', 'settings.xml'))
parser.add_argument(
    '--format', help='format the XML output', action='store_true')
args = parser.parse_args()

# Encrypt the password
result = subprocess.run(
    ['mvn', '--encrypt-password', args.password], stdout=subprocess.PIPE)
encrypted_password = result.stdout.decode().strip()

# Load the settings.xml file, or create it if it doesn't exist
if os.path.isfile(args.file):
    tree = ET.parse(args.file)
    root = tree.getroot()
else:
    root = ET.Element('settings')
    tree = ET.ElementTree(root)

# Find or create the servers element
servers = root.find('servers')
if servers is None:
    servers = ET.SubElement(root, 'servers')

# Find or create the server element to update
server = servers.find(".//server[id='{}']".format(args.id))
if server is None:
    server = ET.SubElement(servers, 'server')
    id_element = ET.SubElement(server, 'id')
    id_element.text = args.id

# Update the username and password elements
username = server.find('username')
if username is None:
    username = ET.SubElement(server, 'username')
username.text = args.username

password = server.find('password')
if password is None:
    password = ET.SubElement(server, 'password')
password.text = encrypted_password

# Sort the server elements by id
servers[:] = sorted(servers, key=lambda server: server.find('id').text)

# Write the modified tree back to the file
xml_string = ET.tostring(root, encoding='utf-8',
                         xml_declaration=True, method='xml')
if args.format:
    root = ET.fromstring(xml_string)
    ET.indent(root)
    xml_string = ET.tostring(root, encoding='utf-8',
                             xml_declaration=True, method='xml')
with open(args.file, 'wb') as f:
    f.write(xml_string)
