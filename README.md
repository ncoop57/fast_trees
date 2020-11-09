# Fast Trees
> Cute little python module that sits atop the tree-sitter library to provide an easier to use and cleaner interface for interacting with source code


## Install

`pip install fast-trees`

## How to use

Easily work with source code data by using the high level API. Here's how you can grab the parameters of a java method:

```
mthd = """public static void main(String[] args, Object clazz) {
    System.out.println(args[0]);
}
"""
parser = FastParser('java')
parser.get_params(mthd)
```




    2



# Supported Languages
- [x] Java

# TODO

- [x] Add ability to grab method parameters
- [ ] Add separation between parsing methods vs classes
- [ ] Add ability to get all methods in a class
- [ ] add ability to get all instance variables in a class
- [ ] Add more languages
