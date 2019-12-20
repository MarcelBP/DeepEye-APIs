from setuptools import setup

setup(
    name="deepeye_pack",
    version="0.1",
    description="relational dataset visualizations ",
    author="http://dbgroup.cs.tsinghua.edu.cn/ligl/papers/icde18-deepeye.pdf",
    author_email="marcelbutucea@gmail.com",
    url="https://github.com/Thanksyy/DeepEye-APIs",
    license="MIT",
    packages=["deepeye_pack"],
    install_requires=["pandas","numpy","pyecharts"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
