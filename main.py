from pathlib import Path
import shutil
import re


# xxx: エラーハンドリを実装しないと意味がない関数
def is_dir(dir_name: str) -> [Path, bool]:
  path: Path = Path(dir_name)
  return [path, path.exists()]


def pull_out_docs(dir_name: str, pick_docs: list):
  path: Path
  dir_is: bool
  path, dir_is = is_dir(dir_name)
  if not dir_is:
    path.mkdir()
  for doc in pick_docs:
    shutil.copy2(doc, path)


def get_iVim_docs(dir_name: str, search_str: str) -> list:
  path: Path
  dir_is: bool
  path, dir_is = is_dir(dir_name)
  if not dir_is:
    return []
  glob_iter: iter = path.glob('*.*')
  iVim_docs: list = [doc for doc in glob_iter if re.search(search_str, str(doc))]
  return iVim_docs


def picup_docs(dir_name: str):
  path: Path
  dir_is: bool
  path, dir_is = is_dir(dir_name)
  glob_iter: iter = path.glob('*.*')
  docs: list = sorted(list(glob_iter))
  for doc in docs:
    print(doc.name)


if __name__ == '__main__':
  master_dir_name: str = './iVimDocsMaster'
  pull_dir_name: str = './pullDocs'
  match: str = 'ios|ivim'

  # picup_docs(master_dir_name)
  docs: list = get_iVim_docs(master_dir_name, match)
  pull_out_docs(pull_dir_name, docs)
