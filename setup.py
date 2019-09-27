from distutils.core import setup

setup(name='csf_kit',
      version='0.1',
      description='StartKit for ChinaScope data',
      author='ChinaScope',
      packages=['csf_kit', 'csf_kit.news', 'csf_kit.news.sample_code'],
      package_data={'csf_kit': ['data/*']},
      requires=[]
      )