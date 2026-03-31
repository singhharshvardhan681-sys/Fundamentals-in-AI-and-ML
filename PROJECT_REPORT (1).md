# Smart Route Optimizer – Project Report

## 1. Approach & Implementation

### Problem Statement
Build a Python application for Transportation & Logistics that allows users to enter two places and calculates the shortest path and travel time using Dijkstra's algorithm.

### Solution Overview
- The project uses a graph data structure to represent places and routes.
- Dijkstra's algorithm is implemented to find the shortest path based on distance or time.
- User inputs start and end locations, and the program outputs the optimal route and cost.
- Sample data is provided in `sample_graph.json` for easy testing.

### Implementation Steps
1. **Graph Representation**: Places and routes are stored in a JSON file and loaded into a Python dictionary.
2. **Dijkstra's Algorithm**: The algorithm is implemented in `route_optimizer.py` to compute shortest paths.
3. **User Interaction**: The script prompts the user for start/end locations and optimization criteria (distance or time).
4. **Result Display**: The shortest route and its cost are displayed to the user.

## 2. Results & Analysis
- The application successfully finds the shortest path and travel time between any two places in the sample graph.
- The solution is efficient for small to medium-sized graphs and can be extended for larger datasets.
- The code is modular and easy to understand, making it suitable for beginners.

## 3. Key Learnings
- Learned how to model real-world problems using graph data structures.
- Gained experience implementing Dijkstra's algorithm in Python.
- Understood the importance of user input validation and clear output formatting.
- Practiced writing clean, maintainable code and technical documentation.

## 4. Setup Instructions
1. Ensure Python 3.x is installed.
2. Clone or download the repository.
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   ```
4. Run the application:
   ```bash
   python route_optimizer.py
   ```
5. Enter start and end locations as prompted.

## 5. Code Details
- `route_optimizer.py`: Main script with graph loading, Dijkstra's algorithm, and user interaction.
- `sample_graph.json`: Sample data for places and routes.
- `README.md`: Technical documentation and setup instructions.
- `.github/copilot-instructions.md`: Project instructions and checklist.

## 6. Repository Access
- Ensure your repository is public or provide necessary access for review.

---
*All fields marked with * are covered above. For further details, see README.md and source code.*
