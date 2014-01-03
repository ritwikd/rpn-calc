# -*- mode: python -*-
a = Analysis(['rpn-calc.py'],
             pathex=['/home/ritwik/workspace/rpn-calc'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='rpn-calc',
          debug=False,
          strip=None,
          upx=True,
          console=True )
