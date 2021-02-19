#mkdir gen-python
cd src

protoc --csharp_out=../gen-csharp *

cd ..