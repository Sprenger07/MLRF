# Makefile

# Define variables
PYTHON = python3
DATA_DIR = data
MODEL_DIR = models
DATASET_URL = https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
DATASET_FILE = cifar-10-python.tar.gz

# Default target
all: train

# Download the dataset
download:
	@echo "Downloading the dataset..."
	wget $(DATASET_URL) -O $(DATA_DIR)/raw/$(DATASET_FILE)

# Extract the dataset
extract: download
	@echo "Extracting the dataset..."
	tar -xzf $(DATA_DIR)/raw/$(DATASET_FILE) -C $(DATA_DIR)/raw
	rm $(DATA_DIR)/raw/$(DATASET_FILE)

# Generate data
data: extract
	@echo "Generating data..."
	$(PYTHON) src/data/make_dataset.py --input_dir=$(DATA_DIR)/raw --output_dir=$(DATA_DIR)/processed

# Train the model
train: data
	@echo "Training the model..."
	$(PYTHON) src/models/train_model.py --data_dir=$(DATA_DIR)/processed --model_dir=$(MODEL_DIR)

# Run model prediction
predict: train
	@echo "Running model prediction..."
	$(PYTHON) src/models/predict_model.py --data_dir=$(DATA_DIR)/processed --model_dir=$(MODEL_DIR)

# Generate visualizations
visualize:
	@echo "Generating visualizations..."
	$(PYTHON) src/visualization/visualize.py --data_dir=$(DATA_DIR)/processed --output_dir=reports/figures

# Clean generated data and model
clean:
	@echo "Cleaning up..."
	rm -rf $(DATA_DIR)/raw/*
	rm -rf $(DATA_DIR)/processed/*
	rm -rf $(MODEL_DIR)/*
	rm -rf reports/figures/*

# Install project dependencies
install:
	@echo "Installing project dependencies..."
	pip install -r requirements.txt

# Check code style
check:
	@echo "Checking code style..."
	flake8 src

# Generate documentation
docs:
	@echo "Generating documentation..."
	cd docs && make html

.PHONY: all download extract data train predict visualize clean install docs check
