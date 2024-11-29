from setuptools import setup, find_packages

setup(
    name="wx-payautogui",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui>=0.9.53",
        "pillow>=8.0.0",
        "opencv-python>=4.5.0",
    ],
    author="xiaofang142",
    author_email="myloveisphp@163.com",
    description="A WeChat automation tool based on pyautogui",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xiaofang142/wx-payautogui",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 