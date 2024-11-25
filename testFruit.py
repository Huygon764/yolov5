from pathlib import Path
from detect import run  # Import the `run` function from `detect.py`

# Define your parameters
weights_path = "weights/Fruits.pt"  # Path to your trained model
source_path = "path-to-img"  # Path to your image
output_path = "runs/detect"  # Output directory for results

# Run the detection
run(weights=weights_path, source=source_path, project=output_path, name="detects", save_txt=True, save_conf=True)

print(f"Inference complete. Results saved in: {output_path}")