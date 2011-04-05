from setuptools import setup


setup(
    name = 'lemonproject',
    version = '0.1.dev',
    url = 'https://github.com/trilan/lemonproject',
    author = 'Mike Yumatov',
    author_email = 'mike@yumatov.org',
    packages = [
        'lemonproject',
    ],
    include_package_data = True,
    install_requires = [
        'skeleton',
    ],
    entry_points = {
        'console_scripts': [
            'lemonproject = lemonproject.main:run',
        ]
    },
)
