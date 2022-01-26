Airflow = Para orquestração de trabalhos = Jenkins

https://airflow.apache.org/


https://airflow.apache.org/docs/apache-airflow/stable/start/index.html

https://airflow.apache.org/docs/apache-airflow/stable/start/local.html


# Airflow needs a home. `~/airflow` is the default, but you can put it
# somewhere else if you prefer (optional)
export AIRFLOW_HOME=~/airflow

# Install Airflow using the constraints file
AIRFLOW_VERSION=2.2.3
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.6
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-3.6.txt
python3 -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone # cria db e estarta
airflow webserver # estarta
airflow scheduler # estarta scheduler

# Visit localhost:8080 in the browser and use the admin account details
# shown on the terminal to login.
# Enable the example_bash_operator dag in the home page


<!-- acessar sem usuário e senha -->
<!-- https://stackoverflow.com/questions/57680082/how-do-i-disable-airflow-login-for-authentication-and-authorization -->

airflow users  create --role Admin --username danilo --email danilo@teste.com --firstname Danilo --lastname Aparecido --password danilo

user:danilo 
password: danilo


airflow users  create --role Admin --username danilo2 --email danilo2@teste.com --firstname Danilo2 --lastname Aparecido --password danilo2



extra alura
# Vamos então começar criando um ambiente virtual em Python, na versão 3.7.

mkdir datapipeline
cd datapipeline
python3 -m venv .env
source .env/bin/activate
# Criaremos uma variável de ambiente que aponta para a pasta onde o Airflow será instalado:

export AIRFLOW_HOME=$(pwd)/airflow
# Lembre sempre de manter esta variável ativa, caso contrário o Airflow será criado na pasta raiz do usuário. Feito isso, # instalaremos o Airflow em nosso ambiente, aqui estamos usando a versão 1.10.14:

pip install apache-airflow==1.10.14 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.14/constraints-3.7.txt"
# Após instalar Airflow, iniciaremos o banco de dados da ferramenta:

airflow initdb
# E para iniciar o serviço Webserver, responsável pela interface da ferramenta, digitaremos:

airflow webserver

# ou

airflow standalone

# Acessaremos a interface do Airflow no navegador usando o link: http://localhost:8080.

# E para iniciarmos o serviço Scheduler, responsável pelo agendamento de tarefas para execução, digitaremos:

airflow scheduler