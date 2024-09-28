import json
import os
import sys
from datetime import datetime

from steps.aggregation import aggregation
from steps.clustering import clustering
from steps.embedding import embedding
from steps.extraction import extraction
from steps.labelling import labelling
from steps.overview import overview
from steps.takeaways import takeaways
from steps.translation import translation
from steps.visualization import visualization
from utils import initialization, run_step, termination


def main():
    config = initialization(sys.argv)

    try:
        run_step("extraction", extraction, config)
        run_step("embedding", embedding, config)
        run_step("clustering", clustering, config)
        run_step("labelling", labelling, config)
        run_step("takeaways", takeaways, config)
        run_step("overview", overview, config)
        # run_step('translation', translation, config)
        run_step("aggregation", aggregation, config)
        run_step("visualization", visualization, config)
        termination(config)
    except Exception as e:
        termination(config, error=e)


if __name__ == "__main__":
    main()
