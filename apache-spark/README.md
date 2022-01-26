Spark = Para processamento distribuido = Extrai is dados e manda para o airflow

https://www.freecodecamp.org/news/installing-scala-and-apache-spark-on-mac-os-837ae57d283f/

Step 1: Get Homebrew
Homebrew makes your life a lot easier when it comes to installing applications and languages on a Mac OS. You can get Homebrew by following the instructions on it’s website.

Which basically just tells you to open your terminal and type:

$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

There are more detailed instructions on installing on the project’s GitHub page. Installing everything through Homebrew should automatically add all the appropriate PATH settings to your profile.

Step 2: Installing xcode-select
In order to install Java, Scala, and Spark through the command line we will probably need to install xcode-select and command line developer tools. Go to you terminal and type:

$ xcode-select --install

You will get a prompt that looks something like this:

FfIidYg0docKBqK3RPLGGMOZmTCA3l2mMVMB
Go ahead and select install.

Step 3: Use Homebrew to install Java
Scala is dependent on Java, you may or may not need to install it. The easiest way to install it is to just use HomeBrew:

In your terminal type:

$ brew cask install java

You may need to enter your password at some point to complete the java installation. After running this Homebrew should have taken care of the Java install. Now we can move on to Scala.

Step 4: Use Homebrew to install Scala
Now with Homebrew installed go to your terminal and type:

$ brew install scala

Step 5: Use Homebrew to install Apache Spark
Now with Scala installed go to your terminal and type:

$ brew install apache-spark

Homebrew will now download and install Apache Spark, it may take some time depending on your internet connection.

Step 5: Start the Spark Shell
Now try this command:

$ spark-shell


arquitetura
https://lorenadesouza.medium.com/bootcamp-de-dados-na-tw-spark-6633275480e4
imagem: https://miro.medium.com/max/1192/0*tBMRTDHNwz9XB-oc.jpg

data workflow: https://miro.medium.com/max/640/0*rPq7F0r0JFDcG6v2
https://aprendizadodemaquina.com/artigos/pyspark-entenda-a-engine-do-spark-para-rodar-python/


