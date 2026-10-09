# ENDG 319 CURE

Python work for the ENDG 319 (Fall 2026) CURE project deliverables.

| Folder | Topic |
| --- | --- |
| `Deliverable1/` | Building a pandas dataframe of gasoline and diesel vehicle efficiencies and slicing it with `.iloc` |
| `Deliverable2/` | Graphical analysis of the Breast Cancer Wisconsin (Diagnostic) dataset ahead of building a classification model |

## Running

```
pip install pandas matplotlib
cd Deliverable2
python main.py     # Task 1 output and Figure 1
python task3.py    # Figure 2
```

Each script is run from inside its own folder, since data files are read by relative path.

## Data

`Deliverable2/wdbc.data` is the Breast Cancer Wisconsin (Diagnostic) dataset from the UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
