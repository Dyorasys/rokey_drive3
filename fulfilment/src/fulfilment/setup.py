from setuptools import find_packages, setup

package_name = 'fulfilment'

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
    maintainer='oh',
    maintainer_email='oh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'conv_hand = fulfilment.conveyor:main', # 손으로 만든 컨베이어 벨트 동작
            'pub_hand = fulfilment.publish:main',   # 명령
            'input_hand = fulfilment.conveyor_c_p_1:main',  # 사용자 명령
            'sub_hand = fulfilment.sub:main',   # 수신
            'conv = fulfilment.conveyor_gui:main',  # 컨베이어 벨트 동작
            'gui = fulfilment.Gui_node:main',   # gui
            'yolo = fulfilment.yolo:main',  # yolo처리 노드
            'cam = fulfilment.camera:main', # camera 읽어오는 노드
            'gui_big = fulfilment.Gui_node_v1:main',    # 큰화면 gui
        ],
    },
)
