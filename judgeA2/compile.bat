@echo off
copy .\source\HuffmanDecompression.java .\
copy .\source\HuffmanCompression.java .\
javac HuffmanDecompression.java
javac HuffmanCompression.java
g++ min_check.cpp -o lengthcheck