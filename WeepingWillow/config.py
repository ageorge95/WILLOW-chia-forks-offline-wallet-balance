from os import path

initial_config = {'assets': {'XTWO': {'db_filepath': '{userdir}\\.two\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'two',
                                      'wallet_sk_derivation_port': [8444]},
                             'BALL': {'db_filepath': '{userdir}\\.ball\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'ballcoin',
                                      'wallet_sk_derivation_port': [8444]},
                             'XONE': {'db_filepath': '{userdir}\\.one\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 100000000,
                                      'friendly_name': 'one',
                                      'wallet_sk_derivation_port': [8444]},
                             'KIK': {'db_filepath': '{userdir}\\.kiwi\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000,
                                      'friendly_name': 'kiwi',
                                      'wallet_sk_derivation_port': [8444]},
                             'GBTC': {'db_filepath': '{userdir}\\.greenbtc\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'greenbtc',
                                      'wallet_sk_derivation_port': [8444]},
                             'XCF': {'db_filepath': '{userdir}\\.coffee\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'coffee',
                                     'wallet_sk_derivation_port': [8444]},
                             'MOC': {'db_filepath': '{userdir}\\.moon\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'moon',
                                     'wallet_sk_derivation_port': [8444]},
                             'XSE': {'db_filepath': '{userdir}\\.seno2\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'seno',
                                     'wallet_sk_derivation_port': [8444]},
                             'XPT': {'db_filepath': '{userdir}\\.petroleum\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'petroleum',
                                     'wallet_sk_derivation_port': [8444]},
                             'HCX': {'db_filepath': '{userdir}\\.chinilla\\vanillanet\\db\\blockchain_v2_vanillanet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'chinilla',
                                     'wallet_sk_derivation_port': [8444]},
                             'XGJ': {'db_filepath': '{userdir}\\.goji\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'goji',
                                     'wallet_sk_derivation_port': [8444]},
                             'ECO': {'db_filepath': '{userdir}\\.ecostake\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'ecostake',
                                     'wallet_sk_derivation_port': [8444, 9699]},
                             'XJK': {'db_filepath': '{userdir}\\.joker\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 100000000,
                                     'friendly_name': 'joker',
                                     'wallet_sk_derivation_port': [9699]},
                             'GL': {'db_filepath': '{userdir}\\.gold\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'gold',
                                    'wallet_sk_derivation_port': [8444]},
                             'PROFIT': {'db_filepath': '{userdir}\\.profit\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                        'denominator': 1000000000000,
                                        'friendly_name': 'profit',
                                        'wallet_sk_derivation_port': [8444]},
                             'BPX': {'db_filepath': '{userdir}\\.bpx\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'bpx',
                                     'wallet_sk_derivation_port': [8444]},
                             'LLC': {'db_filepath': '{userdir}\\.littlelambocoin\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000,
                                     'friendly_name': 'littlelambocoin',
                                     'wallet_sk_derivation_port': [8444, 9699]},
                            'AEC': {'db_filepath': '{userdir}\\.aedge\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'aedge',
                                    'wallet_sk_derivation_port': [8444]},
                            'APPLE': {'db_filepath': '{userdir}\\.apple\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'apple',
                                      'wallet_sk_derivation_port': [8444]},
                            'AVO': {'db_filepath': '{userdir}\\.avocado\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'avocado',
                                    'wallet_sk_derivation_port': [8444]},
                            'CAC': {'db_filepath': '{userdir}\\.cactus\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'cactus',
                                    'wallet_sk_derivation_port': [8444]},
                            'CANS': {'db_filepath': '{userdir}\\.cannabis\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'cannabis',
                                     'wallet_sk_derivation_port': [8444]},
                            'CGN': {'db_filepath': '{userdir}\\.chaingreen\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'chaingreen',
                                    'wallet_sk_derivation_port': [8444]},
                            'COV': {'db_filepath': '{userdir}\\.covid\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'covid',
                                    'wallet_sk_derivation_port': [8444]},
                            'GDOG': {'db_filepath': '{userdir}\\.greendoge\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'greendoge',
                                     'wallet_sk_derivation_port': [8444]},
                            'HDD': {'db_filepath': '{userdir}\\.hddcoin\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'hddcoin',
                                    'wallet_sk_derivation_port': [8444]},
                            'LCH': {'db_filepath': '{userdir}\\.lotus\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'lotus',
                                    'wallet_sk_derivation_port': [8444]},
                            'MELON': {'db_filepath': '{userdir}\\.melon\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000,
                                      'friendly_name': 'melon',
                                      'wallet_sk_derivation_port': [8444]},
                            'MGA': {'db_filepath': '{userdir}\\.mogua\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'mogua',
                                    'wallet_sk_derivation_port': [8444]},
                            'NCH': {'db_filepath': '{userdir}\\.chia\\ext9\\db\\blockchain_v1_ext9.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'n-chain_ext9',
                                    'wallet_sk_derivation_port': [8444]},
                            'OZT': {'db_filepath': '{userdir}\\.goldcoin\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'Goldcoin',
                                    'wallet_sk_derivation_port': [8444]},
                            'PEA': {'db_filepath': '{userdir}\\.peas\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'peas',
                                    'wallet_sk_derivation_port': [8444]},
                            'PIPS': {'db_filepath': '{userdir}\\.pipscoin\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'Pipscoin',
                                     'wallet_sk_derivation_port': [8444]},
                            'ROLLS': {'db_filepath': '{userdir}\\.rolls\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'rolls',
                                      'wallet_sk_derivation_port': [8444]},
                            'SCM': {'db_filepath': '{userdir}\\.scam\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'Scamcoin',
                                    'wallet_sk_derivation_port': [8444]},
                            'SIT': {'db_filepath': '{userdir}\\.sit\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'silicoin',
                                    'wallet_sk_derivation_port': [8444]},
                            'SIX': {'db_filepath': '{userdir}\\.lucky\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'lucky',
                                    'wallet_sk_derivation_port': [8444]},
                            'SOCK': {'db_filepath': '{userdir}\\.socks\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'socks',
                                     'wallet_sk_derivation_port': [8444]},
                            'SPARE': {'db_filepath': '{userdir}\\.spare-blockchain\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'spare',
                                      'wallet_sk_derivation_port': [8444]},
                            'STAI': {'db_filepath': '{userdir}\\.stai\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000,
                                     'friendly_name': 'staicoin',
                                     'wallet_sk_derivation_port': [8444]},
                            'STOR': {'db_filepath': '{userdir}\\.stor\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'stor',
                                     'wallet_sk_derivation_port': [8444]},
                            'TAD': {'db_filepath': '{userdir}\\.tad\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'tad',
                                    'wallet_sk_derivation_port': [8444, 9699]},
                            'TRZ': {'db_filepath': '{userdir}\\.tranzact\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'tranzact',
                                    'wallet_sk_derivation_port': [8444]},
                            'WHEAT': {'db_filepath': '{userdir}\\.wheat\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000000000000,
                                      'friendly_name': 'wheat',
                                      'wallet_sk_derivation_port': [8444]},
                            'XBR': {'db_filepath': '{userdir}\\.beernetwork\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'Beer',
                                    'wallet_sk_derivation_port': [8444]},
                            'XBT': {'db_filepath': '{userdir}\\.beet\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'Beet',
                                    'wallet_sk_derivation_port': [8444]},
                            'XBTC': {'db_filepath': '{userdir}\\.btcgreen\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'btcgreen',
                                     'wallet_sk_derivation_port': [8444]},
                            'XCA': {'db_filepath': '{userdir}\\.xcha\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'xcha',
                                    'wallet_sk_derivation_port': [8444]},
                            'XCC': {'db_filepath': '{userdir}\\.chives\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 100000000,
                                    'friendly_name': 'chives',
                                    'wallet_sk_derivation_port': [9699]},
                            'XCD': {'db_filepath': '{userdir}\\.cryptodoge\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000,
                                    'friendly_name': 'cryptodoge',
                                    'wallet_sk_derivation_port': [8444]},
                            'XCH': {'db_filepath': '{userdir}\\.chia\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'chia',
                                    'wallet_sk_derivation_port': [8444]},
                            'XCR': {'db_filepath': '{userdir}\\.chiarose\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000,
                                    'friendly_name': 'chiarose',
                                    'wallet_sk_derivation_port': [8444]},
                            'XDG': {'db_filepath': '{userdir}\\.dogechia\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'dogechia',
                                    'wallet_sk_derivation_port': [8444]},
                            'XETH': {'db_filepath': '{userdir}\\.ethgreen\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000,
                                     'friendly_name': 'ethgreen',
                                     'wallet_sk_derivation_port': [8444]},
                            'XFK': {'db_filepath': '{userdir}\\.fork\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'fork',
                                    'wallet_sk_derivation_port': [8444]},
                            'XFL': {'db_filepath': '{userdir}\\.flora\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'flora',
                                    'wallet_sk_derivation_port': [8444]},
                            'XFX': {'db_filepath': '{userdir}\\.flax\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'flax',
                                    'wallet_sk_derivation_port': [8444]},
                            'XKA': {'db_filepath': '{userdir}\\.kale\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'kale',
                                    'wallet_sk_derivation_port': [8444]},
                            'XKJ': {'db_filepath': '{userdir}\\.kujenga\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'kujenga',
                                    'wallet_sk_derivation_port': [8444]},
                            'XKM': {'db_filepath': '{userdir}\\.mint\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'mint',
                                    'wallet_sk_derivation_port': [8444]},
                            'XKW': {'db_filepath': '{userdir}\\.kiwi\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'Kiwi',
                                    'wallet_sk_derivation_port': [8444]},
                            'XMX': {'db_filepath': '{userdir}\\.melati\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'melati',
                                    'wallet_sk_derivation_port': [8444]},
                            'XMZ': {'db_filepath': '{userdir}\\.maize\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'maize',
                                    'wallet_sk_derivation_port': [8444]},
                            'XNT': {'db_filepath': '{userdir}\\.skynet\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'skynet',
                                    'wallet_sk_derivation_port': [8444]},
                            'XOL': {'db_filepath': '{userdir}\\.olive\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'olive',
                                    'wallet_sk_derivation_port': [8444]},
                            'XSC': {'db_filepath': '{userdir}\\.sector\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'sector',
                                    'wallet_sk_derivation_port': [8444]},
                            'XSHIB': {'db_filepath': '{userdir}\\.shibgreen\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                      'denominator': 1000,
                                      'friendly_name': 'shibgreen',
                                      'wallet_sk_derivation_port': [8444]},
                            'XSLV': {'db_filepath': '{userdir}\\.salvia\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                     'denominator': 1000000000000,
                                     'friendly_name': 'salvia',
                                     'wallet_sk_derivation_port': [8444]},
                            'XTX': {'db_filepath': '{userdir}\\.taco\\mainnet\\db\\blockchain_v2_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'taco',
                                    'wallet_sk_derivation_port': [8444]},
                            'XVM': {'db_filepath': '{userdir}\\.venidium\\mainnet\\db\\blockchain_v1_mainnet.sqlite'.format(userdir=path.expanduser("~")),
                                    'denominator': 1000000000000,
                                    'friendly_name': 'venidium',
                                    'wallet_sk_derivation_port': [8444]}
                                },
                  'CATs': {'XCH': {'CH21': {'ID': '509deafe3cd8bbfbb9ccce1d930e3d7b57b40c964fa33379b18d628175eb7a8f',
                                            'denominator': 1000,
                                            'friendly_name': 'Chia Holiday 2021 token'},
                                   'SBX': {'ID': '78ad32a8c9ea70f27d73e9306fc467bab2a6b15b30289791e37ab6e8612212b1',
                                           'denominator': 1000,
                                           'friendly_name': 'Spacebucks'}},
                           'XCC': {'KTY': {'ID': '3e3a7614a02d9714a21927ef99c7ef9bf8270e374dc6ecc48f2619cbc70c4ddc',
                                           'denominator': 1000,
                                           'friendly_name': 'chives kitty'},
                                   }
                           }
                  }