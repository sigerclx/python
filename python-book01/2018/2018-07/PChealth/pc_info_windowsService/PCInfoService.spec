# -*- mode: python -*-

block_cipher = None


a = Analysis(['PCInfoService.py'],
             pathex=['D:\\doc\\����\\python\\python-book01\\2018\\2018-07\\PChealth\\pc_info_windowsService'],
             binaries=[],
             datas=[],
             hiddenimports=['win32timezone'],
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
          name='PCInfoService',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='car.ico')
