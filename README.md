# Running inside a container

The code is developed using development containers which make development easier inside visual studio code. The assignment uses python 3.9 and pytest which are installed using Dockerfile. If using vscode, select the ```Remote-Containers: Open Folder in Container``` option and wait for the image to be built. Alternatively, build the image using Docker and share the root of the project as a volume when running the container outside of vsCode. 


# Build, test and run

use pytest in the assignment root directory to run the tests 

```pytest```

The test results will be stored in the test-results directory

To run the app with sample inputs, use the following command in the assignment root directory

```python main.py SST 1 2 3 4 5 6```
