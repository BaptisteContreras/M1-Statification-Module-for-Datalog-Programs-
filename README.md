# Statification Module for Datalog Programs

## More information
**See ``` documents ``` folder**

## Authors
Florent CLEMENT (https://gitlab.com/florent.clement)

Baptiste CONTRERAS (https://github.com/BaptisteContreras)

## Installation Windows

### Etape 1 ( ANTLR4 )

- Décompresser l'archive [Antlr4.zip](Antlr4/Antlr4.zip) et la positionner à la racine du lecteur c
- Une fois sur le sous-système linux appliquer les commandes suivantes :

```shell script
export CLASSPATH="/mnt/c/Antlr4/antlr-4.7.1-complete.jar:$CLASSPATH"
export ANTLR4="java -jar /mnt/c/Antlr4/antlr-4.7.1-complete.jar"
alias antlr4="java -jar /mnt/c/Antlr4/antlr-4.7.1-complete.jar"
alias grun="java org.antlr.v4.gui.TestRig"
```

### Etape 2 ( Java )


```shell script
sudo mkdir -p /usr/lib/jvm 
sudo wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
sudo tar xvf openjdk-11.0.2_linux-x64_bin.tar.gz --directory /usr/lib/jvm/
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-11.0.2/bin/java 1
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-11.0.2/bin/javac 1
```
--> [source](https://doc.ubuntu-fr.org/openjdk)

### Etape 3 ( Python )

```shell script
sudo apt install python3-pip
pip3 install --user pytest-cov
pip3 install --user --upgrade coverage
pip3 install antlr4-python3-runtime==4.7.1
```


## How to use
### Run on a file
```python3 Main.py path/to/file```
### Run tests
```make tests```