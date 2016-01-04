from setuptools import setup

README = open('README.md').read()

setup(
        name='lektor-markdown-video',
        author='Khaled Monsoor',
        author_email='k@kmonsoor.com',
        url='https://github.com/kmonsoor/lektor-markdown-video',
        version='0.0.1',
        license='MIT',
        description='converts video links into a embedded video code snippet',
        long_description=README,
        py_modules=['lektor_markdown_video'],
        entry_points={
            'lektor.plugins': [
                'lektor-markdown-video = lektor_markdown_video:MarkdownVideoPlugin',
            ]
        },
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ], requires=['lektor', 'extract_video_id']
)
