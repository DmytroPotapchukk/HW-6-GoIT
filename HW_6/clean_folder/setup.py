from setuptools import setup, find_packages


setup(name='clean_folder',
      description='A script for sorting files in a folder',
      author='Dmytro Potapchuk',
      packages=find_packages(),
      entry_points={'console_scripts': [clean-folder=clean_folder.main:main']}
