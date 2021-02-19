#mkdir gen-python
cd src
protoc --python_out=../gen-python *
cd ..