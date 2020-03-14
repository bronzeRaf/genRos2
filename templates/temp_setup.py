# This is a template of the setup.py of ROS2 packages
#
# Written in 14/2/2020
# Written by Rafael Brouzos



from setuptools import setup

package_name = '{{data.packageName}}'

setup(
    name = package_name,
    version = '0.0.0',
    packages = [package_name],
    data_files = [
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires = ['setuptools'],
    zip_safe = True,
    maintainer = '{{data.maintainer}}',
    maintainer_email = '{{data.email}}',
    description = '{{data.description}}',
    license = '{{data.license}}',
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
		{% for en in entry_points %}
		{{en}}
		{% endfor %}
        ],
    },
)
