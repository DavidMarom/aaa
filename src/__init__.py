# Add src to python path (For imports in directory/pacakge to work properly)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))