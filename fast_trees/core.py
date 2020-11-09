# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['FastParser']

# Cell
import fast_trees

from git import Repo
from pathlib import Path
from tree_sitter import Language, Parser
from typing import List

# Cell
class FastParser:
    LANG_URLs = {'java': ['https://github.com/tree-sitter/tree-sitter-java', 'tree-sitter-java']}

    def __init__(self, lang: str):
        self.build_parser(lang)

    def get_params(self, mthd: str) -> List[int]:
        '''
        Returns the parameters of a given method

        :param mthd: the method to get the parameters from
        :returns: the parameters of the given method as an array
        '''
        tree = self.parser.parse(bytes(mthd, 'utf8'))
        query = self.language.query("""
            (formal_parameter
            name: (identifier) @function.method)
        """)
        captures = query.captures(tree.root_node)
        params = []
        for node, _ in captures:
            params.append(mthd[node.start_point[1]:node.end_point[1]])

        return params

    def build_parser(self, lang: str):
        url, folder = FastParser.LANG_URLs[lang]
        repo_dir = Path(fast_trees.__path__[0] + '/' + folder)
        if repo_dir.exists():
            print('Repo already exists, continuing.')
        else:
            print(f'Downloading repo {url} to {repo_dir}.')
            Repo.clone_from(url, repo_dir)

        build_dir = fast_trees.__path__[0] + '/' + 'build/my-languages.so'
        Language.build_library(
            # Store the library in the `build` directory
            build_dir,

            # Include one or more languages
            [
                repo_dir
            ]
        )
        self.language = Language(build_dir, lang)
        self.parser = Parser()
        self.parser.set_language(self.language)