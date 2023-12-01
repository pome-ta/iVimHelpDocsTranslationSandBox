from pathlib import Path
import shutil

# 事前にiVim 上でこのファイル(`update.py`) を開く
# iVim でコマンド`:terminal`
# で、ivish を立ち上げ
# `echo $VIMRUNTIME > ./.path` で、ランタイムパスを取得

vimruntime_txt = Path('./.path').read_text().strip()
doc_path = Path(vimruntime_txt, 'doc')
from_path = Path('./iVimDocsMaster')

for f in doc_path.iterdir():
  f_name = f.name
  shutil.copy2(Path(doc_path, f_name), Path(from_path, f_name))

