import argparse
import yaml, json
from alectio_sdk.sdk import Pipeline
from processes import train, test, infer, getdatasetstate

with open("./config.yaml", "r") as stream:
    args = yaml.safe_load(stream)

# put the train/test/infer processes into the constructor
AlectioPipeline = Pipeline(
    name=args["exp_name"],
    train_fn=train,
    test_fn=test,
    infer_fn=infer,
    getstate_fn=getdatasetstate,
    args=args,
    token="a0941db31c3f4c6fbf8d08b89556ba9d",
)

if __name__ == "__main__":
    AlectioPipeline()   