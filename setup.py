from setuptools import setup, find_packages

setup(
    name='MFEA',
    version='0.1.0',
    packages=find_packages(),  # Automatically finds MFEA/
    install_requires=[],       # Add dependencies here or use requirements.txt
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of what MFEA does.',
    url='https://github.com/yourusername/MFEA',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Adjust license if needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
