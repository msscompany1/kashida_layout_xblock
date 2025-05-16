from setuptools import setup
import os


def package_data(pkg, roots):
    """
    Generic function to find package_data.
    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))
    return {pkg: data}


setup(
    name='xblock-kashida',
    version='0.1.0',
    description='Kashida XBlock with CKEditor',
    long_description='Custom XBlock for Kashida with CKEditor 5 cloud integration.',
    long_description_content_type='text/markdown',
    url='https://github.com/msscompany1/kashida_layout_xblock',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[
        'kashida_xblock',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'kashida_xblock = kashida_xblock.block:KashidaXBlock',
        ]
    },
    package_data=package_data("kashida_xblock", ["static", "public", "translations", "html"]),
    include_package_data=True,
    zip_safe=False,
)
