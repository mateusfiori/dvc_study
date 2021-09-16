
# DVC Study

Repository created as hands-on study on understanding how DVC works, and how
to version control machine learning models.




## Installation

Before anything DVC must be installed on your system. 
To do so follow the command below.

```
pip install dvc
```

Obs: I suggest using venv or conda as a python environment.
    
### Usage/Examples

Follow the commands below to init the GIT and DVC repository.

```
git init
dvc init
```

After that add the model file to DVC.

```
dvc add <path-to-model-file>
```

A .dvc file will be created. That's the file that will be used by GIT
to version control the model(s).

```
git add <path-to-dvc-file> <.gitignore>
```

To configure a remote repository execute the following command.

```
dvc remote add -d storage <path-to-remote-repository>
git add .dvc/config
```

And to push the model file the commando below.

```
dvc push
```

If DVC was already configured use the following.

```
dvc pull
```
## Conclusion

Basically DVC is a tool that enhances GIT usage in terms of versioning
big files (e.g. models or datasets).
The actual file won't be stored on GIT but on DVC repository.
GIT will use the .dvc to version control the model file.
So whenever the model file is changed, it must be added to DVC and the .dvc on 
GIT must be added and commited. 
  