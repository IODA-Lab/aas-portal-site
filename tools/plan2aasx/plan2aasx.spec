# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all
import os

HERE = SPECPATH  # 이 spec 파일이 있는 폴더(PyInstaller가 넣어 줌)

datas = [(os.path.join(HERE, 'idta_semantics.json'), '.'), (os.path.join(HERE, 'ko_descriptions.json'), '.'), (os.path.join(HERE, 'templates'), 'templates')]
binaries = []
hiddenimports = ['parse_plan', 'generate_aasx', 'validate_aasx', 'run']
datas += collect_data_files('basyx')
hiddenimports += collect_submodules('basyx')
tmp_ret = collect_all('pyecma376_2')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    [os.path.join(HERE, 'gui.py')],
    pathex=[HERE],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='plan2aasx',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
