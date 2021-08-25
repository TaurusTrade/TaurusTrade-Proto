:: need protoc-gen-doc
protoc -Isrc --doc_opt=html,index.html --doc_out=./docs src/*.proto