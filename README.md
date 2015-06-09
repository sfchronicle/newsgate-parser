# newsgate-parser
Take a .zip dump of content from [NewsGate](http://www.ccieurope.com/solutions/NewsGate/) and transform the contained XML data into JSON.

## Requirements
newsgate-parser was written on Mac OS X 10.10 Yosemite. It has not been tested on Linux (though I imagine it'll be fine). This software is for UNIX-based systems and thus is not tested nor supported for Windows.

- Python 2.7.x+
- [lxml](lxml.de)

## Installation
Provided you use [virtualenv](https://virtualenv.pypa.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):
```bash
$ mkvirtualenv newsgate-parser
$ git clone git@github.com:sfchronicle/newsgate-parser.git
$ cd newsgate-parser
$ pip install -r requirements.txt
```

## Usage
```bash
$ cd newsgate-parser
$ mkdir data  # if it doesn't already exist
$ mv /some/path/newsgate_story_dump.zip newsgate-parser/data
$ python parse.py
```
newsgate-parser uses the XML structure exported from NewsGate and does not support other CMSes at the moment. Create a `data` directory to house the .zip files. newsgate-parser will create `dump` and `build` directories where `dump` contains the raw XML file and `build` contains the transformed JSON file.

### JSON Strcture

Here's the resulting JSON structure:

```json
{
  "hed": "A fantastic headline from the XML dump",
  "byline": "By Jane Reporter",
  "subhed": "A possible online subhed or dek from the XML output",
  "article": [
    "The article attribute is an array.",
    "It contains each paragraph as a separate value.",
    "Hopefully you'll find this project to be helpful!"
  ]
}
```

### Project Structure
Here's an the project structure after transforming the XML data
```
newsgate-parser
├── README.md
├── build
│   └── B88222388Z.1_20150604170609_000.xml.json
├── data
│   └── B88222388Z.1_20150604170609_000_lgarchik.zip
├── dummy.xml
├── dump
│   ├── B88222388Z.1_20150604170609_000+GIB8UID0.1-0.jpg
│   └── B88222388Z.1_20150604170609_000.xml
├── lib
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── utils.py
│   └── utils.pyc
├── parse.py
└── requirements.txt
```

## Contributing

1. Fork it.
2. Create a branch (`git checkout -b username-patch-n`)
3. Commit your changes (`git commit -am "Added support for MovableType"`)
4. Push to the branch (`git push origin username-patch-n`)
5. Open a [Pull Request](http://github.com/github/markup/pulls)
6. Enjoy some [artisanal toast](https://www.eater.com/2014/5/30/6215971/artisanal-toast-is-taking-the-nation-by-storm)

## License
The MIT License (MIT)

Copyright The San Francisco Chronicle from '93 'til ...

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
