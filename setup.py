from setuptools import setup


setup(
    name = 'lemon-project-templates',
    version = '0.1.dev',
    url = 'https://github.com/trilan/lemon-project-templates',
    author = 'Mike Yumatov',
    author_email = 'mike@yumatov.org',
    packages = [
        'lemon_project_templates',
    ],
    include_package_data = True,
    install_requires = [
        'skeleton',
    ],
    entry_points = {
        'console_scripts': [
            'lemonproject = lemon_project_templates.main:run',
        ]
    },
)
