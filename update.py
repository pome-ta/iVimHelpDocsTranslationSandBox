from pathlib import Path
import shutil
import sys

vimruntime_txt = Path('./.path').read_text().strip()
doc_path = Path(vimruntime_txt, 'doc')
from_path = Path('./iVimDocsMaster')

for f in doc_path.iterdir():
  f_name = f.name
  shutil.copy2(Path(doc_path, f_name), Path(from_path, f_name))


