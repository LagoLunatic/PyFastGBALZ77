
### About

This is a Python 3 module for LZ77 compressing data for the GBA.  
It is written in C so the performance is much better than native Python code.  
e.g. For 0x8000 bytes of raw GBA GFX data I tested this on, this module can compress it in 0.06 seconds, while the equivalent native Python code takes 9.97 seconds.  

Currently only supports compression because decompression isn't slow even with native Python code.  

### Installation

`python setup.py install`

### Usage

Call `pyfastgbalz77.compress` with a bytes object containing the data you wish to compress.  
It will return the compressed data as a new bytes object.  
The second argument should be a boolean for whether the compressed data should be made compatible with the GBA's 16-bit LZ77 decompression function. If False, only the 8-bit decompression function will be able to decompress this data, but the size will be slightly smaller.  

Example:
```py
import pyfastgbalz77

with open("some_uncompressed_file.bin", "rb") as f:
  uncompressed_bytes = f.read()

compressed_bytes = pyfastgbalz77.compress(uncompressed_bytes, True)

with open("some_compressed_file.bin", "wb") as f:
  f.write(compressed_bytes)
```
