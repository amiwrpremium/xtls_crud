# Welcome to XTLS_CRUD's documentation!

## Installation

### Install from PyPI
    pip install xtls_crud

### Install from source (build using poetry)
    git clone
    cd xtls_crud
    poetry build
    pip install dist/xtls_crud-<version>-py3-none-any.whl

### Install from GitHub
    pip install git+hhttps://github.com/amiwrprez/xtls_crud.git


## Usage
You can use this package as library or you can run local web server with to use API for CRUD operations.  
  
See examples below.

### Web
You can run local web server with to use API for CRUD operations.

#### Run web server
    xtls_crud web serve

#### Run web server with custom parameters
    xtls_crud web serve --host=0.0.0.0 --port=8080

#### Swagger UI
To see API docs, go to: `/docs`

#### ReDoc
To see API docs, go to: `/redoc`

### Use as library
You can use this package as library.  
See examples below.


## Examples

See [examples](examples.md) for examples.