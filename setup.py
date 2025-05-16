from setuptools import setup

setup(
    name='kashida_xblock',
    version='0.1',
    description='Kashida XBlock with CKEditor Classic',
    packages=['kashida_xblock'],
    install_requires=[],
    include_package_data=True,
    package_data={
        "kashida_xblock": [
            "templates/html/*.html",
            "static/kashida_xblock/css/*.css",
            "static/kashida_xblock/ckeditor/*"
        ],
    },
    entry_points={
        'xblock.v1': [
            'kashida_xblock = kashida_xblock.block:KashidaXBlock',
        ]
    }
)
