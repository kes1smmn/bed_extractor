from distutils.core import setup

setup(
    name='bed_extractor',
    version='1.0',
    packages=[''],
    url='',
    package_data={'bed_extractor' : ['hgnc_complete_set.txt', ]},
    data_files = [('', ['resources/hgnc_complete_set.txt'])],
    license='',
    author='Keith Simmon',
    author_email='keith.simmon@aruplab.com',
    description='extracts lines from bed files with certain names'
)
