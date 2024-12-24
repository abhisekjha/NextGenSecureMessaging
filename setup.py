from setuptools import setup, find_packages

setup(
    name='secure_messaging',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'pqcrypto',
        'pycryptodome',
        'pyky', 
        
    ],
    entry_points={
        'console_scripts': [
            'encrypt_files=scripts.encrypt_files:main',
            'decrypt_files=scripts.decrypt_files:main',
        ],
    },
    author='Abhisek Jha',
    author_email='abhisekjha2020@gmail.com',
    description='A secure messaging system using AES-256 and Kyber and Dilithium post-quantum cryptographic algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/abhisekjha/pqc_aes_multipath',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
