# -*- mode: python ; coding: utf-8 -*-
import sys

block_cipher = None


a = Analysis(['_00_CLI.py'],
             pathex=[],
             binaries=[],
             datas=[('icon.ico', '.'),
			  ('version.txt', '.'),
              ('donation.gif', '.'),
              (sys.prefix+r'/tcl/tix8.4.3', 'tcl/tix8.4.3'),
              ('chia_blockchain/chia', 'chia_blockchain/chia')],
             hiddenimports=['tabulate',
							'pyinstaller',
							'yaml',
							'aiohttp',
							'aiosqlite',
							'bitstring',
							'blspy',
							'chiabip158',
							'chiapos',
							'chiavdf',
							'click',
							'clvm',
							'clvm_tools',
							'colorama',
							'colorlog',
							'concurrent-log-handler',
							'cryptography',
							'dnspython',
							'fasteners',
							'keyrings.cryptfile.cryptfile',
							'watchdog.events',
							'watchdog.observers',
							'websockets',
							'pillow',
							'requests',
							'dataclasses',
							'clvm_tools.curry',
							'clvm_tools.clvmc',
							'clvm_rs',
							'chia_rs'
			 ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='_00_CLI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
		  icon='icon.ico' )
