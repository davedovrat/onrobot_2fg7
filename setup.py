from setuptools import find_packages, setup

package_name = 'onrobot_2fg7'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dave',
    maintainer_email='ddovrat@cs.technion.ac.il',
    description='A client for the OnRobot 2FG7 gripper XML-RPC server',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'status = onrobot_2fg7.status:main',
            'grip = onrobot_2fg7.grip:main'
        ],
    },
)
