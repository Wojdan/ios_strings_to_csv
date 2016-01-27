# Copyright 2016 Bartłomiej Wojdan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import csv

strings = 'filename.strings' #file containing translation
fieldnames = ['value','translation','comment','name']

def parse(filename):
	with open(filename, 'r') as strings_file:
		contents = strings_file.read()
		translations = re.findall('/\* .*\ \*/\n.*;', contents)
		for translation in translations:
		
			item = {}
		
			comment_match = re.search('[/][*][ ].*[ ][*][/]', translation)
			comment = comment_match.group(0)
			item.update({'comment' : comment[3:len(comment)-3]})
		
			name_match = re.search('["](.*)["].*["](.*)["]', translation)
			name = name_match.group(1)
			item.update({'name' : name})

			value_match = re.search('["](.*)["].*["](.*)["]', translation)
			value = value_match.group(2)
			item.update({'value' : value})
			
			print '%s' % comment[3:len(comment)-3]
			print '%s' % name
			print '%s\n' % value

			yield item

f = open('outputs/ios_strings.csv', 'w+')
try:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in parse(strings):
        writer.writerow(i)
finally:
    f.close()
