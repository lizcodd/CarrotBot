# -*- mode: python -*-

block_cipher = None


a = Analysis(['cb_frontend.py'],
             pathex=['C:\\Code\\PurpleCarrot'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas += [('purple_carrots.gif', 'C:\\Code\\PurpleCarrot\\purple_carrots.gif', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='cb_frontend',
          debug=False,
          strip=False,
          upx=True,
          console=False )
