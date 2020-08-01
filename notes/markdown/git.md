## To delete a local branch

```
 git branch -d the_local_branch        
```                             
         
                
## To remove a remote branch (if you know what you are doing!)
     
```
 git push origin :the_remote_branch
```


## create a branch and switch on

```
git checkout -b <branch>

```

## publish local branch to remote branch

```
 git push -u origin <branch>
```

## Rename your branch

1. Rename your local branch.

 * If you are on the branch you want to rename:
	```
    git branch -m new-name
    ```
    
  * If you are on a different branch:
      ```
        git branch -m old-name new-name
      ```
      
2. Delete the old-name remote branch and push the new-name local branch.

```	
$ git push origin :old-name new-name
```


3. Reset the upstream branch for the new-name local branch.

- Switch to the branch and then

```
$ git push origin -u new-name

```


## Stock tracking changes on a file

* step 1 : 

add file to .gitignore 

* step 2 

```
# git will keep file in local repo but stop tracking changes on the file

$ git rm -r --cached <folder>  

$ git rm --cached <file>

```




