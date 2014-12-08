from setuptools import setup


setup(name='micropython-uaiohttpclient',
      version='0.3',
      description="""HTTP client for MicroPython's uasyncio,
roughly compatible with aiohttp module.
""",
      url='https://github.com/pfalcon/uaiohttpclient',
      author='Paul Sokolovsky',
      author_email='pfalcon@users.sourceforge.net',
      license='MIT',
      py_modules=['uaiohttpclient'],
      install_requires=['micropython-uasyncio'])
