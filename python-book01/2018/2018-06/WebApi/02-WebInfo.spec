# -*- mode: python -*-

block_cipher = None


a = Analysis(['02-WebInfo.py'],
             pathex=['D:\\doc\\นคื๗\\python\\python-book01\\2018\\2018-06\\WebApi'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='02-WebInfo',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
