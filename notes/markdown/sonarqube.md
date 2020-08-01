# Jenkins path to sonar properties

```
{WORKSPACE}/xxx/xxx/sonar-project.properties

```


```python
# must be unique in a given SonarQube instance
sonar.projectKey=tools:status_tenant
# this is the name and version displayed in the SonarQube UI. Was mandatory prior to SonarQube 6.1.
sonar.projectName=Tools Status tenant
sonar.projectVersion=1.0

# Path is relative to the sonar-project.properties file. Replace "/"  by "\" on Windows.
# Since SonarQube 4.2, this property is optional if sonar.modules is set. 
# If not set, SonarQube starts looking for source code from the directory containing 
# the sonar-project.properties file.

# Exlusions
sonar.exclusions=${WORKSPACE}/xxx/xx/xx/xx/**

# Encoding of the source code. Default is default system encoding
sonar.sourceEncoding=UTF-8


# path to source directories (required)
# sonar.sources=srcDir1,srcDir2

# # path to test source directories (optional)
# sonar.tests=testDir1,testDir2

# # path to project binaries (optional), for example directory of Java bytecode
# sonar.binaries=binDir

# # optional comma-separated list of paths to libraries. Only path to JAR file and path to directory of classes are supported.
# sonar.libraries=path/to/library.jar,path/to/classes/dir

# # Uncomment this line to analyse a project which is not a java project.
# # The value of the property must be the key of the language.
# sonar.language=cobol

# # Additional parameters
# sonar.my.property=value

```
