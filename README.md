# Fast Trees
> Cute little python module that sits atop the tree-sitter library to provide an easier to use and cleaner interface for interacting with source code


## Install

`fast-trees` requires git to be installed on your system for downloading the different `tree-sitter` languages. So, make sure it is installed before using `fast-trees`. See [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for instruction on installing git.

To install `fast-trees`, simply run:

`pip install fast-trees`

## How to use

Easily work with source code data by using the high level API. Here's how you can grab the parameters of a java method:

```python
mthd = """public static void main(String[] args, Object clazz) {
    // This is a test
    System.out.println(args[0]);
    /**
        This is another test!
    */
}
"""
parser = FastParser("java")
print(parser.get_method_parameters(mthd))
```

    Downloading repo https://github.com/tree-sitter/tree-sitter-java to /home/nathan/projects/other/fast_trees/fast_trees/tree-sitter-java.
    ['args', 'clazz']


And here is how you can grab all of the inline comments:

```python
inline_comments = parser.get_method_inline_comments(mthd)
for c in inline_comments:
    print(c)
```

    // This is a test
    /**
            This is another test!
        */


# Supported Languages
- [x] Java

# TODO

- [x] Add ability to grab method parameters
- [ ] Add separation between parsing methods vs classes
- [ ] Add ability to get all methods in a class
- [ ] add ability to get all instance variables in a class
- [ ] Add more languages
