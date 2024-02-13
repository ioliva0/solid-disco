from roboflow import Roboflow
rf = Roboflow(api_key="E8CAPw1bXxXMtEZcLrwe")
project = rf.workspace("tennis-3ll0a").project("tennis-ball-icifx")
dataset = project.version(1).download("yolov8")
