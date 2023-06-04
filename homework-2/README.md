# Q1. Install the package

    conda create -n homework-2-env python=3.9
    conda activate homework-2-env
    
create `requirements.txt`

    pip install -r requirements.txt



    mlflow --version
    mlflow, version 2.3.2

Answer: 2.3.2

# Q2. Download and preprocess the data

    $ ls -lh
    -rw-r--r--  1 henri  staff   150K Jun  3 14:08 dv.pkl
    -rw-r--r--  1 henri  staff   2.5M Jun  3 14:08 test.pkl
    -rw-r--r--  1 henri  staff   2.0M Jun  3 14:08 train.pkl
    -rw-r--r--  1 henri  staff   2.2M Jun  3 14:08 val.pkl

The size of the dv.pkl file is 154kB

# Q3. Train a model with autolog

    $ python train.py --data_path ../../mlops-zoomcamp2/cohorts/2023/02-experiment-tracking/homework/output

The value of the max_depth parameter is 10

# Launch the tracking server locally for MLflow

    $ mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root file:./artifacts

# Q4. Tune model hyperparameters

    $ python hpo.py --data_path ../../mlops-zoomcamp2/cohorts/2023/02-experiment-tracking/homework/output

Answer: 2.45

Q5. Promote the best model to the model registry

2.285

Q6. Promote the best model to the model registry

All are correct
