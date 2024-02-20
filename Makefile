install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 

train:
	python train.py

eval:
	echo "## Model Metrics" > report.md
	cat ./Results/metrics.txt >> report.md
	
	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](./Results/model_results.png)' >> report.md
	
	cml comment create report.md
		
update-branch:
	git config --global user.name $(USER_NAME)
	git config --global user.email $(USER_EMAIL)
	git commit -am "Update with new results"
	git push --force origin HEAD:update

hf-login: 
	pip install -U "huggingface_hub[cli]"
	git pull origin update
	git switch update
	huggingface-cli login --token $(HF) --add-to-git-credential

<<<<<<< HEAD
push-hub:
    huggingface-cli upload TMSV/Drug-Classification ./APP --repo-type=space --commit-message="Sync App files"
    huggingface-cli upload TMSV/Drug-Classification ./Model --repo-type=space --commit-message="Sync Model"
    huggingface-cli upload TMSV/Drug-Classification ./Results --repo-type=space --commit-message="Sync Results"
=======
push-hub: 
	huggingface-cli upload kingabzpro/Drug-Classification ./App --repo-type=space --commit-message="Sync App files"
	huggingface-cli upload kingabzpro/Drug-Classification ./Model /Model --repo-type=space --commit-message="Sync Model"
	huggingface-cli upload kingabzpro/Drug-Classification ./Results /Metrics --repo-type=space --commit-message="Sync Model"
>>>>>>> feca31fb49dc1b0b5b2bcb122c94a58cb71c3640

deploy: hf-login push-hub

all: install format train eval update-branch deploy