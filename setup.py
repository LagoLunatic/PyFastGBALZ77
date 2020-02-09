from distutils.core import setup, Extension

module1 = Extension('pyfastgbalz77',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '1')],
                    include_dirs = [],
                    libraries = [],
                    library_dirs = [],
                    sources = ['pyfastgbalz77.c'])

setup (name = 'Python Fast GBA LZ77 Compression',
       version = '1.1',
       description = 'GBA LZ77 compression written in C.',
       author = 'LagoLunatic',
       author_email = '',
       url = 'https://github.com/LagoLunatic',
       long_description = '''
Python module written in C for LZ77 compressing data for the GBA with better performance than native Python code.
''',
       ext_modules = [module1])
